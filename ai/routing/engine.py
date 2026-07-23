"""
AI Routing Engine

Orchestrates task classification, profile selection, and execution.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, Callable, List, Union
from enum import Enum
import time
import logging

from ..profiles.profiles import (
    ReasoningProfile, ProfileConfig, get_profile, PROFILES
)
from ..classifier.classifier import (
    TaskClassifier, TaskCharacteristics, TaskCategory, ComplexityLevel
)
from ..ir.hybrid_ir import HybridIRSystem, IRConfig, RetrievedContext


logger = logging.getLogger(__name__)


class SelectionStrategy(Enum):
    """Strategy for profile selection."""
    DIRECT = "direct"           # Direct mapping from category
    WEIGHTED = "weighted"       # Weighted scoring
    CASCADE = "cascade"         # Escalate until confidence met
    PARALLEL = "parallel"      # Execute multiple, pick best


@dataclass
class SelectionCriteria:
    """Criteria for profile selection."""
    strategy: SelectionStrategy = SelectionStrategy.WEIGHTED
    cascade_confidence_threshold: float = 0.7
    max_cascade_depth: int = 3
    enable_ir_fallback: bool = True
    parallel_threshold: float = 0.6


@dataclass
class ExecutionResult:
    """Result of executing a task."""
    profile_used: str
    response: str
    latency_ms: float
    cost_estimate: float
    confidence: float
    ir_contexts: List[RetrievedContext] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TaskRequest:
    """A task to be processed."""
    task_id: str
    prompt: str
    category: Optional[TaskCategory] = None  # Explicit category
    explicit_profile: Optional[str] = None   # Explicit profile preference
    context: Optional[str] = None            # Additional context
    priority: str = "normal"               # normal, high, low
    user_id: Optional[str] = None
    session_id: Optional[str] = None


class ProfileSelector:
    """Selects the appropriate profile based on task characteristics."""
    
    # Profile scores for each category
    CATEGORY_SCORES: Dict[TaskCategory, Dict[ReasoningProfile, float]] = {
        TaskCategory.RETRIEVAL_SIMPLE: {
            ReasoningProfile.FAST: 0.95,
            ReasoningProfile.BALANCED: 0.70,
            ReasoningProfile.HYBRID_IR: 0.50,
        },
        TaskCategory.RETRIEVAL_COMPLEX: {
            ReasoningProfile.HYBRID_IR: 0.90,
            ReasoningProfile.DEEP: 0.80,
            ReasoningProfile.BALANCED: 0.60,
        },
        TaskCategory.VALIDATION_STANDARD: {
            ReasoningProfile.BALANCED: 0.85,
            ReasoningProfile.VERIFICATION: 0.75,
            ReasoningProfile.FAST: 0.50,
        },
        TaskCategory.VALIDATION_SAFETY: {
            ReasoningProfile.VERIFICATION: 0.95,
            ReasoningProfile.BALANCED: 0.60,
            ReasoningProfile.DEEP: 0.80,
        },
        TaskCategory.VALIDATION_CRITICAL: {
            ReasoningProfile.VERIFICATION: 0.98,
            ReasoningProfile.DEEP: 0.85,
        },
        TaskCategory.GENERATION_SIMPLE: {
            ReasoningProfile.FAST: 0.80,
            ReasoningProfile.BALANCED: 0.75,
        },
        TaskCategory.GENERATION_STANDARD: {
            ReasoningProfile.BALANCED: 0.90,
            ReasoningProfile.HYBRID_IR: 0.70,
            ReasoningProfile.CREATIVE: 0.60,
        },
        TaskCategory.GENERATION_CREATIVE: {
            ReasoningProfile.CREATIVE: 0.90,
            ReasoningProfile.DEEP: 0.75,
        },
        TaskCategory.ANALYSIS_STANDARD: {
            ReasoningProfile.BALANCED: 0.75,
            ReasoningProfile.DEEP: 0.85,
        },
        TaskCategory.ANALYSIS_COMPLEX: {
            ReasoningProfile.DEEP: 0.95,
            ReasoningProfile.HYBRID_IR: 0.80,
        },
        TaskCategory.SYNTHESIS: {
            ReasoningProfile.DEEP: 0.90,
            ReasoningProfile.CREATIVE: 0.75,
            ReasoningProfile.HYBRID_IR: 0.80,
        },
        TaskCategory.EXPLANATION: {
            ReasoningProfile.HYBRID_IR: 0.90,
            ReasoningProfile.BALANCED: 0.70,
        },
        TaskCategory.PLANNING_SIMPLE: {
            ReasoningProfile.BALANCED: 0.80,
            ReasoningProfile.FAST: 0.60,
        },
        TaskCategory.PLANNING_COMPLEX: {
            ReasoningProfile.DEEP: 0.85,
            ReasoningProfile.CREATIVE: 0.80,
        },
        TaskCategory.DEBUGGING: {
            ReasoningProfile.DIAGNOSTIC: 0.90,
            ReasoningProfile.DEEP: 0.75,
        },
        TaskCategory.DIAGNOSIS: {
            ReasoningProfile.DIAGNOSTIC: 0.95,
            ReasoningProfile.DEEP: 0.80,
        },
        TaskCategory.UNKNOWN: {
            ReasoningProfile.BALANCED: 0.90,
        },
    }
    
    def select(
        self,
        characteristics: TaskCharacteristics,
        criteria: SelectionCriteria
    ) -> ProfileConfig:
        """
        Select the best profile for task characteristics.
        
        Args:
            characteristics: Classified task characteristics
            criteria: Selection criteria
            
        Returns:
            Selected profile configuration
        """
        # Apply explicit preference if provided
        if characteristics.explicit_keywords:
            for keyword in characteristics.explicit_keywords:
                if keyword in [p.value for p in ReasoningProfile]:
                    return get_profile(keyword)
        
        # Get scores for category
        category_scores = self.CATEGORY_SCORES.get(
            characteristics.category,
            self.CATEGORY_SCORES[TaskCategory.UNKNOWN]
        )
        
        # Adjust for complexity
        adjusted_scores = self._adjust_for_complexity(
            characteristics, category_scores
        )
        
        # Adjust for latency tolerance
        adjusted_scores = self._adjust_for_latency(
            characteristics, adjusted_scores
        )
        
        # Select best profile
        if adjusted_scores:
            best_profile = max(adjusted_scores, key=adjusted_scores.get)
            return PROFILES[best_profile]
        
        # Default to balanced
        return PROFILES[ReasoningProfile.BALANCED]
    
    def _adjust_for_complexity(
        self,
        characteristics: TaskCharacteristics,
        scores: Dict[ReasoningProfile, float]
    ) -> Dict[ReasoningProfile, float]:
        """Adjust scores based on complexity level."""
        if characteristics.complexity == ComplexityLevel.VERY_HIGH:
            # Prefer deep reasoning
            return {
                p: s * (2.0 if p in [ReasoningProfile.DEEP, ReasoningProfile.DIAGNOSTIC] else 0.7)
                for p, s in scores.items()
            }
        elif characteristics.complexity in [ComplexityLevel.LOW, ComplexityLevel.TRIVIAL]:
            # Prefer fast
            return {
                p: s * (2.0 if p == ReasoningProfile.FAST else 0.7)
                for p, s in scores.items()
            }
        return scores
    
    def _adjust_for_latency(
        self,
        characteristics: TaskCharacteristics,
        scores: Dict[ReasoningProfile, float]
    ) -> Dict[ReasoningProfile, float]:
        """Adjust scores based on latency tolerance."""
        if characteristics.latency_tolerance == "instant":
            return {
                p: s * (3.0 if p == ReasoningProfile.FAST else 0.3)
                for p, s in scores.items()
            }
        elif characteristics.latency_tolerance == "patient":
            return {
                p: s * (2.0 if p in [ReasoningProfile.DEEP, ReasoningProfile.CREATIVE] else 0.8)
                for p, s in scores.items()
            }
        return scores


class RoutingEngine:
    """
    Main routing engine that orchestrates task processing.
    
    Pipeline:
    1. Classify task
    2. Select profile
    3. Execute (with optional IR)
    4. Return response
    """
    
    def __init__(
        self,
        classifier: Optional[TaskClassifier] = None,
        selector: Optional[ProfileSelector] = None,
        ir_system: Optional[HybridIRSystem] = None,
        executor: Optional[Callable] = None,
        criteria: Optional[SelectionCriteria] = None,
        telemetry: Optional[Any] = None
    ):
        self.classifier = classifier or TaskClassifier()
        self.selector = selector or ProfileSelector()
        self.ir_system = ir_system
        self.executor = executor or self._default_executor
        self.criteria = criteria or SelectionCriteria()
        self.telemetry = telemetry
    
    def process(self, request: TaskRequest) -> ExecutionResult:
        """
        Process a task through the routing pipeline.
        
        Args:
            request: The task request
            
        Returns:
            ExecutionResult with response and metadata
        """
        start_time = time.time()
        
        # Step 1: Classify task
        characteristics = self.classifier.classify(
            request.prompt,
            explicit_category=request.category
        )
        
        # Step 2: Select profile
        profile = self.selector.select(characteristics, self.criteria)
        
        # Step 3: Prepare prompt (with optional IR)
        prepared_prompt = self._prepare_prompt(request, characteristics, profile)
        
        # Step 4: Execute
        response, raw_metadata = self.executor(
            prepared_prompt,
            profile.name,
            request.prompt
        )
        
        # Step 5: Compile result
        elapsed_ms = (time.time() - start_time) * 1000
        
        result = ExecutionResult(
            profile_used=profile.name,
            response=response,
            latency_ms=elapsed_ms,
            cost_estimate=self._estimate_cost(profile, elapsed_ms),
            confidence=characteristics.classification_confidence,
            ir_contexts=getattr(self.ir_system, 'last_contexts', []) if self.ir_system else [],
            metadata={
                'category': characteristics.category.value,
                'complexity': characteristics.complexity.name,
                'retrieval_used': characteristics.retrieval_required,
                'profile_config': profile.name,
                **raw_metadata
            }
        )
        
        # Step 6: Log to telemetry
        if self.telemetry:
            self.telemetry.log_decision(
                request=request,
                characteristics=characteristics,
                profile_selected=profile,
                result=result
            )
        
        return result
    
    def _prepare_prompt(
        self,
        request: TaskRequest,
        characteristics: TaskCharacteristics,
        profile: ProfileConfig
    ) -> str:
        """Prepare prompt with IR context if needed."""
        if not self.ir_system or not characteristics.retrieval_required:
            return request.prompt
        
        if not self.ir_system.retriever:
            return request.prompt
        
        return self.ir_system.process(
            query=request.prompt,
            user_prompt=request.prompt,
            max_context_tokens=profile.context_window
        )
    
    def _default_executor(
        self,
        prompt: str,
        profile_name: str,
        original_prompt: str
    ) -> tuple[str, Dict[str, Any]]:
        """
        Default executor placeholder.
        
        In production, this would call the actual AI model.
        """
        # Placeholder implementation
        return (
            f"[{profile_name}] Processed: {original_prompt[:100]}...",
            {"executor": "placeholder", "model_used": "unknown"}
        )
    
    def _estimate_cost(self, profile: ProfileConfig, latency_ms: float) -> float:
        """Estimate cost based on profile and latency."""
        # Simplified cost model
        base_cost_per_second = {
            'fast': 0.001,
            'balanced': 0.005,
            'deep': 0.020,
            'verification': 0.015,
            'creative': 0.018,
            'hybrid_ir': 0.012,
            'diagnostic': 0.018
        }
        
        profile_key = profile.name.lower()
        rate = base_cost_per_second.get(profile_key, 0.005)
        
        return rate * (latency_ms / 1000)
    
    def cascade_execute(
        self,
        request: TaskRequest,
        max_depth: int = 3
    ) -> ExecutionResult:
        """
        Execute with cascade: start simple, escalate if needed.
        
        Args:
            request: The task request
            max_depth: Maximum cascade depth
            
        Returns:
            ExecutionResult from final (or first successful) profile
        """
        results: List[ExecutionResult] = []
        
        # Profile order for cascade
        cascade_order = [
            ReasoningProfile.FAST,
            ReasoningProfile.BALANCED,
            ReasoningProfile.DEEP
        ]
        
        for i, profile_enum in enumerate(cascade_order[:max_depth]):
            result = self.process(request)
            results.append(result)
            
            # Check if confidence is acceptable
            if result.confidence >= self.criteria.cascade_confidence_threshold:
                result.metadata['cascade_depth'] = i + 1
                result.metadata['cascade_tried'] = len(results)
                return result
        
        # Return best result from cascade
        best = max(results, key=lambda r: r.confidence)
        best.metadata['cascade_depth'] = len(results)
        best.metadata['cascade_tried'] = len(results)
        return best


def create_routing_engine(
    documents: Optional[List[Dict[str, str]]] = None,
    **config_kwargs
) -> RoutingEngine:
    """
    Factory function to create a configured routing engine.
    
    Args:
        documents: Documents for IR system
        **config_kwargs: Configuration overrides
        
    Returns:
        Configured RoutingEngine
    """
    from ..ir.hybrid_ir import create_ir_system
    
    classifier = TaskClassifier()
    selector = ProfileSelector()
    
    if documents:
        ir_system = create_ir_system(documents=documents)
    else:
        ir_system = None
    
    return RoutingEngine(
        classifier=classifier,
        selector=selector,
        ir_system=ir_system
    )
