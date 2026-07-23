"""
Trexa AI Module

Adaptive AI routing system for engineering tasks.

Phases:
- Phase 1: Profile Registry (profiles/)
- Phase 2: Task Classifier (classifier/)
- Phase 3: Hybrid IR (ir/)
- Phase 4: Routing Engine (routing/)
- Phase 5: Telemetry (telemetry/)
"""

from .profiles.profiles import (
    ReasoningProfile,
    ProfileConfig,
    PROFILES,
    get_profile,
    get_all_profiles,
    get_profiles_for_category,
    get_fastest_profile,
    get_cheapest_profile,
    get_highest_quality_profile
)

from .classifier.classifier import (
    TaskClassifier,
    TaskCharacteristics,
    TaskCategory,
    ComplexityLevel
)

from .routing.engine import (
    RoutingEngine,
    ProfileSelector,
    TaskRequest,
    ExecutionResult,
    SelectionStrategy,
    SelectionCriteria,
    create_routing_engine
)

from .telemetry.telemetry import (
    Telemetry,
    TelemetryStats,
    DecisionLogEntry,
    UserOverride,
    QualityRating
)

__version__ = "0.1.0"

__all__ = [
    # Profiles
    "ReasoningProfile",
    "ProfileConfig",
    "PROFILES",
    "get_profile",
    "get_all_profiles",
    "get_profiles_for_category",
    "get_fastest_profile",
    "get_cheapest_profile",
    "get_highest_quality_profile",
    # Classifier
    "TaskClassifier",
    "TaskCharacteristics",
    "TaskCategory",
    "ComplexityLevel",
    # Routing
    "RoutingEngine",
    "ProfileSelector",
    "TaskRequest",
    "ExecutionResult",
    "SelectionStrategy",
    "SelectionCriteria",
    "create_routing_engine",
    # Telemetry
    "Telemetry",
    "TelemetryStats",
    "DecisionLogEntry",
    "UserOverride",
    "QualityRating"
]
