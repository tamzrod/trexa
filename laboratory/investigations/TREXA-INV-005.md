# Investigation: TREXA-INV-005

**ID**: TREXA-INV-005
**Title**: Gap Analysis and Next Investigation Recommendation
**Version**: 1.0.0
**Date**: 2026-07-23T10:30:00Z
**Status**: ACTIVE
**Author**: KDE Runtime (KDE-ENGINE-002 Beta)
**Seed**: SEED-001 (Genesis)

---

## Purpose

Determine the single highest-value next investigation to advance Trexa toward a usable engineering user interface.

---

## Current Knowledge Baseline

### Human Intent (AUTHORITATIVE)

> Trexa is a visual engineering platform where users can create engineering diagrams using a WYSIWYG interface.
> 
> The platform shall support multiple engineering domains from a common architecture.
> 
> Initial supported domains: SLD, GIS
> 
> The platform shall support: drag-and-drop, connection points, engineering relationships, reusable rendering technologies.

### What We Have

| Investigation | Status | What It Provides |
|-------------|--------|------------------|
| **TREXA-INV-001** | Complete | Engineering implications observations |
| **TREXA-INV-002** | Complete | 34 platform capabilities identified |
| **TREXA-INV-003** | Complete | AI routing system implemented |
| **AI Module** | Implemented | Profiles, classifier, IR, routing, telemetry |

### What We Need (Per Human Intent)

| Requirement | Gap Status |
|------------|-----------|
| WYSIWYG interface | Platform capabilities known, not implemented |
| Drag-and-drop objects | Capability identified (CAP-017), not implemented |
| Connection points | Capability identified (CAP-009), not implemented |
| Engineering relationships | Capability identified (CAP-012), not implemented |
| SLD domain | **NOT YET INVESTIGATED FOR TREXA** |
| GIS domain | **NOT YET INVESTIGATED FOR TREXA** |

---

## Gap Analysis

### Gap Category 1: Platform Core

**Status**: CAPABILITIES KNOWN, NOT IMPLEMENTED

TREXA-INV-002 identified 34 capabilities, but:
- These are research findings, not implementation specs
- No implementation approach has been validated
- Dependency chains are known but untested

**Gap Severity**: MEDIUM
**Blocker**: NO (can proceed with implementation once domain is defined)

---

### Gap Category 2: Domain Specification

**Status**: NOT YET INVESTIGATED

The platform needs domain-specific knowledge:

| What Platform Needs | Source Available | Gap |
|-------------------|-------------------|-----|
| Primitive definitions | KDE SLD Expert | Must translate to Trexa format |
| Connection point specs | KDE SLD Expert | Must define for platform |
| Rendering rules | KDE SLD Expert | Must map to renderer abstraction |
| State visualization | KDE SLD Expert | Must define state machine |
| Validation rules | KDE SLD Expert | Must define for CAP-024 |

**Gap Severity**: HIGH
**Blocker**: YES (without domain, platform has no content)

---

### Gap Category 3: Integration Path

**Status**: UNCLEAR

Questions that remain:
- How do platform capabilities integrate with domain implementations?
- What's the minimal viable platform subset for initial domain?
- What's the development sequence?

**Gap Severity**: MEDIUM
**Blocker**: NO (can be resolved during implementation)

---

## Option Analysis

### Option A: SLD Domain Specification

**Description**: Define SLD primitives, connection points, and behaviors for Trexa platform.

**Investigates**:
- Trexa-specific primitive definitions (CB, DS, ES, Bus, Transformer)
- Connection point specifications per primitive
- State machine for each primitive
- Validation rules for topology
- Rendering requirements per primitive

**From Human Intent**: Directly enables "drag-and-drop engineering objects" for SLD

**Return on Investment**:
- Enables first usable domain
- Validates platform capabilities
- Provides template for future domains

**Estimated Effort**: 1 investigation

---

### Option B: Minimal Viable Platform Specification

**Description**: Define the minimal platform capability subset needed for first domain.

**Investigates**:
- Which of 34 capabilities are truly minimal?
- What can be deferred?
- What's the MVP scope?

**From Human Intent**: Indirect - defines implementation scope, not content

**Return on Investment**:
- Reduces scope uncertainty
- May conflict with domain requirements

**Estimated Effort**: 1 investigation

---

### Option C: GIS Domain Specification

**Description**: Define GIS primitives, connection points, and behaviors.

**Investigates**: Similar to Option A but for GIS

**From Human Intent**: Enables GIS domain, but SLD listed first

**Return on Investment**: Equal to Option A, but SLD is higher priority per intent

---

## Recommendation

### Single Recommended Investigation: **SLD Domain Specification**

**Title**: TREXA-INV-006: SLD Domain Definition for Trexa Platform

**Scope**:
1. Map KDE SLD expert knowledge to Trexa primitive definitions
2. Define connection points for each SLD primitive
3. Specify state machines and visualizations
4. Define topology validation rules
5. Determine rendering requirements

---

## Justification

### Why SLD Domain Specification Has Highest ROI

| Factor | Analysis |
|--------|----------|
| **Human Intent Order** | SLD listed before GIS |
| **Content Requirement** | Platform needs content to be usable |
| **Knowledge Availability** | KDE SLD expert provides foundation |
| **Validation Opportunity** | Tests platform capabilities end-to-end |
| **Template Value** | GIS and future domains follow same pattern |

### Why NOT Minimal Viable Platform

| Factor | Analysis |
|--------|----------|
| **Scope Reduction** | May defer necessary capabilities |
| **Content Gap** | Platform without domain is unusable |
| **Sequence** | Domain defines capability requirements |

---

## Expected Deliverables

### From SLD Domain Specification Investigation

| Deliverable | Purpose |
|------------|---------|
| Primitive Definitions | Trexa-specific specs for CB, DS, ES, Bus, Transformer |
| Connection Point Spec | Attachment points with types and constraints |
| State Machine Spec | States, transitions, visualization |
| Validation Rules | Topology rules for CAP-024 |
| Rendering Requirements | Visual specs for CAP-013 |
| Integration Guide | How domain uses platform capabilities |

---

## Expected Implementation Impact

### Immediate

1. **First usable domain**: SLD diagrams can be rendered and edited
2. **Platform validation**: Tests that 34 capabilities are sufficient
3. **Pattern established**: GIS and future domains follow same approach

### Secondary

1. **Platform refinements**: Gaps discovered during domain integration
2. **GIS foundation**: Partial reuse for GIS domain
3. **Documentation**: Domain authoring guide for future domains

---

## Success Criteria

### For Investigation (TREXA-INV-006)

| Criteria | Definition |
|----------|------------|
| Completeness | All SLD primitives defined with connection points |
| Feasibility | All specs achievable with known capabilities |
| Validation | Specs can be rendered by AI module's profiles |
| Integration | Clear how domain uses CAP-001 through CAP-035 |

### For Implementation (Post-Investigation)

| Criteria | Definition |
|----------|------------|
| WYSIWYG Editing | User can drag-drop SLD primitives |
| Connection Creation | User can connect primitives at valid points |
| State Visualization | Primitives display CLOSED/OPEN/UNKNOWN states |
| Basic Validation | Platform validates SLD topology |

---

## Conclusion

### Single Recommended Next Investigation

**TREXA-INV-006**: SLD Domain Definition for Trexa Platform

### Rationale

1. **Highest ROI**: Enables first usable domain
2. **Directly advances intent**: "drag-and-drop engineering objects" → SLD primitives
3. **Knowledge available**: KDE SLD expert provides foundation
4. **Validates platform**: Tests that 34 capabilities are sufficient
5. **Establishes pattern**: Future domains follow same approach

### What This Is NOT

- Not platform architecture design
- Not AI routing optimization
- Not GIS domain investigation
- Not implementation planning

---

**Recommendation Status**: READY FOR HUMAN REVIEW

**Proposed Investigation**: TREXA-INV-006: SLD Domain Definition

**Awaiting human authorization before proceeding.**
