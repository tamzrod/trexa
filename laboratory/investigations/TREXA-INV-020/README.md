# TREXA-INV-020: Documentation Knowledge Architecture Investigation

**Status**: COMPLETE
**Type**: Investigation
**Date**: 2026-07-24
**Human Review**: APPROVED WITH ADDENDUM

## Purpose

Determine the optimal documentation architecture for the Trexa repository.

## Key Findings

| Finding | Assessment |
|---------|------------|
| Current state | Two domains: KDE (runtime) + Laboratory (engineering) |
| Gap identified | No dedicated human documentation domain exists |
| Recommendation | Tripartite architecture (KDE + Human Docs + Laboratory) |

## Human Review Addendum

The reviewer approved the architecture with a refinement:
- Use `docs/` as the single human-facing documentation domain (instead of `product/`)
- The `docs/` directory contains `application/` (product docs) and `kde/` (methodology docs)

## Investigation Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Documentation Architecture Assessment | SPEC.md Section 1 |
| 2 | Knowledge Domain Classification | SPEC.md Section 2 |
| 3 | Documentation Ownership Matrix | SPEC.md Section 3 |
| 4 | Information Boundary Analysis | SPEC.md Section 4 |
| 5 | Cross-Reference Strategy | SPEC.md Section 5 |
| 6 | Navigation Hierarchy | SPEC.md Section 6 |
| 7 | Migration Recommendations | SPEC.md Section 7 |
| 8 | Risks and Trade-offs | SPEC.md Section 8 |
| 9 | Final Documentation Architecture | SPEC.md Section 9 |
| 10 | Final Recommendation | SPEC.md Section 10 |

## Recommendation Summary

**Establish a Tripartite Documentation Architecture:**

```
.kde/        → Runtime Knowledge (Bootstrap Authority)
docs/        → Human Documentation (NEW per Human Review)
laboratory/  → Engineering Knowledge
```

## Files

| File | Purpose |
|------|---------|
| `SPEC.md` | Full investigation report |
| `README.md` | This summary |
| `CONCLUSION.md` | Key conclusions |

---

*Investigation completed per KDE Runtime governance*
*Human Review: APPROVED WITH ADDENDUM*
*Pending: Create `docs/` directory structure*
