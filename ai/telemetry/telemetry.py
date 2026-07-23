"""
Telemetry System

Tracks decision logs, latency, cost, quality, and user overrides.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List, Callable
from datetime import datetime, timedelta
from enum import Enum
import threading
import json


class QualityRating(Enum):
    """Quality rating for responses."""
    EXCELLENT = 5
    GOOD = 4
    ADEQUATE = 3
    POOR = 2
    FAILED = 1


@dataclass
class DecisionLogEntry:
    """A single decision log entry."""
    timestamp: datetime
    task_id: str
    user_id: Optional[str]
    session_id: Optional[str]
    
    # Task info
    task_prompt: str
    task_category: str
    task_complexity: str
    
    # Selection info
    profile_selected: str
    selection_confidence: float
    selection_strategy: str
    
    # Execution info
    latency_ms: float
    cost_estimate: float
    ir_contexts_used: int
    
    # Quality info
    quality_rating: Optional[QualityRating] = None
    user_feedback: Optional[str] = None
    
    # Override info
    was_overridden: bool = False
    override_reason: Optional[str] = None
    
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def cost_per_second(self) -> float:
        """Calculate cost per second."""
        if self.latency_ms > 0:
            return self.cost_estimate / (self.latency_ms / 1000)
        return 0.0


@dataclass
class TelemetryStats:
    """Aggregated statistics."""
    total_requests: int
    avg_latency_ms: float
    avg_cost: float
    total_cost: float
    profile_distribution: Dict[str, int]
    category_distribution: Dict[str, int]
    quality_distribution: Dict[str, int]
    p95_latency_ms: float
    p99_latency_ms: float
    
    override_rate: float
    error_rate: float


class UserOverride:
    """Records user overrides to selection."""
    
    def __init__(
        self,
        task_pattern: str,
        preferred_profile: str,
        reason: str,
        created_by: str,
        expires: Optional[datetime] = None
    ):
        self.task_pattern = task_pattern
        self.preferred_profile = preferred_profile
        self.reason = reason
        self.created_by = created_by
        self.created_at = datetime.utcnow()
        self.expires = expires
        self.usage_count = 0
    
    def matches(self, task_prompt: str) -> bool:
        """Check if this override matches the task."""
        if self.expires and datetime.utcnow() > self.expires:
            return False
        return self.task_pattern.lower() in task_prompt.lower()
    
    def use(self):
        """Record that this override was used."""
        self.usage_count += 1


class Telemetry:
    """
    Telemetry system for tracking routing decisions.
    
    Tracks:
    - Decision logs
    - Latency metrics
    - Cost metrics
    - Quality ratings
    - User overrides
    """
    
    def __init__(
        self,
        max_entries: int = 10000,
        aggregation_window: timedelta = timedelta(hours=1)
    ):
        self._entries: List[DecisionLogEntry] = []
        self._max_entries = max_entries
        self._aggregation_window = aggregation_window
        self._overrides: List[UserOverride] = []
        self._lock = threading.Lock()
        
        # Callbacks
        self._on_decision: Optional[Callable] = None
        self._on_quality_update: Optional[Callable] = None
    
    def log_decision(
        self,
        request: Any,
        characteristics: Any,
        profile_selected: Any,
        result: Any
    ):
        """
        Log a routing decision.
        
        Args:
            request: TaskRequest that was processed
            characteristics: TaskCharacteristics from classification
            profile_selected: ProfileConfig that was selected
            result: ExecutionResult from execution
        """
        entry = DecisionLogEntry(
            timestamp=datetime.utcnow(),
            task_id=request.task_id,
            user_id=request.user_id,
            session_id=request.session_id,
            task_prompt=request.prompt[:500],  # Truncate for storage
            task_category=characteristics.category.value,
            task_complexity=characteristics.complexity.name,
            profile_selected=profile_selected.name,
            selection_confidence=characteristics.classification_confidence,
            selection_strategy="weighted",
            latency_ms=result.latency_ms,
            cost_estimate=result.cost_estimate,
            ir_contexts_used=len(result.ir_contexts),
            was_overridden=False,
            metadata=result.metadata
        )
        
        # Check for active overrides
        for override in self._overrides:
            if override.matches(request.prompt):
                entry.was_overridden = True
                entry.override_reason = f"Matched override: {override.task_pattern}"
                override.use()
                break
        
        with self._lock:
            self._entries.append(entry)
            
            # Trim if needed
            if len(self._entries) > self._max_entries:
                self._entries = self._entries[-self._max_entries:]
        
        # Notify callback
        if self._on_decision:
            self._on_decision(entry)
    
    def rate_quality(
        self,
        task_id: str,
        rating: QualityRating,
        feedback: Optional[str] = None
    ):
        """
        Record quality rating for a task.
        
        Args:
            task_id: ID of the task
            rating: QualityRating enum value
            feedback: Optional user feedback text
        """
        with self._lock:
            for entry in reversed(self._entries):
                if entry.task_id == task_id:
                    entry.quality_rating = rating
                    entry.user_feedback = feedback
                    break
        
        if self._on_quality_update:
            self._on_quality_update(task_id, rating, feedback)
    
    def add_override(
        self,
        task_pattern: str,
        preferred_profile: str,
        reason: str,
        created_by: str,
        expires: Optional[datetime] = None
    ) -> UserOverride:
        """
        Add a user override for profile selection.
        
        Args:
            task_pattern: Pattern to match against prompts
            preferred_profile: Profile to select when matched
            reason: Reason for the override
            created_by: User who created the override
            expires: Optional expiration time
            
        Returns:
            Created UserOverride
        """
        override = UserOverride(
            task_pattern=task_pattern,
            preferred_profile=preferred_profile,
            reason=reason,
            created_by=created_by,
            expires=expires
        )
        
        with self._lock:
            self._overrides.append(override)
        
        return override
    
    def remove_override(self, task_pattern: str) -> bool:
        """Remove override by pattern."""
        with self._lock:
            before = len(self._overrides)
            self._overrides = [
                o for o in self._overrides
                if o.task_pattern != task_pattern
            ]
            return len(self._overrides) < before
    
    def get_stats(
        self,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None
    ) -> TelemetryStats:
        """
        Get aggregated statistics.
        
        Args:
            since: Start of time window
            until: End of time window
            
        Returns:
            TelemetryStats with aggregated data
        """
        with self._lock:
            entries = self._entries
            
            if since:
                entries = [e for e in entries if e.timestamp >= since]
            if until:
                entries = [e for e in entries if e.timestamp <= until]
        
        if not entries:
            return TelemetryStats(
                total_requests=0,
                avg_latency_ms=0,
                avg_cost=0,
                total_cost=0,
                profile_distribution={},
                category_distribution={},
                quality_distribution={},
                p95_latency_ms=0,
                p99_latency_ms=0,
                override_rate=0,
                error_rate=0
            )
        
        # Calculate distributions
        profile_dist: Dict[str, int] = {}
        category_dist: Dict[str, int] = {}
        quality_dist: Dict[str, int] = {}
        
        for entry in entries:
            profile_dist[entry.profile_selected] = \
                profile_dist.get(entry.profile_selected, 0) + 1
            category_dist[entry.task_category] = \
                category_dist.get(entry.task_category, 0) + 1
            if entry.quality_rating:
                key = entry.quality_rating.name
                quality_dist[key] = quality_dist.get(key, 0) + 1
        
        # Calculate latency percentiles
        latencies = sorted(e.latency_ms for e in entries)
        p95_idx = int(len(latencies) * 0.95)
        p99_idx = int(len(latencies) * 0.99)
        
        # Calculate rates
        override_count = sum(1 for e in entries if e.was_overridden)
        failed_count = sum(
            1 for e in entries
            if e.quality_rating == QualityRating.FAILED
        )
        
        return TelemetryStats(
            total_requests=len(entries),
            avg_latency_ms=sum(e.latency_ms for e in entries) / len(entries),
            avg_cost=sum(e.cost_estimate for e in entries) / len(entries),
            total_cost=sum(e.cost_estimate for e in entries),
            profile_distribution=profile_dist,
            category_distribution=category_dist,
            quality_distribution=quality_dist,
            p95_latency_ms=latencies[p95_idx] if latencies else 0,
            p99_latency_ms=latencies[p99_idx] if latencies else 0,
            override_rate=override_count / len(entries),
            error_rate=failed_count / len(entries)
        )
    
    def get_recent_entries(
        self,
        limit: int = 100,
        offset: int = 0
    ) -> List[DecisionLogEntry]:
        """Get recent decision log entries."""
        with self._lock:
            start = max(0, len(self._entries) - limit - offset)
            end = len(self._entries) - offset
            return self._entries[start:end]
    
    def get_overrides(self) -> List[UserOverride]:
        """Get all active overrides."""
        with self._lock:
            return [
                o for o in self._overrides
                if not o.expires or o.expires > datetime.utcnow()
            ]
    
    def export_logs(
        self,
        format: str = "json",
        since: Optional[datetime] = None
    ) -> str:
        """
        Export logs in specified format.
        
        Args:
            format: Export format (json, csv)
            since: Only export entries since this time
            
        Returns:
            Exported data as string
        """
        entries = self.get_recent_entries(limit=self._max_entries)
        
        if since:
            entries = [e for e in entries if e.timestamp >= since]
        
        if format == "json":
            return json.dumps([
                {
                    "timestamp": e.timestamp.isoformat(),
                    "task_id": e.task_id,
                    "category": e.task_category,
                    "profile": e.profile_selected,
                    "latency_ms": e.latency_ms,
                    "cost": e.cost_estimate,
                    "confidence": e.selection_confidence,
                    "quality": e.quality_rating.name if e.quality_rating else None
                }
                for e in entries
            ], indent=2)
        
        # CSV format
        lines = ["timestamp,task_id,category,profile,latency_ms,cost,confidence,quality"]
        for e in entries:
            lines.append(
                f"{e.timestamp.isoformat()},"
                f"{e.task_id},"
                f"{e.task_category},"
                f"{e.profile_selected},"
                f"{e.latency_ms:.2f},"
                f"{e.cost_estimate:.6f},"
                f"{e.selection_confidence:.2f},"
                f"{e.quality_rating.name if e.quality_rating else ''}"
            )
        
        return "\n".join(lines)
    
    def set_callbacks(
        self,
        on_decision: Optional[Callable] = None,
        on_quality_update: Optional[Callable] = None
    ):
        """Set callback functions for async notifications."""
        self._on_decision = on_decision
        self._on_quality_update = on_quality_update
