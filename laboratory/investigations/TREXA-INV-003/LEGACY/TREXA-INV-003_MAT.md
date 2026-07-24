# Engine Selection Criteria and Decision Matrix: TREXA-INV-003

**Investigation**: TREXA-INV-003
**Title**: AI Engine Selection and Reasoning Strategy
**Date**: 2026-07-23T09:00:00Z
**Status**: COMPLETE

---

## Engine Selection Criteria

### Primary Criteria

#### CRITERIA-001: Task Category Match
**Definition**: How well does the profile match the task category?
**Evaluation**:
- EXACT (5): Profile designed for this exact task type
- HIGH (4): Profile supports this task type well
- MEDIUM (3): Profile can handle with reduced capability
- LOW (2): Profile勉强 supports this type
- POOR (1): Profile not suitable for this type

#### CRITERIA-002: Reasoning Depth Required
**Definition**: How many reasoning steps are needed?
**Evaluation**:
- SINGLE (1): Single lookup or simple rule
- FEW (2-3): Few steps, linear
- MODERATE (4-7): Several steps, some branching
- DEEP (8-15): Many steps, complex branching
- EXTENSIVE (15+): Extensive exploration needed

#### CRITERIA-003: Context Requirements
**Definition**: How much context is needed?
**Evaluation**:
- MINIMAL (<2K): Single entity
- LOW (2-8K): Simple object or rule
- MODERATE (8-32K): Multiple objects, standard diagram
- HIGH (32-128K): Large diagram, complex relationships
- EXTENSIVE (>128K): Full system, multi-diagram

#### CRITERIA-004: Retrieval Requirements
**Definition**: How much external knowledge retrieval is needed?
**Evaluation**:
- NONE: Task is self-contained
- OPTIONAL: Retrieval helpful but not required
- HELPFUL: Retrieval improves quality
- REQUIRED: Task impossible without retrieval
- CRITICAL: Retrieval is the primary task

#### CRITERIA-005: Verification Requirements
**Definition**: How thorough must verification be?
**Evaluation**:
- NONE: No verification needed
- LIGHT: Spot-check sufficient
- MODERATE: Standard verification
- THOROUGH: Comprehensive verification
- EXHAUSTIVE: Proof-like verification required

#### CRITERIA-006: Latency Tolerance
**Definition**: How much time can the user wait?
**Evaluation**:
- INSTANT (<1s): Interactive editing
- FAST (1-3s): Responsive workflow
- MODERATE (3-10s): Background acceptable
- PATIENT (10-30s): Research mode acceptable
- ASYNC (>30s): Batch processing fine

#### CRITERIA-007: Cost Constraints
**Definition**: How cost-sensitive is this task?
**Evaluation**:
- CRITICAL: Must use cheapest option
- IMPORTANT: Prefer lower cost
- NEUTRAL: Cost-quality trade-off acceptable
- FLEXIBLE: Quality over cost
- IGNORE: Cost not a factor

---

## Decision Matrix

### Task-to-Profile Mapping

| Task Type | Primary Profile | Score | Alt Profile 1 | Score | Alt Profile 2 | Score |
|-----------|---------------|-------|---------------|-------|---------------|-------|
| **Retrieval (simple)** | FAST | 25 | BALANCED | 18 | - | - |
| **Retrieval (complex)** | HYBRID IR+R | 23 | DEEP RESEARCH | 20 | BALANCED | 15 |
| **Validation (standard)** | BALANCED | 22 | VERIFICATION | 20 | FAST | 14 |
| **Validation (safety)** | VERIFICATION | 25 | BALANCED | 17 | - | - |
| **Generation (simple)** | FAST | 20 | BALANCED | 18 | - | - |
| **Generation (standard)** | BALANCED | 22 | HYBRID IR+R | 19 | CREATIVE | 16 |
| **Generation (novel)** | CREATIVE | 23 | DEEP RESEARCH | 20 | HYBRID IR+R | 17 |
| **Analysis (standard)** | DEEP RESEARCH | 24 | HYBRID IR+R | 21 | BALANCED | 15 |
| **Synthesis** | DEEP RESEARCH | 25 | CREATIVE | 22 | HYBRID IR+R | 20 |
| **Explanation** | HYBRID IR+R | 24 | BALANCED | 18 | - | - |
| **Planning (simple)** | BALANCED | 20 | CREATIVE | 18 | - | - |
| **Planning (complex)** | DEEP RESEARCH | 23 | CREATIVE | 21 | - | - |
| **Debugging** | DIAGNOSTIC | 25 | DEEP RESEARCH | 19 | BALANCED | 14 |

**Score Calculation**: Weighted sum of criteria scores (see weights below)

---

### Scoring Weights

| Criteria | Weight | Rationale |
|---------|--------|------------|
| Task Category Match | 0.25 | Primary selection factor |
| Reasoning Depth | 0.20 | Determines capability fit |
| Context Requirements | 0.15 | Determines feasibility |
| Retrieval Requirements | 0.15 | Affects quality |
| Verification | 0.10 | Affects reliability |
| Latency Tolerance | 0.10 | Affects UX |
| Cost Constraints | 0.05 | Business factor |

---

## Routing Strategy

### Strategy 1: Direct Mapping (Simple)

For clearly classified tasks:

```
IF task.type == "retrieval_simple" THEN select(FAST)
IF task.type == "validation_safety" THEN select(VERIFICATION)
IF task.type == "analysis_complex" THEN select(DEEP_RESEARCH)
```

**When to Use**: User explicitly selects task type
**Advantages**: Fast, predictable
**Disadvantages**: Requires explicit classification

---

### Strategy 2: Automatic Classification

For implicit task detection:

```
1. Analyze task description for keywords
2. Evaluate complexity heuristics
3. Check context requirements
4. Apply classification model
5. Select profile based on classification
```

**Keyword Heuristics**:
| Keyword Pattern | Suggested Profile |
|----------------|-------------------|
| "what is", "color", "standard" | FAST |
| "validate", "check", "verify" | BALANCED or VERIFICATION |
| "analyze", "assess", "evaluate" | DEEP RESEARCH |
| "explain", "why", "because" | HYBRID IR+R |
| "design", "suggest", "alternative" | CREATIVE |
| "debug", "why failed", "diagnose" | DIAGNOSTIC |

**When to Use**: User provides natural language request
**Advantages**: Flexible, natural
**Disadvantages**: Classification may be imperfect

---

### Strategy 3: Cascade Selection

For uncertain classification:

```
1. Start with FAST
2. IF FAST output confidence < threshold THEN escalate to BALANCED
3. IF BALANCED output confidence < threshold THEN escalate to DEEP RESEARCH
4. Continue until satisfactory output or max depth
```

**When to Use**: Unknown complexity, budget constraints
**Advantages**: Cost-efficient, always produces output
**Disadvantages**: May be slow for complex tasks

**Parameters**:
- Confidence threshold: 0.7
- Max cascade depth: 3 levels
- Escalation timeout: 30s total

---

### Strategy 4: Parallel Evaluation

For high-stakes decisions:

```
1. Execute FAST and BALANCED in parallel
2. Compare outputs for consistency
3. IF inconsistent THEN escalate to DEEP RESEARCH
4. Return highest-quality consistent output
```

**When to Use**: Safety-critical validation, important decisions
**Advantages**: High confidence, catches errors
**Disadvantages**: 2-3x cost

---

### Strategy 5: Context-Aware Selection

For session-based optimization:

```
1. Track task history in session
2. Build user/task profile
3. Adjust selection based on learned patterns
4. Apply domain-specific overrides
```

**Session Variables**:
- User expertise level
- Task complexity distribution
- Preferred latency/quality trade-off
- Domain context

**When to Use**: Personalized experience, long sessions
**Advantages**: Optimized for user
**Disadvantages**: Complexity, cold-start issues

---

## Composite Selection Algorithm

```python
def select_profile(task, context):
    # Step 1: Get explicit preferences
    explicit = context.get('profile_preference', None)
    if explicit:
        return explicit
    
    # Step 2: Analyze task characteristics
    characteristics = analyze_task(task)
    
    # Step 3: Apply heuristics
    keyword_profile = keyword_match(task.description)
    
    # Step 4: Score all profiles
    scores = {}
    for profile in PROFILES:
        scores[profile] = score_profile(profile, characteristics)
    
    # Step 5: Apply constraints
    constrained = apply_constraints(scores, context)
    
    # Step 6: Select best
    return max(constrained, key=constrained.get)
```

---

## Fallback Strategy

### Primary Engine Failure

```
1. IF primary fails THEN retry with same profile
2. IF retry fails THEN retry with simpler profile
3. IF simpler fails THEN retry with backup provider
4. IF all fail THEN return error with partial results
```

### Timeout Handling

```
1. IF timeout THEN return partial results
2. IF partial quality < threshold THEN flag for user review
3. IF user requests completion THEN escalate profile
```

---

## Selection Criteria Summary

| Criteria | Weight | Type |
|---------|--------|------|
| Task Category Match | 0.25 | Quality |
| Reasoning Depth | 0.20 | Quality |
| Context Requirements | 0.15 | Feasibility |
| Retrieval Requirements | 0.15 | Quality |
| Verification | 0.10 | Reliability |
| Latency Tolerance | 0.10 | UX |
| Cost Constraints | 0.05 | Business |

---

**Decision Matrix Status**: COMPLETE
**Routing Strategies Defined**: 5
**Selection Algorithm**: Defined

**Next**: Benefits and Risks Analysis
