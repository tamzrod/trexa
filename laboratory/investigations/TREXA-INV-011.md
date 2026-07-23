# Investigation: TREXA-INV-011

**ID**: TREXA-INV-011
**Title**: Foundation Architecture
**Version**: 1.0.0
**Date**: 2026-07-23T21:00:00Z
**Status**: COMPLETE
**Author**: KDE Runtime (KDE-ENGINE-002 Beta)
**Seed**: SEED-001 (Genesis)

---

## Investigation Objective

Define the minimum architectural foundation required before implementation begins.

**This is NOT BDUF.** This investigation establishes only the decisions that have high Return on Engineering and will significantly reduce future rework.

---

## Context

### Approved Technology Decisions

| TDR | Technology | Implication |
|-----|-----------|-------------|
| TDR-001 | JointJS | Rendering engine selected |
| TDR-002 | TypeScript | Language selected |
| TDR-003 | React | UI framework selected |

### Constraints Applied

- AI-First development
- FOSS (no commercial lock-in)
- Modular and extensible
- Testable
- Low coupling, high cohesion

---

# PART 1: FOUNDATION ARCHITECTURE OVERVIEW

## Purpose

The Foundation Architecture defines the core domain concepts that form the basis of Trexa. These concepts are:

1. **Engineering Independent** - Apply to any engineering domain
2. **Implementation Agnostic** - Not tied to specific technologies
3. **Minimal** - Only what reduces future rework

## Architecture Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE                          │
│  React Components, JointJS Visualization                   │
├─────────────────────────────────────────────────────────────┤
│                    APPLICATION                             │
│  Commands, Validation, Selection, State                    │
├─────────────────────────────────────────────────────────────┤
│                    DOMAIN                                   │
│  Document, EngineeringObjects, Symbols, Connections          │
├─────────────────────────────────────────────────────────────┤
│                    PLATFORM                                 │
│  Persistence, AI Integration, Extensions                    │
└─────────────────────────────────────────────────────────────┘
```

---

# PART 2: CORE ARCHITECTURAL CONCEPTS

## CONCEPT-001: Document

### Purpose

A Document is the root container for all engineering content in Trexa. It represents a complete engineering diagram or project.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Contain Content** | Holds all engineering objects |
| **Manage Hierarchy** | Maintains parent-child relationships |
| **Provide Bounds** | Defines canvas/workspace boundaries |
| **Own Metadata** | Contains document-level properties |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Engineering objects | User interface state |
| Document metadata | Undo/redo history |
| Layer references | Selection state |
| File format definition | Rendering data |

### Dependencies

```
Document
├── Layer[] (owns)
├── EngineeringObject[] (owns)
└── Metadata (owns)
```

### Ownership

**Document OWNS**:
- Layer creation and deletion
- Object insertion and removal
- Metadata management

**Document DOES NOT OWN**:
- Selection (owned by Selection Manager)
- History (owned by History Manager)
- Rendering (owned by JointJS)

### Why It Exists

Documents exist because engineering diagrams need a root container. Without a document concept, all objects would be floating without context.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| User interface state | Belongs to React components |
| Undo/redo | Belongs to History Manager |
| Selection | Belongs to Selection Manager |
| Rendering | Belongs to JointJS |

---

## CONCEPT-002: Layer

### Purpose

A Layer provides organizational grouping for engineering objects within a Document.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Group Objects** | Logical grouping |
| **Control Visibility** | Show/hide all objects |
| **Control Editability** | Lock/unlock all objects |
| **Z-Order** | Determine rendering order |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Object references | Object definitions |
| Layer properties | Document metadata |
| Visibility state | Selection state |
| Lock state | Rendering data |

### Dependencies

```
Layer
├── EngineeringObject[] (references)
└── Document (parent)
```

### Ownership

**Layer OWNS**:
- Object grouping
- Visibility state
- Lock state

**Layer DOES NOT OWN**:
- Object geometry (owned by object)
- Object properties (owned by object)
- Selection (owned by Selection Manager)

### Why It Exists

Layers exist because engineering diagrams need organizational structure. Different domains, voltage levels, or equipment types need separation.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Object geometry | Belongs to EngineeringObject |
| Object properties | Belongs to EngineeringObject |
| Selection | Belongs to Selection Manager |

---

## CONCEPT-003: EngineeringObject

### Purpose

An EngineeringObject is any drawable entity that can be placed on the diagram.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Define Identity** | Unique ID and type |
| **Hold Geometry** | Position, size, rotation |
| **Hold Properties** | Domain-specific attributes |
| **Define Connections** | Connection points |
| **Validate State** | Domain validation rules |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Unique identifier | Selection state |
| Geometry data | Rendering data |
| Properties | Position on canvas |
| Connection points | Layer reference |
| Domain type | Validation rules |

### Subtypes

| Subtype | Examples | Domain |
|---------|----------|--------|
| **Primitive** | CircuitBreaker, DisconnectSwitch, Busbar | SLD |
| **Composite** | Feeder, Bay | SLD |
| **Connection** | Conductor, Wire | All domains |
| **Annotation** | Label, TextBox | All domains |

### Dependencies

```
EngineeringObject
├── Geometry (owns)
├── Property[] (owns)
├── ConnectionPoint[] (owns)
├── Symbol (references)
└── Layer (parent reference)
```

### Ownership

**EngineeringObject OWNS**:
- Geometry data
- Properties
- Connection points
- Validation state

**EngineeringObject DOES NOT OWN**:
- Position (owned by Document via geometry)
- Selection (owned by Selection Manager)
- Rendering (owned by JointJS)
- Layer membership (owned by Layer)

### Why It Exists

EngineeringObjects exist because the domain requires entities that can be drawn, connected, and configured. The concept is abstract enough to cover all domains.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Rendering | Belongs to JointJS |
| Selection | Belongs to Selection Manager |
| Position logic | Belongs to Command pattern |

---

## CONCEPT-004: Symbol

### Purpose

A Symbol defines the visual representation and default properties for a type of EngineeringObject.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Define Visual** | SVG path, dimensions |
| **Default Properties** | Initial attribute values |
| **Domain Association** | Which domain uses it |
| **Connection Spec** | Connection point definitions |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Visual definition | Instance geometry |
| Default values | Instance properties |
| Domain association | Rendering data |
| Connection specs | Object state |

### Dependencies

```
Symbol
├── VisualDefinition (owns)
├── DefaultProperty[] (owns)
├── ConnectionPointSpec[] (owns)
└── Domain (references)
```

### Ownership

**Symbol OWNS**:
- Visual definition
- Default properties
- Connection specifications

**Symbol DOES NOT OWN**:
- Instance geometry (owned by EngineeringObject)
- Instance properties (owned by EngineeringObject)
- Instance state (owned by EngineeringObject)

### Why It Exists

Symbols exist because multiple objects of the same type share visual and default characteristics. Without Symbol, each object would redundantly define its own visuals.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Instance geometry | Belongs to EngineeringObject |
| Instance state | Belongs to EngineeringObject |
| Domain logic | Belongs to Domain Manager |

---

## CONCEPT-005: Connection

### Purpose

A Connection represents an electrical or logical relationship between two EngineeringObjects.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Link Objects** | Connect two objects |
| **Define Points** | Start and end points |
| **Define Routing** | Path between objects |
| **Define Type** | Electrical, logical, etc. |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Source reference | Source geometry |
| Target reference | Target geometry |
| Connection points | Rendering data |
| Routing data | Validation rules |

### Dependencies

```
Connection
├── SourceObject (references)
├── SourcePoint (references)
├── TargetObject (references)
├── TargetPoint (references)
├── RoutingData (owns)
└── ConnectionType (references)
```

### Ownership

**Connection OWNS**:
- Routing data
- Connection type
- Point references

**Connection DOES NOT OWN**:
- Object geometry (owned by EngineeringObject)
- Validation rules (owned by Validation Manager)
- Rendering (owned by JointJS)

### Why It Exists

Connections exist because engineering diagrams contain relationships between objects. Without Connection, objects would have implicit coupling.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Geometry | Belongs to objects |
| Routing algorithms | Belongs to JointJS |
| Validation | Belongs to Validation Manager |

---

## CONCEPT-006: Property

### Purpose

A Property is a named attribute of an EngineeringObject.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Store Value** | Hold property value |
| **Define Type** | String, number, enum, etc. |
| **Define Constraints** | Validation rules |
| **Provide Label** | Display name |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Name | Object geometry |
| Value | Object type |
| Type definition | Rendering |
| Constraints | Validation logic |

### Dependencies

```
Property
├── Name (owns)
├── Value (owns)
├── TypeDefinition (owns)
└── Constraint[] (owns)
```

### Ownership

**Property OWNS**:
- Value
- Type definition
- Constraints

**Property DOES NOT OWN**:
- Validation logic (belongs to Validation Manager)
- Rendering (belongs to JointJS)

### Why It Exists

Properties exist because engineering objects have configurable attributes. Without Property, objects would have hard-coded values.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Validation logic | Belongs to Validation Manager |
| Default values | Belongs to Symbol |
| UI representation | Belongs to React components |

---

## CONCEPT-007: Selection

### Purpose

Selection represents the current user selection state.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Track Selected** | Which objects are selected |
| **Track Mode** | Single, multi, etc. |
| **Provide Info** | Selection bounds, count |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Selected IDs | Object definitions |
| Selection mode | Document data |
| Selection bounds | Undo/redo |

### Why It Exists

Selection exists because users need to interact with objects. Without Selection, the system wouldn't know which objects the user is working on.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Object data | Belongs to Document |
| Undo/redo | Belongs to History Manager |
| Rendering | Belongs to JointJS |

---

## CONCEPT-008: Command

### Purpose

A Command represents a single user action that can be executed, undone, and redone.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Define Action** | What to do |
| **Provide Undo** | How to reverse |
| **Encapsulate State** | Before/after state |

### Command Types

| Type | Examples |
|------|----------|
| **Create** | AddObjectCommand |
| **Delete** | RemoveObjectCommand |
| **Modify** | MoveCommand, ResizeCommand, PropertyChangeCommand |
| **Transform** | RotateCommand |
| **Connect** | CreateConnectionCommand |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Execute logic | Object state (references) |
| Undo logic | History management |
| State delta | Validation logic |

### Dependencies

```
Command
├── Execute()
├── Undo()
└── State (references)
```

### Why It Exists

Commands exist because undo/redo requires encapsulating actions. Without Command, undo/redo would require storing entire document state.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| History management | Belongs to History Manager |
| Validation | Belongs to Validation Manager |
| Object state | Belongs to EngineeringObject |

---

## CONCEPT-009: Validation

### Purpose

Validation determines whether the document or objects satisfy domain rules.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Define Rules** | Domain-specific rules |
| **Check Objects** | Validate individual objects |
| **Check Topology** | Validate relationships |
| **Report Errors** | Return validation results |

### Validation Levels

| Level | Scope | Examples |
|-------|-------|----------|
| **Object** | Single object | Required properties, valid values |
| **Connection** | Two objects | Compatible connection points |
| **Topology** | Document | Voltage consistency, protection zones |
| **Safety** | Critical rules | Isolation before energizing |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Validation rules | Object definitions |
| Validation logic | User interface |
| Error reporting | Object modification |

### Why It Exists

Validation exists because engineering diagrams have rules. Without Validation, invalid diagrams could be created.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Object modification | Belongs to Commands |
| UI display | Belongs to React components |

---

## CONCEPT-010: AI Module Interface

### Purpose

The AI Module Interface defines how the frontend communicates with the AI routing system.

### Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Define Contract** | API between frontend and AI |
| **Manage Context** | Pass context to AI |
| **Handle Responses** | Process AI recommendations |
| **Track Telemetry** | Log AI decisions |

### Interface Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| API contract | AI implementation |
| Request/response types | AI routing logic |
| Telemetry interface | AI model training |

### Dependencies

```
AI Interface
├── Request (owns)
├── Response (owns)
├── Context (owns)
└── Telemetry (owns)
```

### Why It Exists

The AI Interface exists because AI and frontend are separate concerns. Without a clear interface, they would be tightly coupled.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| AI routing | Belongs to ai/ module |
| AI training | Belongs to ai/ module |
| Model definitions | Belongs to ai/ module |

---

## CONCEPT-011: Extension

### Purpose

An Extension provides a way to add custom functionality without modifying core code.

### Extension Points

| Point | Allows |
|-------|--------|
| **Symbols** | New symbol types |
| **Properties** | New property types |
| **Validation** | New validation rules |
| **Commands** | New commands |
| **Renderers** | New renderers |

### Boundaries

| INCLUDES | DOES NOT INCLUDE |
|----------|------------------|
| Extension definition | Core implementation |
| Extension points | Extension instances |
| Loading mechanism | UI integration |

### Why It Exists

Extensions exist because engineering domains evolve. Without Extension, adding new domains would require modifying core code.

### Why It Should NOT Include More

| Additional Responsibility | Why Excluded |
|--------------------------|--------------|
| Core functionality | Belongs to core |
| UI integration | Belongs to React |
| Rendering | Belongs to JointJS |

---

# PART 3: RESPONSIBILITY BOUNDARIES

## Technology Boundaries

### JointJS Boundary

```
JointJS OWNS:
├── SVG rendering
├── Viewport management
├── Zoom/pan
├── Connection routing
├── Shape definitions
└── Interaction events

JointJS DOES NOT OWN:
├── Document data
├── Object properties
├── Selection state
├── Validation rules
└── AI integration
```

### React Boundary

```
React OWNS:
├── UI components
├── User input handling
├── Property panels
├── Toolbars
└── State management (UI portion)

React DOES NOT OWN:
├── Document data (reference only)
├── Rendering (delegates to JointJS)
├── Object geometry
└── Validation logic
```

### AI Module Boundary

```
AI Module OWNS:
├── Profile selection
├── Task routing
├── IR processing
└── Telemetry

AI Module DOES NOT OWN:
├── User interface
├── Document state
├── Validation execution
└── Command execution
```

## State Ownership

| State | Owner | Observers |
|-------|-------|-----------|
| Document | Document | React, JointJS |
| Selection | Selection Manager | React, JointJS |
| History | History Manager | React |
| Validation | Validation Manager | React |
| AI Context | AI Module | React |

---

# PART 4: INTERACTION DIAGRAM

## Object Creation Flow

```
User Action
    │
    ▼
React Component
    │
    ▼
Command (CreateObjectCommand)
    │
    ├─▶ Validation Manager (validate)
    │
    ├─▶ Document (add object)
    │
    └─▶ History Manager (push command)
            │
            ▼
        JointJS (render)
```

## AI Integration Flow

```
User Request
    │
    ▼
React Component
    │
    ▼
AI Interface
    │
    ▼
ai/ Module
    │
    ├─▶ Profile Selection
    ├─▶ Task Classification
    └─▶ IR Processing
            │
            ▼
        AI Response
            │
            ▼
        React Component (display)
```

---

# PART 5: ARCHITECTURAL RISKS

| Risk | Severity | Mitigation |
|------|----------|------------|
| JointJS coupling too tight | MEDIUM | Clear boundaries, wrapper components |
| AI Module integration complex | MEDIUM | Simple interface, phased integration |
| Validation architecture unclear | LOW | Start simple, extend as needed |
| Extension points insufficient | MEDIUM | Design for extensibility from start |
| State management scattered | MEDIUM | Clear ownership model |

---

# PART 6: OPEN QUESTIONS

These questions require future investigation:

| Question | Why Open | Priority |
|----------|----------|----------|
| How to persist documents? | Need persistence investigation | HIGH |
| What is the file format? | Need format investigation | HIGH |
| How to structure React components? | Need component architecture | MEDIUM |
| How to test architecture? | Need testing strategy | MEDIUM |
| How to handle concurrent editing? | Future consideration | LOW |

---

# PART 7: CONFIDENCE ASSESSMENT

## Architecture Stability

| Concept | Confidence | Rationale |
|---------|------------|------------|
| Document | HIGH | Core concept, well-understood |
| EngineeringObject | HIGH | Based on TREXA-INV-006 |
| Symbol | MEDIUM | Needs validation against JointJS |
| Connection | HIGH | Based on TREXA-INV-006 |
| Property | HIGH | Standard pattern |
| Selection | MEDIUM | UI-specific, may evolve |
| Command | HIGH | Standard pattern |
| Validation | MEDIUM | Domain-specific, needs refinement |
| AI Interface | MEDIUM | New concept, needs validation |
| Extension | LOW | Speculative, may change |

## Overall Confidence: MEDIUM-HIGH (7/10)

---

# PART 8: RECOMMENDATION

## Foundation Architecture Summary

This investigation defines 10 core architectural concepts:

| Concept | Purpose | Confidence |
|---------|---------|-------------|
| Document | Root container | HIGH |
| Layer | Organization | HIGH |
| EngineeringObject | Drawable entity | HIGH |
| Symbol | Visual definition | MEDIUM |
| Connection | Relationship | HIGH |
| Property | Attribute | HIGH |
| Selection | User selection | MEDIUM |
| Command | Action/undo | HIGH |
| Validation | Rule checking | MEDIUM |
| AI Interface | AI integration | MEDIUM |

## Next Steps

After approval, these concepts should be validated against:

1. **JointJS**: How do these concepts map to JointJS?
2. **React**: How do these concepts map to React components?
3. **Implementation**: Can these concepts be implemented incrementally?

## What This Is NOT

| NOT This | Why |
|----------|-----|
| Database schema | Belongs to persistence investigation |
| API design | Belongs to API investigation |
| Component hierarchy | Belongs to component architecture |
| Class diagrams | Belongs to implementation |
| Folder structure | Belongs to project structure |

---

## Confidence

**Overall Confidence**: MEDIUM-HIGH (7/10)

The architecture is well-defined but requires validation through implementation.

---

**Investigation Status**: COMPLETE

**Awaits human review.**
