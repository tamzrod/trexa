# TREXA-EXP-005: Core Invariant Discovery Experiment

**Status**: COMPLETE
**Type**: Experiment
**Date**: 2026-07-24

## Hypothesis

A single reusable visual representation model exists that can describe every intended Trexa application regardless of engineering domain.

## Conclusion

**HYPOTHESIS CONFIRMED**

The **Semantic Graph Model** is the core invariant of Trexa.

## Core Invariant

Every Trexa visualization domain is a **directed or undirected graph** where:

1. **Nodes** (Primitives) - Semantic elements with identity, type, visual, properties
2. **Edges** (Connections) - Relationships with source, target, type, properties
3. **Graph Properties** - Domain-specific rules

## Verification Results

| Domain | Fit | Evidence |
|--------|-----|----------|
| SLD | ✅ | Electrical circuits are graphs |
| GIS | ✅ | Spatial features + routes |
| P&ID | ✅ | Equipment + pipes |
| SCADA | ✅ | Points + data links |
| Dashboard | ✅ | Widgets + bindings |
| Network | ✅ | Devices + links |
| Knowledge Graph | ✅ | Entities + relationships |
| Workflow | ✅ | Activities + flow |
| Digital Twin | ✅ | Components + connections |
| Org Chart | ✅ | Positions + hierarchy |

**All 10 domains fit the graph model (100%)**

## Deliverables

| # | Deliverable | Status |
|---|-------------|--------|
| 1 | Domain Comparison Matrix | ✅ |
| 2 | Common Capability Matrix | ✅ |
| 3 | Variable Capability Matrix | ✅ |
| 4 | Candidate Core Invariant | ✅ |
| 5 | Evidence Assessment | ✅ |
| 6 | Final Recommendation | ✅ |

## Files

| File | Purpose |
|------|---------|
| `SPEC.md` | Full experiment specification and results |
| `RESULT.md` | Conclusion summary |

---

*Experiment completed per KDE Runtime governance*
