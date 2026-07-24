# Core vs. Domain Classification: TREXA-INV-002

**Investigation**: TREXA-INV-002
**Title**: Platform Capability Discovery
**Date**: 2026-07-23T08:30:00Z
**Status**: COMPLETE

---

## Classification Overview

This document classifies each capability as CORE (platform) or DOMAIN (domain-specific).

---

## Core Capabilities

Core capabilities are required by ALL domains and form the foundation of the platform.

### Core: Foundational (4)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-001 | Workspace Management | All domains need a drawing surface |
| CAP-002 | Coordinate System Management | All domains need positioning |
| CAP-007 | Data Model Management | All domains need data persistence |
| CAP-020 | Event Handling | All domains need input handling |

### Core: Object Management (4)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-003 | Layer Management | All domains organize visual layers |
| CAP-005 | Object Instantiation | All domains create objects |
| CAP-006 | Object Positioning | All domains position objects |
| CAP-008 | Selection Management | All domains need selection |

### Core: Connection Management (2)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-010 | Connection Creation | All domains connect objects |
| CAP-016 | Connection Rendering | All domains render connections |

### Core: Rendering (2)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-013 | Primitive Rendering | All domains render primitives |
| CAP-015 | Renderer Abstraction | All domains need rendering flexibility |

### Core: Interaction (4)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-017 | Drag-and-Drop Support | WYSIWYG requirement for all domains |
| CAP-018 | Object Manipulation | All domains need resize/rotate |
| CAP-019 | Undo/Redo Support | All domains need operation reversal |
| CAP-032 | Navigation Support | All domains need pan/zoom |

### Core: State Management (1)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-021 | State Management | All domains may have dynamic states |

### Core: Domain Management (2)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-023 | Domain Registry | Required for multi-domain support |
| CAP-033 | Domain Switching | Required for multi-domain support |

### Core: Persistence (3)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-026 | Diagram Persistence | All domains need save/load |
| CAP-027 | Export Capability | All domains need export |
| CAP-028 | Primitive Library Persistence | All domains need primitive storage |

### Core: User Interface (4)

| ID | Capability | Rationale |
|----|------------|-----------|
| CAP-029 | Object Palette | All domains need primitive selection |
| CAP-030 | Properties Panel | All domains need property editing |
| CAP-031 | Toolbar Management | All domains need tools |
| CAP-035 | Shared Rendering Infrastructure | All domains share background rendering |

---

## Domain Capabilities

Domain capabilities are specific to particular engineering domains and require domain-specific implementations.

### Domain: Primitive Definition (1)

| ID | Capability | Domain-Specific Element |
|----|------------|------------------------|
| CAP-004 | Primitive Definition | Each domain defines different primitives (CB vs Point) |

### Domain: Connection Modeling (3)

| ID | Capability | Domain-Specific Element |
|----|------------|------------------------|
| CAP-009 | Connection Point Definition | Connection point types vary by primitive |
| CAP-011 | Connection Routing | Routing rules differ (orthogonal for SLD, geodesic for GIS) |
| CAP-012 | Relationship Modeling | Relationship semantics vary by domain |

### Domain: Visualization (1)

| ID | Capability | Domain-Specific Element |
|----|------------|------------------------|
| CAP-014 | State Visualization | State-to-visual mapping varies (SLD states vs GIS symbols) |

### Domain: Validation (1)

| ID | Capability | Domain-Specific Element |
|----|------------|------------------------|
| CAP-024 | Domain Validation | Validation rules vary by domain (topology rules vs spatial rules) |

### Domain: Styling (1)

| ID | Capability | Domain-Specific Element |
|----|------------|------------------------|
| CAP-025 | Domain Styling | Color schemes and styles vary by domain |

---

## Optional Capabilities

### Optional: State Integration (1)

| ID | Capability | Optional Reason |
|----|------------|-----------------|
| CAP-022 | External Data Integration | Can use static state for MVP |

### Optional: Multi-Domain (1)

| ID | Capability | Optional Reason |
|----|------------|-----------------|
| CAP-034 | Cross-Domain Connections | Only needed for cross-domain diagrams |

---

## Classification Summary

| Category | Count | Percentage |
|----------|-------|------------|
| **CORE** | 26 | 76% |
| **DOMAIN** | 6 | 18% |
| **OPTIONAL** | 2 | 6% |
| **Total** | 34 | 100% |

---

## Core vs. Domain Ratio

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPABILITY DISTRIBUTION                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  CORE (26 capabilities) ████████████████████████████ 76%    │
│                                                              │
│  DOMAIN (6 capabilities) ██████ 18%                        │
│                                                              │
│  OPTIONAL (2 capabilities) ██ 6%                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Domain Capability Allocation

### SLD Domain

| Core Capabilities Used | Domain-Specific Implementation |
|----------------------|-------------------------------|
| All 26 core capabilities | CAP-004: CB, DS, ES, Bus, Transformer primitives |
| | CAP-009: Connection points per primitive |
| | CAP-011: Orthogonal routing with 90° angles |
| | CAP-012: Power flow relationships |
| | CAP-014: CLOSED/OPEN/UNKNOWN state visualization |
| | CAP-024: Topology validation rules |
| | CAP-025: Electrical color scheme (voltage colors) |

**SLD Total**: 26 core + 7 domain = 33 capabilities

---

### GIS Domain

| Core Capabilities Used | Domain-Specific Implementation |
|----------------------|-------------------------------|
| All 26 core capabilities | CAP-004: Point, Line, Polygon primitives |
| | CAP-009: Connection points (optional for topology) |
| | CAP-011: Geodesic routing with coordinate transforms |
| | CAP-012: Spatial relationships (contains, intersects) |
| | CAP-014: Symbol-based visualization (optional states) |
| | CAP-024: Spatial validation rules |
| | CAP-025: Map symbol styles |

**GIS Total**: 26 core + 7 domain = 33 capabilities

---

### Future Domains (P&ID, SCADA, etc.)

Each future domain will implement:
- CAP-004: Domain-specific primitives
- CAP-009: Primitive-specific connection points
- CAP-011: Domain-appropriate routing
- CAP-012: Domain relationship semantics
- CAP-014: Domain state visualization (if applicable)
- CAP-024: Domain validation rules
- CAP-025: Domain styling

**Future Domain Total**: 26 core + up to 7 domain = up to 33 capabilities

---

## Implication for Implementation

### Platform Core Team

Responsible for: All 26 core capabilities
- Canvas, coordinate, layer management
- Object management and positioning
- Connection management
- Rendering abstraction
- User interaction
- State management
- Domain registry and switching
- Persistence and export
- User interface framework

### Domain Implementation Teams

Responsible for: Domain-specific capabilities (per domain)
- Primitive definitions
- Connection point definitions
- Routing rules
- Relationship semantics
- State visualization
- Validation rules
- Styling

---

## Classification Matrix

| Capability ID | CAP-001 | CAP-002 | CAP-003 | ... | CAP-034 |
|--------------|---------|---------|---------|-----|---------|
| **Type** | CORE | CORE | CORE | ... | OPTIONAL |
| **SLD** | ✓ | ✓ | ✓ | ... | - |
| **GIS** | ✓ | ✓ | ✓ | ... | - |
| **P&ID** | ✓ | ✓ | ✓ | ... | - |
| **SCADA** | ✓ | ✓ | ✓ | ... | - |

---

## Reuse Analysis

### Reusable Across All Domains (26 core)

1. CAP-001: Workspace Management
2. CAP-002: Coordinate System Management
3. CAP-003: Layer Management
4. CAP-005: Object Instantiation
5. CAP-006: Object Positioning
6. CAP-007: Data Model Management
7. CAP-008: Selection Management
8. CAP-010: Connection Creation
9. CAP-013: Primitive Rendering
10. CAP-015: Renderer Abstraction
11. CAP-016: Connection Rendering
12. CAP-017: Drag-and-Drop Support
13. CAP-018: Object Manipulation
14. CAP-019: Undo/Redo Support
15. CAP-020: Event Handling
16. CAP-021: State Management
17. CAP-023: Domain Registry
18. CAP-026: Diagram Persistence
19. CAP-027: Export Capability
20. CAP-028: Primitive Library Persistence
21. CAP-029: Object Palette
22. CAP-030: Properties Panel
23. CAP-031: Toolbar Management
24. CAP-032: Navigation Support
25. CAP-033: Domain Switching
26. CAP-035: Shared Rendering Infrastructure

### Must Be Reimplemented Per Domain (6 domain)

1. CAP-004: Primitive Definition
2. CAP-009: Connection Point Definition
3. CAP-011: Connection Routing
4. CAP-012: Relationship Modeling
5. CAP-024: Domain Validation
6. CAP-025: Domain Styling

**Reuse Ratio**: 26:6 or approximately **4:1**

---

## Classification Conclusion

| Finding | Value |
|---------|-------|
| **Core Capabilities** | 26 (76%) |
| **Domain-Specific** | 6 (18%) |
| **Optional** | 2 (6%) |
| **Reuse Ratio** | 4:1 (core:domain) |
| **Platform Team Scope** | 26 core capabilities |
| **Domain Team Scope** | 6-7 per domain |

---

**Classification Status**: COMPLETE

**Next**: Risks, Assumptions, Missing Capabilities
