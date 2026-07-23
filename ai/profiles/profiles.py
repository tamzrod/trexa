"""
Reasoning Profile Registry

Defines the 7 reasoning profiles for adaptive AI routing.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


class ReasoningProfile(Enum):
    """Enumeration of available reasoning profiles."""
    FAST = "fast"
    BALANCED = "balanced"
    DEEP = "deep"
    VERIFICATION = "verification"
    CREATIVE = "creative"
    HYBRID_IR = "hybrid_ir"
    DIAGNOSTIC = "diagnostic"


@dataclass
class ProfileConfig:
    """Configuration for a reasoning profile."""
    
    name: str
    depth: int  # Reasoning depth (1-10+)
    context_window: int  # Max tokens
    retrieval: bool  # Whether retrieval is used
    verification_level: int  # 0=none, 5=exhaustive
    latency_tier: str  # instant, fast, moderate, patient, async
    cost_tier: int  # 1=minimal, 5=premium
    confidence_output: bool  # Whether confidence is reported
    citations_required: bool  # Whether citations are required
    
    # Capability flags
    supports_multimodal: bool = False
    supports_streaming: bool = True
    supports_tools: bool = False
    supports_citations: bool = False
    
    # Matching keywords for automatic detection
    keywords: List[str] = field(default_factory=list)
    
    # Task categories this profile handles
    task_categories: List[str] = field(default_factory=list)
    
    # Constraints
    min_latency_ms: int = 0
    max_latency_ms: int = 30000
    
    @property
    def relative_cost(self) -> float:
        """Cost relative to FAST profile."""
        return [1.0, 2.5, 7.5, 4.0, 6.0, 4.5, 6.0][
            [p.name for p in ReasoningProfile].index(self.name.upper())
        ] if hasattr(self, 'name') else 1.0


# Profile Definitions
PROFILES: Dict[ReasoningProfile, ProfileConfig] = {
    ReasoningProfile.FAST: ProfileConfig(
        name="FAST",
        depth=1,
        context_window=8000,
        retrieval=False,
        verification_level=0,
        latency_tier="instant",
        cost_tier=1,
        confidence_output=False,
        citations_required=False,
        supports_streaming=True,
        keywords=["what is", "color", "standard", "code", "define", "lookup", "retrieve"],
        task_categories=["retrieval_simple", "generation_simple"],
        min_latency_ms=0,
        max_latency_ms=1000
    ),
    
    ReasoningProfile.BALANCED: ProfileConfig(
        name="BALANCED",
        depth=3,
        context_window=32000,
        retrieval=False,
        verification_level=1,
        latency_tier="moderate",
        cost_tier=2,
        confidence_output=True,
        citations_required=False,
        supports_streaming=True,
        keywords=["validate", "check", "generate", "create", "analyze", "explain"],
        task_categories=["validation_standard", "generation_standard", "explanation"],
        min_latency_ms=1000,
        max_latency_ms=5000
    ),
    
    ReasoningProfile.DEEP: ProfileConfig(
        name="DEEP",
        depth=10,
        context_window=128000,
        retrieval=True,
        verification_level=3,
        latency_tier="patient",
        cost_tier=4,
        confidence_output=True,
        citations_required=True,
        supports_streaming=True,
        supports_citations=True,
        keywords=["analyze", "assess", "evaluate", "synthesize", "research", "investigate"],
        task_categories=["analysis_complex", "synthesis", "planning_complex"],
        min_latency_ms=10000,
        max_latency_ms=30000
    ),
    
    ReasoningProfile.VERIFICATION: ProfileConfig(
        name="VERIFICATION",
        depth=5,
        context_window=64000,
        retrieval=True,
        verification_level=5,
        latency_tier="moderate",
        cost_tier=3,
        confidence_output=True,
        citations_required=True,
        supports_streaming=True,
        supports_citations=True,
        keywords=["verify", "compliance", "audit", "validate_safety", "proof", "certify"],
        task_categories=["validation_safety", "validation_critical"],
        min_latency_ms=5000,
        max_latency_ms=15000
    ),
    
    ReasoningProfile.CREATIVE: ProfileConfig(
        name="CREATIVE",
        depth=7,
        context_window=128000,
        retrieval=True,
        verification_level=1,
        latency_tier="patient",
        cost_tier=4,
        confidence_output=True,
        citations_required=False,
        supports_streaming=True,
        keywords=["design", "suggest", "alternative", "innovate", "create_novel", "brainstorm"],
        task_categories=["generation_creative", "planning_creative"],
        min_latency_ms=10000,
        max_latency_ms=30000
    ),
    
    ReasoningProfile.HYBRID_IR: ProfileConfig(
        name="HYBRID_IR",
        depth=5,
        context_window=128000,
        retrieval=True,
        verification_level=2,
        latency_tier="moderate",
        cost_tier=3,
        confidence_output=True,
        citations_required=True,
        supports_streaming=True,
        supports_citations=True,
        supports_tools=True,
        keywords=["explain", "why", "because", "grounded", "cited", "source"],
        task_categories=["explanation", "retrieval_complex", "analysis_grounded"],
        min_latency_ms=5000,
        max_latency_ms=20000
    ),
    
    ReasoningProfile.DIAGNOSTIC: ProfileConfig(
        name="DIAGNOSTIC",
        depth=10,
        context_window=128000,
        retrieval=True,
        verification_level=4,
        latency_tier="patient",
        cost_tier=4,
        confidence_output=True,
        citations_required=True,
        supports_streaming=True,
        supports_citations=True,
        keywords=["debug", "diagnose", "why_failed", "investigate", "troubleshoot", "root_cause"],
        task_categories=["debugging", "diagnosis"],
        min_latency_ms=10000,
        max_latency_ms=45000
    ),
}


def get_profile(name: str) -> ProfileConfig:
    """Get profile configuration by name."""
    try:
        profile = ReasoningProfile(name.lower())
        return PROFILES[profile]
    except ValueError:
        raise ValueError(f"Unknown profile: {name}")


def get_all_profiles() -> Dict[ReasoningProfile, ProfileConfig]:
    """Get all profile configurations."""
    return PROFILES.copy()


def get_profiles_for_category(category: str) -> List[ProfileConfig]:
    """Get all profiles that handle a given task category."""
    matching = []
    for profile in PROFILES.values():
        if category in profile.task_categories:
            matching.append(profile)
    return matching if matching else [PROFILES[ReasoningProfile.BALANCED]]


def get_fastest_profile() -> ProfileConfig:
    """Get the fastest (lowest latency) profile."""
    return PROFILES[ReasoningProfile.FAST]


def get_cheapest_profile() -> ProfileConfig:
    """Get the cheapest profile."""
    return PROFILES[ReasoningProfile.FAST]


def get_highest_quality_profile() -> ProfileConfig:
    """Get the profile with highest reasoning depth."""
    return max(PROFILES.values(), key=lambda p: p.depth)
