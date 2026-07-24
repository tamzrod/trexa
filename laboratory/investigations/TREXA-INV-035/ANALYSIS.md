# TREXA-INV-035: Artifact Analysis

**Investigation ID**: TREXA-INV-035
**Title**: Repository Salvage Report
**Date**: 2026-07-24
**Status**: IN_PROGRESS

---

# Part 1: .kde/ Runtime Artifacts Analysis

## 1.1 Artifact Inventory

| File | Size | Purpose |
|------|------|---------|
| .kde/README.md | Core | Runtime overview |
| .kde/bootstrap/README.md | Core | Bootstrap documentation |
| .kde/bootstrap/config.yaml | Core | Runtime configuration |
| .kde/bootstrap/requirements.json | Core | System requirements |
| .kde/capabilities/README.md | Governance | Capabilities documentation |
| .kde/commands/README.md | Governance | Commands documentation |
| .kde/engines/README.md | Governance | Engines documentation |
| .kde/experts/README.md | Governance | Experts documentation |
| .kde/governance/NAMING-CONVENTIONS.md | Governance | Naming policy |
| .kde/governance/README.md | Governance | Governance overview |
| .kde/knowledge/README.md | Governance | Knowledge documentation |
| .kde/runtime/README.md | Core | Runtime documentation |
| .kde/runtime/state.json | Core | Runtime state |
| .kde/seeds/README.md | Governance | Seeds documentation |
| .kde/templates/IMP.md | Governance | IMP template |
| .kde/templates/README.md | Governance | Templates documentation |
| .kde/verification/README.md | Governance | Verification documentation |

## 1.2 Classification: .kde/

| Artifact | Classification | Rationale |
|----------|----------------|-----------|
| .kde/README.md | **Preserve** | Core runtime documentation |
| .kde/bootstrap/README.md | **Preserve** | Bootstrap process documentation |
| .kde/bootstrap/config.yaml | **Preserve** | Runtime configuration |
| .kde/bootstrap/requirements.json | **Preserve** | System requirements |
| .kde/capabilities/README.md | **Preserve** | Capability definitions |
| .kde/commands/README.md | **Preserve** | Command definitions |
| .kde/engines/README.md | **Preserve** | Engine documentation |
| .kde/experts/README.md | **Preserve** | Expert documentation |
| .kde/governance/NAMING-CONVENTIONS.md | **Preserve** | Governance policy |
| .kde/governance/README.md | **Preserve** | Governance overview |
| .kde/knowledge/README.md | **Preserve** | Knowledge documentation |
| .kde/runtime/README.md | **Preserve** | Runtime documentation |
| .kde/runtime/state.json | **Preserve** | Runtime state tracking |
| .kde/seeds/README.md | **Preserve** | Seeds documentation |
| .kde/templates/IMP.md | **Preserve** | IMP artifact template |
| .kde/templates/README.md | **Preserve** | Templates documentation |
| .kde/verification/README.md | **Preserve** | Verification documentation |

**Classification**: ALL PRESERVE
**Rationale**: All .kde/ artifacts are runtime infrastructure required for KDE operation. No modifications recommended.

---

# Part 2: ai/ Module Artifacts Analysis

## 2.1 Artifact Inventory

| File | Purpose | Evidence |
|------|---------|----------|
| ai/__init__.py | Module init | Python package |
| ai/classifier/__init__.py | Classifier init | Python package |
| ai/classifier/classifier.py | Task classification | Defines TaskCategory, ComplexityLevel |
| ai/ir/__init__.py | IR init | Python package |
| ai/ir/hybrid_ir.py | Information retrieval | Hybrid IR system |
| ai/profiles/__init__.py | Profiles init | Python package |
| ai/profiles/profiles.py | Reasoning profiles | 7 profiles defined |
| ai/routing/__init__.py | Routing init | Python package |
| ai/routing/engine.py | Routing engine | AI routing orchestration |
| ai/telemetry/__init__.py | Telemetry init | Python package |
| ai/telemetry/telemetry.py | Telemetry system | Usage tracking |

## 2.2 Engineering Knowledge in ai/

### AI Profiles (ai/profiles/profiles.py)

**Engineering Knowledge Identified**:
- 7 reasoning profiles: FAST, BALANCED, DEEP, VERIFICATION, CREATIVE, HYBRID_IR, DIAGNOSTIC
- Profile configurations with depth, context_window, retrieval, verification_level
- Latency and cost tiers
- Task categories mapping

**Evidence Source**: INV-003 defines AI strategy, this implements it

### Task Classifier (ai/classifier/classifier.py)

**Engineering Knowledge Identified**:
- 17 task categories: RETRIEVAL_SIMPLE, VALIDATION_STANDARD, GENERATION_CREATIVE, etc.
- 5 complexity levels: TRIVIAL to VERY_HIGH
- Task characteristics affecting profile selection

**Evidence Source**: INV-003 and INV-008

### Routing Engine (ai/routing/engine.py)

**Engineering Knowledge Identified**:
- Selection strategies: DIRECT, WEIGHTED, CASCADE, PARALLEL
- Execution result structure
- Criteria for profile selection

**Evidence Source**: INV-003

### Hybrid IR (ai/ir/hybrid_ir.py)

**Engineering Knowledge Identified**:
- Retrieval strategies: SEMANTIC, KEYWORD, HYBRID, EXACT
- Context retrieval and compression
- Relevance scoring

**Evidence Source**: INV-002 (Capabilities)

### Telemetry (ai/telemetry/telemetry.py)

**Engineering Knowledge Identified**:
- Usage tracking system
- Performance metrics

**Evidence Source**: INV-002 (Capabilities)

## 2.3 Classification: ai/

| Artifact | Classification | Rationale |
|----------|----------------|-----------|
| ai/__init__.py | **Preserve** | Python package infrastructure |
| ai/classifier/__init__.py | **Preserve** | Python package infrastructure |
| ai/classifier/classifier.py | **Preserve** | Engineering knowledge: task categories, complexity levels |
| ai/ir/__init__.py | **Preserve** | Python package infrastructure |
| ai/ir/hybrid_ir.py | **Preserve** | Engineering knowledge: IR strategies, context retrieval |
| ai/profiles/__init__.py | **Preserve** | Python package infrastructure |
| ai/profiles/profiles.py | **Preserve** | Engineering knowledge: 7 reasoning profiles |
| ai/routing/__init__.py | **Preserve** | Python package infrastructure |
| ai/routing/engine.py | **Preserve** | Engineering knowledge: routing strategies |
| ai/telemetry/__init__.py | **Preserve** | Python package infrastructure |
| ai/telemetry/telemetry.py | **Preserve** | Engineering knowledge: telemetry system |

**Classification**: ALL PRESERVE
**Rationale**: ai/ module contains implementation of AI routing architecture defined in INV-003. These are source code implementations, not documentation or evidence.

**Duplicate Knowledge Note**: The profile definitions, task categories, and routing logic are documented in TREXA-INV-003. The source code is the authoritative implementation.

---

# Part 3: docs/ Documentation Artifacts Analysis

## 3.1 Artifact Inventory

### Application Documentation

| File | Purpose |
|------|---------|
| docs/README.md | Documentation hub |
| docs/application/README.md | Application docs hub |
| docs/application/api/README.md | API documentation |
| docs/application/architecture/README.md | Architecture documentation |
| docs/application/getting-started/README.md | Quick start |
| docs/application/guides/README.md | User guides |
| docs/application/reference/README.md | Technical reference |
| docs/application/roadmap/README.md | Product roadmap |

### KDE Methodology Documentation

| File | Purpose |
|------|---------|
| docs/kde/README.md | KDE docs hub |
| docs/kde/governance/README.md | Governance documentation |
| docs/kde/history/README.md | KDE evolution history |
| docs/kde/methodology/AI-FIRST-METHODOLOGY.md | AI-First methodology |
| docs/kde/principles/ENGINEERING-PRINCIPLES.md | Engineering principles |
| docs/kde/reviews/README.md | KDE reviews |
| docs/kde/runtime-concepts/README.md | Runtime concepts |

## 3.2 Engineering Knowledge in docs/

### AI-First Methodology (docs/kde/methodology/AI-FIRST-METHODOLOGY.md)

**Engineering Knowledge Identified**:
- AI-First evaluation criteria framework
- Traditional vs AI-First criteria weights
- 8 criteria: Engineering Capability, AI-Enabled Productivity, Ecosystem, etc.
- Evidence hierarchy

**Laboratory Relationship**: Captured in TREXA-INV-008
**Duplication Status**: DUPLICATE - Both laboratory and docs have this content

### Engineering Principles (docs/kde/principles/ENGINEERING-PRINCIPLES.md)

**Engineering Knowledge Identified**:
- 5 core principles: Evidence Over Intuition, Experiment Before Deployment, Preserve Ambiguity, Traceability Always, Reproducibility Required

**Laboratory Relationship**: Partially in TREXA-INV-014, TREXA-INV-032
**Duplication Status**: PARTIAL DUPLICATE - Core principles also in laboratory

### Product Roadmap (docs/application/roadmap/README.md)

**Engineering Knowledge Identified**:
- 5 development phases with milestones
- Phase 1: Foundation (current)
- Phase 2-5: Implementation plan

**Laboratory Relationship**: No direct laboratory artifact
**Duplication Status**: UNIQUE - Product planning in docs only

### Architecture Documentation (docs/application/architecture/README.md)

**Engineering Knowledge Identified**:
- Cross-references to laboratory investigations
- Architecture principles
- Key architecture documents list

**Laboratory Relationship**: All content from INV-011, INV-006, INV-003
**Duplication Status**: DUPLICATE - Summary of laboratory findings

## 3.3 Classification: docs/

### Application Documentation

| Artifact | Classification | Rationale |
|----------|----------------|-----------|
| docs/README.md | **Preserve** | Documentation hub per INV-020 |
| docs/application/README.md | **Preserve** | Application docs entry |
| docs/application/api/README.md | **Preserve** | API documentation structure |
| docs/application/architecture/README.md | **Migrate to Documentation** | Architecture summary (keep in docs) |
| docs/application/getting-started/README.md | **Preserve** | User onboarding |
| docs/application/guides/README.md | **Preserve** | User guides structure |
| docs/application/reference/README.md | **Preserve** | Technical reference structure |
| docs/application/roadmap/README.md | **Preserve** | Product roadmap - unique to docs |

### KDE Methodology Documentation

| Artifact | Classification | Rationale |
|----------|----------------|-----------|
| docs/kde/README.md | **Preserve** | KDE docs hub |
| docs/kde/governance/README.md | **Preserve** | Governance docs |
| docs/kde/history/README.md | **Archive** | Historical - minimal content (v1.0.0 only) |
| docs/kde/methodology/AI-FIRST-METHODOLOGY.md | **Preserve** | Human-readable methodology |
| docs/kde/principles/ENGINEERING-PRINCIPLES.md | **Preserve** | Human-readable principles |
| docs/kde/reviews/README.md | **Preserve** | Review documentation |
| docs/kde/runtime-concepts/README.md | **Preserve** | Runtime concepts for humans |

---

# Part 4: Root Artifacts Analysis

## 4.1 Artifact Inventory

| File | Purpose |
|------|---------|
| README.md | Project overview |
| LICENSE | MIT License |

## 4.2 Classification: Root

| Artifact | Classification | Rationale |
|----------|----------------|-----------|
| README.md | **Preserve** | Project entry point, triparte reference |
| LICENSE | **Preserve** | Legal requirement |

---

# Part 5: Duplicate Knowledge Analysis

## 5.1 Knowledge Duplicated in Laboratory and Docs

| Topic | Docs Location | Laboratory Location | Status |
|-------|---------------|---------------------|--------|
| AI-First Methodology | docs/kde/methodology/ | TREXA-INV-008, INV-008A | DUPLICATE |
| Engineering Principles | docs/kde/principles/ | TREXA-INV-014, INV-032 | PARTIAL |
| Architecture | docs/application/architecture/ | TREXA-INV-011, INV-006 | DUPLICATE |
| Platform Capabilities | docs/application/architecture/ | TREXA-INV-002 | DUPLICATE |
| KDE Framework | docs/kde/runtime-concepts/ | .kde/ directory | EXPECTED |

## 5.2 Knowledge Unique to Laboratory

| Topic | Location | Status |
|-------|----------|--------|
| Experiment results | laboratory/experiments/ | UNIQUE |
| Investigation conclusions | laboratory/investigations/ | UNIQUE |
| Technology decisions | laboratory/decisions/ | UNIQUE |
| Implementation specs | laboratory/implementations/ | UNIQUE |

## 5.3 Knowledge Unique to Runtime

| Topic | Location | Status |
|----------|---------|--------|
| Bootstrap configuration | .kde/bootstrap/ | UNIQUE |
| Runtime state | .kde/runtime/state.json | UNIQUE |
| Naming conventions | .kde/governance/ | UNIQUE |
| Templates | .kde/templates/ | UNIQUE |

## 5.4 Knowledge Unique to Documentation

| Topic | Location | Status |
|-------|----------|--------|
| Product roadmap | docs/application/roadmap/ | UNIQUE |
| User guides | docs/application/guides/ | UNIQUE |
| Getting started | docs/application/getting-started/ | UNIQUE |

---

# Part 6: Orphaned Knowledge Analysis

## 6.1 No Orphaned Knowledge Identified

**Result**: All engineering knowledge found in repository is already represented in the Laboratory or appropriately located.

### Evidence:

| Knowledge Type | Location | Laboratory Representation |
|----------------|----------|--------------------------|
| AI profiles | ai/profiles/profiles.py | TREXA-INV-003 |
| Task categories | ai/classifier/classifier.py | TREXA-INV-003 |
| Routing strategies | ai/routing/engine.py | TREXA-INV-003 |
| IR strategies | ai/ir/hybrid_ir.py | TREXA-INV-002 |
| Methodology | docs/kde/methodology/ | TREXA-INV-008 |
| Principles | docs/kde/principles/ | TREXA-INV-014 |
| Architecture | docs/application/architecture/ | TREXA-INV-011 |

---

# Part 7: Temporary or Obsolete Content

## 7.1 Potential Temporary Content

| Artifact | Status | Recommendation |
|----------|--------|----------------|
| laboratory_BACKUP_20260724_014010/ | Obsolete backup | DISCARD - Old backup directory |
| .kde/runtime/state.json | Active state | PRESERVE - Current runtime state |

## 7.2 No Temporary Content Found in Active Locations

All artifacts in .kde/, ai/, docs/, and root are either:
- Active runtime/knowledge infrastructure
- User documentation
- Source code implementations

---

# Summary: Artifact Classification

## Classification Matrix

| Location | Total | Preserve | Migrate | Archive | Discard |
|----------|-------|----------|---------|---------|---------|
| .kde/ | 17 | 17 | 0 | 0 | 0 |
| ai/ | 12 | 12 | 0 | 0 | 0 |
| docs/ | 15 | 14 | 1 | 1 | 0 |
| root/ | 2 | 2 | 0 | 0 | 0 |
| **TOTAL** | **46** | **45** | **1** | **1** | **0** |

## Recommendations Summary

| Classification | Count | Action |
|----------------|-------|--------|
| Preserve | 45 | Retain in current location |
| Migrate to Documentation | 1 | Keep architecture summaries in docs |
| Archive | 1 | docs/kde/history/ (minimal content) |
| Discard | 0 | No artifacts to discard |

---

*Analysis completed per KDE Runtime governance*
