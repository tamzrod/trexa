# TREXA-INV-019: AI Module Value & Integration Investigation

**Status**: COMPLETE
**Type**: Investigation
**Date**: 2026-07-24

## Purpose

Determine whether the existing AI module (`ai/`) continues to provide engineering value and whether it should be retained, rewired, merged, archived, or removed.

## Module Under Review

| Component | Path | Purpose |
|-----------|------|---------|
| Classifier | `ai/classifier/classifier.py` | Task classification (15 categories) |
| Profiles | `ai/profiles/profiles.py` | 7 reasoning profiles |
| Routing | `ai/routing/engine.py` | Profile selection & orchestration |
| IR | `ai/ir/hybrid_ir.py` | Information retrieval |
| Telemetry | `ai/telemetry/telemetry.py` | Decision logging |

## Key Findings

| Finding | Assessment |
|---------|------------|
| Functional value | **HIGH** - Complete, working implementation |
| Maintenance cost | **LOW** - No external dependencies |
| Alignment with vision | **HIGH** - AI-first methodology |
| ROE Score | **9.0/10** |
| Strategic risk | **LOW** |

## Recommendation

**RETAIN + INTEGRATE**

The AI module provides significant engineering value and should be retained. The recommended action is to **rewire** the module into the KDE architecture:

| Action | Target | Priority |
|--------|--------|----------|
| Wire telemetry | `.kde/verification/` | MEDIUM |
| Wire IR | `.kde/knowledge/` | MEDIUM |
| Document in capabilities | `.kde/capabilities/` | LOW |

## Component Recommendations

| Component | Recommendation | Rationale |
|-----------|---------------|-----------|
| `ai/classifier/` | **RETAIN** | Core engine |
| `ai/profiles/` | **RETAIN** | Essential data |
| `ai/routing/` | **RETAIN** | Core orchestration |
| `ai/ir/` | **RETAIN (Rewire)** | Integrate with knowledge |
| `ai/telemetry/` | **RETAIN (Rewire)** | Integrate with verification |

## Deliverables

| # | Deliverable | Status |
|---|-------------|--------|
| 1 | AI Module Assessment | ✅ |
| 2 | Original Intent Reconstruction | ✅ |
| 3 | Current Integration Analysis | ✅ |
| 4 | Dependency Analysis | ✅ |
| 5 | Capability Assessment | ✅ |
| 6 | Architectural Alignment Assessment | ✅ |
| 7 | Cost vs Value Analysis | ✅ |
| 8 | Risk Assessment | ✅ |
| 9 | Recommendation Matrix | ✅ |
| 10 | Final Recommendation | ✅ |

## Files

| File | Purpose |
|------|---------|
| `SPEC.md` | Full investigation report |

---

*Investigation completed per KDE Runtime governance*
*Awaiting human review*
