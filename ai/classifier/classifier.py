"""
Task Classifier Module

Classifies engineering tasks and determines reasoning complexity.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Set
import re


class TaskCategory(Enum):
    """Engineering task categories."""
    RETRIEVAL_SIMPLE = "retrieval_simple"
    RETRIEVAL_COMPLEX = "retrieval_complex"
    VALIDATION_STANDARD = "validation_standard"
    VALIDATION_SAFETY = "validation_safety"
    VALIDATION_CRITICAL = "validation_critical"
    GENERATION_SIMPLE = "generation_simple"
    GENERATION_STANDARD = "generation_standard"
    GENERATION_CREATIVE = "generation_creative"
    ANALYSIS_STANDARD = "analysis_standard"
    ANALYSIS_COMPLEX = "analysis_complex"
    SYNTHESIS = "synthesis"
    EXPLANATION = "explanation"
    PLANNING_SIMPLE = "planning_simple"
    PLANNING_COMPLEX = "planning_complex"
    DEBUGGING = "debugging"
    DIAGNOSIS = "diagnosis"
    UNKNOWN = "unknown"


class ComplexityLevel(Enum):
    """Reasoning complexity levels."""
    TRIVIAL = 1   # Single lookup
    LOW = 2        # 1-2 steps
    MEDIUM = 3      # 3-5 steps
    HIGH = 4        # 6-10 steps
    VERY_HIGH = 5    # 10+ steps


@dataclass
class TaskCharacteristics:
    """Characteristics of a task that influence profile selection."""
    
    # Core attributes
    category: TaskCategory = TaskCategory.UNKNOWN
    complexity: ComplexityLevel = ComplexityLevel.MEDIUM
    context_required: int = 8000  # tokens
    retrieval_required: bool = False
    verification_level: int = 0  # 0-5
    safety_critical: bool = False
    
    # Additional attributes
    latency_tolerance: str = "moderate"  # instant, fast, moderate, patient, async
    cost_priority: bool = False  # True if cost is a priority
    quality_priority: bool = True  # True if quality is priority
    creativity_required: bool = False
    
    # Source indicators
    explicit_keywords: List[str] = field(default_factory=list)
    implicit_signals: List[str] = field(default_factory=list)
    
    # Confidence in classification
    classification_confidence: float = 0.5  # 0.0-1.0
    
    @property
    def reasoning_depth_estimate(self) -> int:
        """Estimated reasoning depth needed."""
        return self.complexity.value * 2


class TaskClassifier:
    """
    Classifies engineering tasks based on their characteristics.
    
    Supports multiple classification strategies:
    - Keyword-based (fast, no training)
    - Heuristic-based (rule-based patterns)
    - Explicit type specification
    """
    
    # Keyword patterns for category detection
    CATEGORY_PATTERNS: Dict[TaskCategory, List[str]] = {
        TaskCategory.RETRIEVAL_SIMPLE: [
            r'\bwhat\s+is\b', r'\bdefine\b', r'\blookup\b', r'\bcolor\b',
            r'\bstandard\b', r'\bcode\b', r'\bretrieve\b', r'\bfind\b',
            r'\bget\b.*\bstandard\b', r'\blist\b.*\brequirements\b'
        ],
        TaskCategory.RETRIEVAL_COMPLEX: [
            r'\bfind\s+all\b', r'\bsearch\b.*\bcomprehensive\b',
            r'\blookup\b.*\bmultiple\b', r'\bretrieve\b.*\bcontext\b'
        ],
        TaskCategory.VALIDATION_STANDARD: [
            r'\bvalidate\b', r'\bcheck\b', r'\bverify\b',
            r'\bconfirm\b', r'\btest\b', r'\bassess\b'
        ],
        TaskCategory.VALIDATION_SAFETY: [
            r'\bverify\b.*\bsafety\b', r'\bcompliance\b', r'\baudit\b',
            r'\bcertify\b', r'\bproof\b', r'\bcritical\b',
            r'\bvalidate\b.*\bstandard\b', r'\bcheck\b.*\bregulation\b'
        ],
        TaskCategory.VALIDATION_CRITICAL: [
            r'\bvalidate\b.*\bsafety[\s_-]critical\b', r'\bproof\b',
            r'\bformal\s+verification\b', r'\bcertification\b'
        ],
        TaskCategory.GENERATION_SIMPLE: [
            r'\bcreate\b.*\bsimple\b', r'\bgenerate\b.*\bbasic\b',
            r'\bdraw\b.*\bsymbol\b', r'\bmake\b.*\bquick\b'
        ],
        TaskCategory.GENERATION_STANDARD: [
            r'\bgenerate\b', r'\bcreate\b', r'\bproduce\b',
            r'\bbuild\b', r'\bcompose\b', r'\bdesign\b'
        ],
        TaskCategory.GENERATION_CREATIVE: [
            r'\bdesign\b.*\balternative\b', r'\bsuggest\b.*\bnovel\b',
            r'\bcreate\b.*\binnovative\b', r'\bgenerate\b.*\bcreative\b',
            r'\bpropose\b.*\bnew\b', r'\b brainstorm\b'
        ],
        TaskCategory.ANALYSIS_STANDARD: [
            r'\banalyze\b', r'\bexamine\b', r'\binvestigate\b',
            r'\bevaluate\b', r'\bassess\b'
        ],
        TaskCategory.ANALYSIS_COMPLEX: [
            r'\banalyze\b.*\bcomprehensive\b', r'\bevaluate\b.*\bdeep\b',
            r'\bresearch\b', r'\bdeep\s+analysis\b', r'\bthorough\b.*\bexamine\b'
        ],
        TaskCategory.SYNTHESIS: [
            r'\bsynthesize\b', r'\bcombine\b.*\bmultiple\b',
            r'\bintegrate\b', r'\bmerge\b.*\bsources\b',
            r'\bcomprehensive\b.*\breport\b'
        ],
        TaskCategory.EXPLANATION: [
            r'\bexplain\b', r'\bwhy\b', r'\bbecause\b',
            r'\bdescribe\b.*\breason\b', r'\bclarify\b',
            r'\bgrounded\b.*\bexplanation\b'
        ],
        TaskCategory.PLANNING_SIMPLE: [
            r'\bplan\b.*\bsimple\b', r'\bschedule\b.*\bbasic\b',
            r'\boutline\b.*\bsteps\b'
        ],
        TaskCategory.PLANNING_COMPLEX: [
            r'\bplan\b.*\bcomplex\b', r'\boptimize\b',
            r'\bsequence\b.*\bdependencies\b', r'\bstrategize\b'
        ],
        TaskCategory.DEBUGGING: [
            r'\bdebug\b', r'\btroubleshoot\b', r'\bfix\b.*\berror\b',
            r'\bwhy\s+failed\b', r'\bidentify\b.*\bproblem\b'
        ],
        TaskCategory.DIAGNOSIS: [
            r'\bdiagnose\b', r'\broot\s+cause\b',
            r'\binvestigate\b.*\bfailure\b', r'\btroubleshoot\b.*\bsystematic\b'
        ],
    }
    
    # Complexity modifiers
    COMPLEXITY_INCREASERS: List[str] = [
        r'\bcomprehensive\b', r'\bdeep\b', r'\bthorough\b',
        r'\banalyze\b.*\ball\b', r'\bmultiple\b', r'\bcomplex\b',
        r'\bsystematic\b', r'\bdetailed\b'
    ]
    
    COMPLEXITY_DECREASERS: List[str] = [
        r'\bsimple\b', r'\bquick\b', r'\bbasic\b',
        r'\bjust\b', r'\bonly\b', r'\bsingle\b'
    ]
    
    # Safety indicators
    SAFETY_KEYWORDS: List[str] = [
        r'\bsafety\b', r'\bcritical\b', r'\bregulation\b',
        r'\bcompliance\b', r'\baudit\b', r'\bcertif\b'
    ]
    
    def __init__(self):
        """Initialize the classifier with compiled patterns."""
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Pre-compile regex patterns for performance."""
        self._compiled_patterns: Dict[TaskCategory, List[re.Pattern]] = {}
        for category, patterns in self.CATEGORY_PATTERNS.items():
            self._compiled_patterns[category] = [
                re.compile(p, re.IGNORECASE) for p in patterns
            ]
        
        self._complexity_increasers = [
            re.compile(p, re.IGNORECASE) for p in self.COMPLEXITY_INCREASERS
        ]
        self._complexity_decreasers = [
            re.compile(p, re.IGNORECASE) for p in self.COMPLEXITY_DECREASERS
        ]
        self._safety_patterns = [
            re.compile(p, re.IGNORECASE) for p in self.SAFETY_KEYWORDS
        ]
    
    def classify(self, task: str, explicit_category: Optional[TaskCategory] = None) -> TaskCharacteristics:
        """
        Classify a task based on its description.
        
        Args:
            task: Natural language description of the task
            explicit_category: If provided, use this category directly
            
        Returns:
            TaskCharacteristics describing the task
        """
        if explicit_category:
            return self._classify_explicit(task, explicit_category)
        
        return self._classify_implicit(task)
    
    def _classify_explicit(self, task: str, category: TaskCategory) -> TaskCharacteristics:
        """Classify with explicit category specification."""
        characteristics = TaskCharacteristics(
            category=category,
            complexity=self._estimate_complexity(task),
            context_required=self._estimate_context(task),
            retrieval_required=category in [
                TaskCategory.RETRIEVAL_COMPLEX, TaskCategory.SYNTHESIS,
                TaskCategory.ANALYSIS_COMPLEX, TaskCategory.EXPLANATION
            ],
            verification_level=self._estimate_verification_level(task, category),
            safety_critical=category in [
                TaskCategory.VALIDATION_SAFETY, TaskCategory.VALIDATION_CRITICAL
            ],
            latency_tolerance=self._estimate_latency_tolerance(task),
            classification_confidence=0.95  # Explicit is high confidence
        )
        characteristics.explicit_keywords = [category.value]
        return characteristics
    
    def _classify_implicit(self, task: str) -> TaskCharacteristics:
        """Classify based on keyword and pattern matching."""
        matched_categories: Dict[TaskCategory, int] = {}
        
        # Count pattern matches
        for category, patterns in self._compiled_patterns.items():
            matches = sum(1 for pattern in patterns if pattern.search(task))
            if matches > 0:
                matched_categories[category] = matches
        
        # Determine primary category
        if matched_categories:
            primary_category = max(matched_categories, key=matched_categories.get)
            confidence = min(matched_categories[primary_category] / 3.0, 1.0)
        else:
            primary_category = TaskCategory.UNKNOWN
            confidence = 0.3
        
        characteristics = TaskCharacteristics(
            category=primary_category,
            complexity=self._estimate_complexity(task),
            context_required=self._estimate_context(task),
            retrieval_required=primary_category in [
                TaskCategory.RETRIEVAL_COMPLEX, TaskCategory.SYNTHESIS,
                TaskCategory.ANALYSIS_COMPLEX, TaskCategory.EXPLANATION,
                TaskCategory.DIAGNOSIS
            ],
            verification_level=self._estimate_verification_level(task, primary_category),
            safety_critical=any(p.search(task) for p in self._safety_patterns),
            latency_tolerance=self._estimate_latency_tolerance(task),
            classification_confidence=confidence
        )
        
        return characteristics
    
    def _estimate_complexity(self, task: str) -> ComplexityLevel:
        """Estimate task complexity based on keywords."""
        base = ComplexityLevel.MEDIUM
        
        # Check for complexity modifiers
        increasers = sum(1 for p in self._complexity_increasers if p.search(task))
        decreasers = sum(1 for p in self._complexity_decreasers if p.search(task))
        
        adjustments = increasers - decreasers
        
        new_level = base.value + adjustments
        new_level = max(1, min(5, new_level))
        
        return ComplexityLevel(new_level)
    
    def _estimate_context(self, task: str) -> int:
        """Estimate context window requirements."""
        # Simple heuristic based on task length and complexity
        base_tokens = len(task.split()) * 10  # Approximate
        
        # Add overhead based on keywords
        if any(p.search(task) for p in self._complexity_increasers):
            base_tokens *= 2
        if any(p.search(task) for p in self._complexity_decreasers):
            base_tokens = max(1000, base_tokens // 2)
        
        return min(base_tokens, 128000)  # Cap at max context
    
    def _estimate_verification_level(self, task: str, category: TaskCategory) -> int:
        """Estimate required verification level."""
        if category == TaskCategory.VALIDATION_CRITICAL:
            return 5
        if category == TaskCategory.VALIDATION_SAFETY:
            return 4
        if category == TaskCategory.VALIDATION_STANDARD:
            return 2
        
        # Check for verification keywords
        verify_keywords = ['verify', 'validate', 'check', 'confirm', 'proof']
        if any(k in task.lower() for k in verify_keywords):
            return 2
        
        return 1
    
    def _estimate_latency_tolerance(self, task: str) -> str:
        """Estimate acceptable latency."""
        task_lower = task.lower()
        
        if any(k in task_lower for k in ['instant', 'quick', 'fast', 'immediate']):
            return 'instant'
        if any(k in task_lower for k in ['slow', 'patient', 'deep', 'thorough']):
            return 'patient'
        
        return 'moderate'
    
    def batch_classify(self, tasks: List[str]) -> List[TaskCharacteristics]:
        """Classify multiple tasks."""
        return [self.classify(task) for task in tasks]
