# TREXA-INV-017: Knowledge Evolution & Repository Simplification Investigation

**ID**: TREXA-INV-017
**Title**: Knowledge Evolution & Repository Simplification Investigation
**Type**: Investigation
**Status**: COMPLETE
**Date**: 2026-07-24
**Author**: OpenHands Agent

---

## Precondition Verification

| Component | Status | Evidence |
|-----------|--------|----------|
| KDE Bootstrap | ✅ VERIFIED | config.yaml v1.0.0, bootstrap_date: 2026-07-24 |
| KDE Runtime | ✅ VERIFIED | state.json: "initialized", "ready", 9 modules loaded |

---

# 1. Executive Summary

## 1.1 Current State

| Metric | Value |
|--------|-------|
| Investigations | 16 (INV-001 to INV-016, INV-009 missing) |
| Experiments | 4 (EXP-001 to EXP-004) |
| Decisions | 3 (TDR-001 to TDR-003) |
| Methodology | 1 (AI-FIRST-METHODOLOGY.md) |
| Reviews | 1 (TREXA-REV-001.md) |
| Governance Documents | 1 (NAMING-CONVENTIONS.md) |

## 1.2 Problem Statement

No formal lifecycle exists governing how knowledge artifacts should evolve, merge, archive, or be removed.

## 1.3 Recommendation

**Establish a formal Knowledge Artifact Lifecycle Policy** with:
- 8 lifecycle states
- Clear transition criteria
- Preservation requirements for knowledge extraction
- Governance authority for state changes

---

# 2. Knowledge Lifecycle Assessment

## 2.1 Lifecycle States Analysis

### State Definitions

| State | Definition | Evidence | Retention |
|-------|------------|----------|-----------|
| **Draft** | Initial creation, not reviewed | New investigations start here | Short-term only |
| **Active** | Approved, current guidance | TDR-001, TDR-002, TDR-003 | Indefinite while valid |
| **Revision Required** | Valuable but needs update | AI-FIRST-METHODOLOGY (INV-016) | Until revised |
| **Merged** | Combined into another artifact | Not yet applied | Historical reference |
| **Superseded** | Replaced by newer knowledge | Not yet applied | Historical reference |
| **Historical** | Preserved for context | LEGACY/ directories | Indefinite |
| **Archived** | No longer referenced | Not yet applied | Long-term optional |
| **Removed** | Deleted from repository | Not yet applied | Git history only |

## 2.2 Lifecycle State Transitions

```
                    ┌─────────────────────────────────────────┐
                    │                                         │
                    ▼                                         │
┌─────────┐    ┌─────────┐    ┌──────────────────┐          │
│  DRAFT  │───▶│ ACTIVE  │───▶│ REVISION REQUIRED │          │
└─────────┘    └─────────┘    └────────┬─────────┘          │
     │              │                    │                    │
     │              │                    ▼                    │
     │              │           ┌──────────────────┐          │
     │              │           │     MERGED       │          │
     │              │           └────────┬─────────┘          │
     │              │                    │                    │
     │              ▼                    ▼                    │
     │       ┌──────────┐          ┌────────────┐            │
     │       │SUPERSEDED│◀─────────│ HISTORICAL │            │
     │       └────┬─────┘          └──────┬─────┘            │
     │            │                       │                    │
     │            ▼                       ▼                    │
     │      ┌──────────┐           ┌──────────┐             │
     │      │ ARCHIVED │           │ REMOVED  │             │
     │      └──────────┘           └──────────┘             │
     │                                                   │
     └───────────────────────────────────────────────────┘
                          (Rejection path from Draft)
```

## 2.3 Transition Criteria

| Current State | Target State | Trigger Criteria |
|--------------|-------------|------------------|
| Draft → Active | Human approval granted | Investigation complete, reviewed |
| Draft → Removed | Rejected | No value identified |
| Active → Revision Required | New evidence contradicts or extends | New investigation finding |
| Active → Superseded | Newer artifact replaces | New TDR or investigation |
| Active → Merged | Consolidate related artifacts | Multiple artifacts cover same topic |
| Revision Required → Active | Update completed | Human approval of revision |
| Revision Required → Merged | Revision becomes consolidation | Extract knowledge, retire |
| Superseded → Archived | Historical value only | No future reference expected |
| Superseded → Removed | No historical value | Evidence demonstrates obsolescence |
| Historical → Archived | Never referenced | No active use in 6+ months |
| Archived → Removed | Repository cleanup | Explicit removal decision |

---

# 3. Complexity vs Knowledge Analysis

## 3.1 Trade-off Matrix

| Scenario | Complexity | Knowledge | Recommendation |
|----------|-----------|----------|----------------|
| Valuable + Unique | +1 | +1 | **Retain** |
| Valuable + Duplicated | +1 | 0 | **Merge** |
| Outdated + Unique | +1 | 0 | **Archive** |
| Outdated + Duplicated | +1 | -1 | **Remove** |
| Obsolete + Confusing | +1 | -2 | **Remove** |

## 3.2 Complexity Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Total investigations | >50 | Review consolidation opportunities |
| Investigation size | >100KB | Split or extract key findings |
| Duplicate concepts | >3 artifacts | Merge into single source |
| Missing cross-references | >20% | Add linking |
| Outdated artifacts | >25% of total | Archive campaign |

## 3.3 Knowledge Value Assessment

| Value Dimension | Assessment Method | Weight |
|----------------|------------------|--------|
| Current applicability | Is artifact referenced? | 30% |
| Unique knowledge | Cannot be derived from other artifacts? | 30% |
| Engineering guidance | Provides actionable direction? | 20% |
| Historical context | Explains evolution? | 10% |
| Maintenance burden | Requires updates? | 10% |

---

# 4. Repository Simplification Strategy

## 4.1 Three Pillars

| Pillar | Description | Priority |
|--------|-------------|----------|
| **Knowledge Preservation** | Extract unique knowledge before removal | HIGH |
| **Repository Clarity** | Remove confusing artifacts | MEDIUM |
| **Engineering Guidance** | Maintain actionable current state | HIGH |

## 4.2 Simplification Principles

| Principle | Implementation |
|-----------|---------------|
| Extract Before Remove | Always extract unique knowledge first |
| Merge Before Delete | Consolidate duplicates rather than delete |
| Archive Before Remove | Preserve historical context when in doubt |
| Reference Before Remove | Ensure no active dependencies |
| Authorize Before Remove | Require human approval for removal |

## 4.3 Simplification Triggers

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Investigation accumulation | 50+ investigations | Lifecycle review |
| Duplicate artifacts | 3+ covering same topic | Merge investigation |
| Outdated percentage | >25% outdated | Archive campaign |
| Cross-reference breakage | Dependencies violated | Resolution investigation |

---

# 5. Artifact Evolution Model

## 5.1 Evolution Types

| Type | Description | Example |
|------|-------------|---------|
| **Growth** | New artifact created | INV-017 from investigation |
| **Refinement** | Artifact improved, same scope | INV-016 revision of AI-FIRST-METHODOLOGY |
| **Split** | One artifact becomes multiple | Not yet observed |
| **Merge** | Multiple artifacts become one | Potential for INV-013/014/015 |
| **Promotion** | Artifact becomes governance | Naming conventions from practice |
| **Demotion** | Governance becomes guidance | Future methodology evolution |
| **Archive** | Artifact preserved, not maintained | LEGACY/ directories |
| **Removal** | Artifact deleted | Future cleanup |

## 5.2 Evolution Decision Tree

```
Artifact under consideration
    │
    ▼
┌─────────────────────────────────────────┐
│ Is artifact actively referenced?         │
│                                         │
│ NO ──────────────────────────────▶  2   │
│ YES                                    │
│    │                                   │
│    ▼                                   │
│ 1. Does artifact contain unique         │
│    knowledge not in newer artifacts?    │
│                                         │
│ NO ──────────────────────────────▶  3   │
│ YES                                   │
│    │                                   │
│    ▼                                   │
│ Does artifact create confusion?           │
│                                         │
│ NO ──────────────────────────────▶ KEEP  │
│ YES ────────────────────────────▶ MERGE │
└─────────────────────────────────────────┘
    │
    │  2. Does artifact have historical   │
    │     value for understanding          │
    │     repository evolution?           │
    │                                         │
    │ NO ────────────────────────────▶ REMOVE │
    │ YES ──────────────────────────▶ ARCHIVE │
    │
    │  3. Can knowledge be extracted      │
    │     into newer artifacts?           │
    │                                         │
    │ NO ────────────────────────────▶ REMOVE │
    │ YES ──────────────────────────▶ EXTRACT │
    │     → Then evaluate remaining         │
    └─────────────────────────────────────────┘
```

## 5.3 Evolution Authority

| Action | Authority Required |
|--------|-------------------|
| Draft → Active | Human approval |
| Active → Revision Required | Investigation finding |
| Active → Superseded | Newer TDR or investigation |
| Revision Required → Active | Human approval |
| Any → Merged | Human approval |
| Superseded → Archived | Automated (6 months inactive) |
| Superseded → Removed | Human approval |
| Archived → Removed | Governance decision |

---

# 6. Recommended Lifecycle Policy

## 6.1 Policy Statement

**KDE Knowledge Artifact Lifecycle Policy (GOV-LIFECYCLE-001)**

All knowledge artifacts within KDE shall follow a defined lifecycle with explicit state transitions and preservation requirements.

## 6.2 Lifecycle States (Formal)

| State | Code | Description | Retention |
|-------|------|-------------|-----------|
| Draft | DRAFT | Initial creation, under development | Until completion or removal |
| Active | ACTIVE | Approved, current, authoritative | Indefinite while valid |
| Revision Required | REVREQ | Valuable but needs update | Until revised or transitioned |
| Merged | MERGED | Consolidated into another artifact | Historical reference only |
| Superseded | SUPERSEDED | Replaced by newer knowledge | Historical reference only |
| Historical | HISTORICAL | Preserved for context | Long-term preservation |
| Archived | ARCHIVED | Not maintained, not referenced | Optional long-term |
| Removed | REMOVED | Deleted from repository | Git history only |

## 6.3 State Metadata

Each artifact shall include lifecycle metadata:

```yaml
lifecycle:
  state: ACTIVE
  previous_states: [DRAFT]
  state_history:
    - { state: DRAFT, date: "2026-07-24", reason: "Created" }
    - { state: ACTIVE, date: "2026-07-24", reason: "Human approval" }
  next_state: null
  superseded_by: null
  merged_into: null
```

## 6.4 Preservation Requirements

| State | Preservation | Knowledge Extraction Required |
|-------|-------------|------------------------------|
| DRAFT | No | N/A |
| ACTIVE | Yes | N/A |
| REVREQ | Yes | Optional |
| MERGED | Historical | Yes - extract to target |
| SUPERSEDED | Historical | Optional |
| HISTORICAL | Yes | N/A |
| ARCHIVED | Optional | No |
| REMOVED | Git only | Yes - before removal |

## 6.5 Transition Authority Matrix

| From \ To | DRAFT | ACTIVE | REVREQ | MERGED | SUPERSEDED | HISTORICAL | ARCHIVED | REMOVED |
|-----------|-------|--------|--------|--------|------------|------------|----------|----------|
| DRAFT | - | Human | - | - | - | - | - | Human |
| ACTIVE | - | - | INV | Human | INV | - | - | Human |
| REVREQ | - | Human | - | Human | - | - | - | Human |
| MERGED | - | - | - | - | - | - | - | Human |
| SUPERSEDED | - | - | - | - | - | Auto | Auto | Human |
| HISTORICAL | - | - | - | - | - | - | Auto | Human |
| ARCHIVED | - | - | - | - | - | - | - | Human |

Legend: INV = Investigation finding, Auto = Automated transition, Human = Human approval required

---

# 7. Final Recommendation

## 7.1 Recommended Policy

**Adopt GOV-LIFECYCLE-001: KDE Knowledge Artifact Lifecycle Policy**

This policy establishes:
1. 8 lifecycle states with clear definitions
2. Explicit transition criteria and authorities
3. Preservation requirements before removal
4. Metadata requirements for state tracking

## 7.2 Implementation Requirements

| Requirement | Description |
|-------------|-------------|
| Add lifecycle metadata | Update artifact templates to include lifecycle state |
| Create state transitions | Define procedures for each state change |
| Establish review cadence | Annual lifecycle review for all artifacts |
| Automate archival | Archive after 6 months inactive |
| Require extraction | Extract knowledge before removal |

## 7.3 Relationship to Existing Governance

| Document | Relationship |
|----------|--------------|
| NAMING-CONVENTIONS.md | Complements - lifecycle adds temporal dimension |
| INV-016 recommendation | Aligned - revision requirement state defined |
| LEGACY/ directories | Aligned - historical preservation pattern |

## 7.4 Benefits

| Benefit | Impact |
|---------|--------|
| Predictable evolution | Clear path for artifact lifecycle |
| Reduced complexity | Regular cleanup prevents accumulation |
| Knowledge preservation | Extraction requirement ensures no loss |
| Engineering clarity | Active artifacts always authoritative |
| Governance clarity | Explicit authority for each transition |

## 7.5 Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Over-removal | Require knowledge extraction before removal |
| Over-retention | Annual review and automation |
| Confusion during transitions | Clear metadata and cross-references |
| Authority bottlenecks | Automate safe transitions |

## 7.6 Success Metrics

| Metric | Target |
|--------|--------|
| Artifacts with lifecycle metadata | 100% |
| Active artifacts current | >90% |
| Superseded without knowledge loss | 100% |
| Lifecycle review frequency | Annual |
| Average artifact age (active) | <12 months |

---

## 7.7 Investigation Conclusion

| Criterion | Finding |
|-----------|---------|
| Is a formal lifecycle needed? | **YES** - no current governance exists |
| Should artifacts be preserved? | **EXTRACT FIRST** - knowledge over container |
| Should duplicates be merged? | **YES** - repository clarity |
| Should obsolete be removed? | **YES** - after extraction and archival |
| Is complexity a concern? | **YES** - thresholds and reviews recommended |

---

*Investigation completed per KDE Runtime governance*
*Awaiting human review for recommendation adoption*
