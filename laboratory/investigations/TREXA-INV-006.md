# Investigation: TREXA-INV-006

**ID**: TREXA-INV-006
**Title**: SLD Domain Definition for Trexa Platform
**Version**: 1.0.0
**Date**: 2026-07-23T11:00:00Z
**Status**: COMPLETE
**Author**: KDE Runtime (KDE-ENGINE-002 Beta)
**Seed**: SEED-001 (Genesis)

---

## Investigation Objective

Establish the authoritative SLD domain definition for Trexa.

This specification shall become the reference template for future engineering domains.

---

## Source Knowledge

This investigation synthesizes validated KDE knowledge:

| Source | Status | Content |
|--------|--------|---------|
| KDE-EXPERT-SLD-001 | APPROVED | SLD primitives, geometry, states |
| SLD Design Rules | VALIDATED | Symbol rules, colors, typography |
| SLD Symbols | VALIDATED | IEEE/IEC standards, symbol conventions |
| SLD Dynamics | VALIDATED | Real-time updates, animations |

---

# PART 1: PRIMITIVE CATALOG

## SLD-001: Circuit Breaker (CB)

**Engineering Purpose**: Primary protection and switching device that can interrupt fault currents.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-001 |
| **Name** | Circuit Breaker |
| **Category** | Switching Equipment |
| **IEEE Code** | Device Function Number applies to associated protection |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| equipment_id | string | YES | Unique identifier (e.g., "CB-101") |
| voltage_level | enum | YES | Voltage class (500kV, 230kV, 115kV, 69kV) |
| mva_rating | number | NO | MVA interrupting rating |
| bay_id | string | NO | Associated bay |

### Optional Properties

| Property | Type | Description |
|----------|------|-------------|
| manufacturer | string | Equipment manufacturer |
| model | string | Equipment model |
| year_installed | number | Installation year |

### States

| State | Visual Representation | Color |
|-------|---------------------|-------|
| CLOSED | Filled rectangle | Red (#ef4444) |
| OPEN | Outline rectangle | Green (#22c55e) |
| TRIPPED | Flashing filled | Red (#ef4444) at 0.5s |
| SELECTED | White outline | #FFFFFF |
| LOCKED | Gray fill | #888888 |
| UNKNOWN | Dashed outline | Cyan (#00FFFF) |

### State Transitions

```
CLOSED ←→ OPEN (via command)
    ↓
TRIPPED (via protection action)
    ↓
CLOSED (via reset + command)
    ↓
LOCKED (via permission)
```

### Visual Requirements

```
┌─────────────────────────────────────┐
│           Conductor                │
│              ║                     │
│             ∧∧    ← Double Chevron│
│             │ │      UP           │
│           ┌──────┐                 │
│           │██████│ ← Rectangle    │
│           │██████│   (state fill) │
│           └──────┘                 │
│             ∧∧    ← Double Chevron │
│             │ │      DOWN         │
│              ║                     │
│           Conductor                │
└─────────────────────────────────────┘

Dimensions:
- Body: 36×80px
- Chevrons: 8px wide, 2.5px stroke
- Conductors: 4px stroke, vertical
- Continuous line through chevrons
```

### Constraints

- Chevron orientation is fixed (not rotatable for SLD)
- Connection points at top and bottom conductors only
- Body fill color is state-dependent

---

## SLD-002: Disconnect Switch (DS)

**Engineering Purpose**: Isolates equipment for maintenance without interrupting fault current capability.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-002 |
| **Name** | Disconnect Switch (Isolator) |
| **Category** | Switching Equipment |
| **IEEE Code** | Device function number applies |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| equipment_id | string | YES | Unique identifier |
| voltage_level | enum | YES | Voltage class |
| interlocking_type | enum | NO | Type of interlocking |

### States

| State | Visual Representation | Color |
|-------|---------------------|-------|
| CLOSED | Knife vertical (0°) | Red (#ef4444) |
| OPEN | Knife rotated (40°) | Green (#44FF44) |
| UNKNOWN | No knife shown | Hidden |
| SELECTED | White outline | #FFFFFF |

### State Transitions

```
CLOSED → OPEN (via command)
OPEN → CLOSED (via command)
CLOSED ↔ OPEN (requires interlocking sequence)
```

### Visual Requirements

```
┌─────────────────────────────────────┐
│           Conductor                │
│              ║                     │
│     ────────●───────  ← Top Contact│
│              │                     │
│              │  ← Knife (0°/40°)   │
│              │                     │
│     ────────●───────  ← Bottom Cont│
│              ║                     │
│           Conductor                │
└─────────────────────────────────────┘

Elements:
- Conductors: 4px stroke, vertical
- Contacts: 3px stroke, horizontal, 115px wide
- Pivot: Circle at center-top contact, 6px radius
- Knife: 5px stroke, solid, round caps
```

### Constraints

- Knife rotates from 0° (closed) to 40° (open)
- Pivot point fixed at center-top contact
- ES is a branch device, does NOT interrupt main path

---

## SLD-003: Earthing Switch (ES)

**Engineering Purpose**: Provides deliberate ground connection for safety during maintenance.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-003 |
| **Name** | Earthing Switch |
| **Category** | Safety Equipment |
| **Connection Type** | Branch (does NOT interrupt main path) |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| equipment_id | string | YES | Unique identifier |
| voltage_level | enum | YES | Voltage class |

### States

| State | Visual Representation | Color |
|-------|---------------------|-------|
| CLOSED | Knife + ground symbol | Red (#ef4444) |
| OPEN | Knife rotated, no ground | Green (#44FF44) |
| UNKNOWN | No knife shown | Hidden |

### Visual Requirements

```
┌─────────────────────────────────────┐
│        Conductor / Bus             │
│              │                     │
│      ────────●───────  ← Top Contact│
│              │                     │
│              │  ← Knife (0°/40°)   │
│              │                     │
│              │  ← Down to Ground   │
│            ═════  ← Ground Symbol  │
└─────────────────────────────────────┘

Elements:
- Conductor: 4px stroke
- Contacts: 30px wide
- Ground: 3 horizontal bars, 3px stroke
```

### Constraints

- ES is ALWAYS a branch from main path
- ES does NOT interrupt electrical continuity
- Ground symbol required when CLOSED

---

## SLD-004: Busbar

**Engineering Purpose**: Collects and distributes electrical power within a substation.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-004 |
| **Name** | Busbar |
| **Category** | Conductors |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| section_id | string | YES | Bus section identifier |
| voltage_level | enum | YES | Voltage class |
| bus_name | string | YES | Bus designation (e.g., "115kV Bus A") |

### Optional Properties

| Property | Type | Description |
|----------|------|-------------|
| sections | number | Number of sections |
| grounding_type | enum | Grounding configuration |

### States

| State | Visual Representation | Color |
|-------|---------------------|-------|
| ENERGIZED | Solid line | Voltage color |
| DE-ENERGIZED | Solid line | Gray (#666666) |
| GROUNDED | Solid line | Black (#000000) |
| FAULT | Flashing | Red (#FF0000) |

### Visual Requirements

```
═══════════════════════════════════════════  115kV Bus A

Elements:
- Line: 6px stroke (thicker than conductors)
- Color: Based on voltage level
- Label: Voltage + Bus Name
```

### Voltage Colors

| Voltage | Color | Hex |
|---------|-------|-----|
| 500 kV | Blue | #0000FF |
| 230 kV | Red | #FF0000 |
| 115 kV | Yellow-Orange | #FFBF00 |
| 69 kV | Cyan | #00FFFF |

### Constraints

- Always horizontal orientation
- Cannot have connection points on sides
- Sections shown as gaps with switching devices

---

## SLD-005: Transformer (Two-Winding)

**Engineering Purpose**: Transfers energy between voltage levels.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-005 |
| **Name** | Two-Winding Transformer |
| **Category** | Power Equipment |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| equipment_id | string | YES | Unique identifier |
| primary_voltage | enum | YES | Primary voltage level |
| secondary_voltage | enum | YES | Secondary voltage level |
| mva_rating | number | YES | MVA capacity |
| vector_group | string | NO | Connection configuration |

### Optional Properties

| Property | Type | Description |
|----------|------|-------------|
| impedance | number | Percent impedance |
| tap_position | number | Current tap position |
| cooling_type | enum | Cooling method |

### States

| State | Visual Representation | Symbol Lines |
|-------|---------------------|--------------|
| ENERGIZED | Filled lines | Solid |
| DE-ENERGIZED | Hollow lines | Outline |
| LOADED | Filled + values | MW/MVAR shown |

### Visual Requirements

```
     115kV
────|   |────  [T1]  34.5kV
────| 2W |────   50 MVA
────|   |────   DYn11
```

### Constraints

- Primary and secondary may use different voltage colors
- Label shows primary voltage above, secondary below

---

## SLD-006: Line/Conductor

**Engineering Purpose**: Transmits power between substations or to loads.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-006 |
| **Name** | Transmission/Distribution Line |
| **Category** | Conductors |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| line_id | string | YES | Unique identifier |
| voltage_level | enum | YES | Operating voltage |
| length | number | NO | Line length |

### Optional Properties

| Property | Type | Description |
|----------|------|-------------|
| mw_value | number | Current MW flow |
| mvar_value | number | Current MVAR flow |
| impedance | number | Line impedance |
| owner | string | Operating utility |

### States

| State | Visual Representation | Color |
|-------|---------------------|-------|
| ENERGIZED | Solid with values | Voltage color |
| DE-ENERGIZED | Solid | Gray (#666666) |
| FAULT | Flashing | Red (#FF0000) |

### Visual Requirements

```
────────────────────  [L1]  115kV  12.5 mi
                        ↓ MW: 45.2
```

### Constraints

- Flow direction shown with arrows
- MW/MVAR values displayed inline
- Single-line representation only

---

## SLD-007: Current Transformer (CT)

**Engineering Purpose**: Measures current for protection and metering.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-007 |
| **Name** | Current Transformer |
| **Category** | Instrumentation |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| equipment_id | string | YES | Unique identifier |
| ratio | string | YES | CT ratio (e.g., "1200:5") |

### Visual Requirements

```
─────○─────
    (CT)
```

### Constraints

- Usually embedded in breaker representation
- Label shows ratio

---

## SLD-008: Potential Transformer (PT)

**Engineering Purpose**: Measures voltage for protection and metering.

### Primitive Specification

| Attribute | Value |
|-----------|-------|
| **ID** | SLD-008 |
| **Name** | Potential Transformer |
| **Category** | Instrumentation |

### Required Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| equipment_id | string | YES | Unique identifier |
| ratio | string | YES | PT ratio |

### Visual Requirements

```
─────○─────
    (PT)
```

### Constraints

- Usually shown at bus entrance
- Indicates voltage measurement point

---

# PART 2: CONNECTION MODEL

## Connection Points Specification

### CB (SLD-001) Connection Points

| Point ID | Position | Type | Allowed Connections |
|----------|----------|------|-------------------|
| CB-TOP | Top | ELECTRICAL | Busbar, Line, Transformer |
| CB-BOTTOM | Bottom | ELECTRICAL | Busbar, Line, Transformer |

### DS (SLD-002) Connection Points

| Point ID | Position | Type | Allowed Connections |
|----------|----------|------|-------------------|
| DS-TOP | Top | ELECTRICAL | Busbar, Line, Transformer, CB |
| DS-BOTTOM | Bottom | ELECTRICAL | Busbar, Line, Transformer, CB |

### ES (SLD-003) Connection Points

| Point ID | Position | Type | Allowed Connections |
|----------|----------|------|-------------------|
| ES-TOP | Top | ELECTRICAL | Busbar, Line, Transformer, CB, DS |
| ES-BOTTOM | Bottom | GROUND | Ground reference |

### Busbar (SLD-004) Connection Points

| Point ID | Position | Type | Allowed Connections |
|----------|----------|------|-------------------|
| BUS-LEFT | Left | ELECTRICAL | Any equipment at same voltage |
| BUS-RIGHT | Right | ELECTRICAL | Any equipment at same voltage |

### Transformer (SLD-005) Connection Points

| Point ID | Position | Type | Allowed Connections |
|----------|----------|------|-------------------|
| XFMR-PRIMARY | Left | ELECTRICAL | Higher voltage bus/line |
| XFMR-SECONDARY | Right | ELECTRICAL | Lower voltage bus/line |

### Line (SLD-006) Connection Points

| Point ID | Position | Type | Allowed Connections |
|----------|----------|------|-------------------|
| LINE-START | Start | ELECTRICAL | Any equipment |
| LINE-END | End | ELECTRICAL | Any equipment |

---

## Connection Types

| Type | Description | Symbol |
|------|-------------|--------|
| ELECTRICAL | Conducting path | Solid line |
| CONTROL | Control wiring | Dashed line |
| GROUND | Ground reference | Ground symbol |

---

## Connection Constraints

### Electrical Connectivity Rules

1. **Voltage Consistency**: Connected equipment should have compatible voltage levels
2. **Impedance Path**: CB or DS must be open to isolate equipment
3. **Ground Reference**: ES connects to ground reference

### Forbidden Connections

| From | To | Reason |
|------|-----|--------|
| Busbar | Ground | Busbar is main conductor |
| Transformer Primary | Transformer Secondary | Must go through transformation |
| Different voltage levels | Direct | Requires transformer |

---

# PART 3: RELATIONSHIP MODEL

## Relationship Types

### R-001: Electrical Connectivity

**Description**: Represents conducting path between equipment.

| Attribute | Value |
|-----------|-------|
| Type | CONDUCTS |
| Direction | Bidirectional |
| Semantic | Power can flow in either direction |
| Visual | Solid conductor line |

### R-002: Containment

**Description**: Equipment is physically located within a substation/bay.

| Attribute | Value |
|-----------|-------|
| Type | CONTAINED_BY |
| Direction | Unidirectional |
| Semantic | Equipment belongs to substation |
| Visual | Spatial grouping |

### R-003: Protection

**Description**: CB protects downstream equipment.

| Attribute | Value |
|-----------|-------|
| Type | PROTECTS |
| Direction | CB → Protected equipment |
| Semantic | CB trip clears faults downstream |
| Visual | Protection zone indicator |

### R-004: Isolation

**Description**: DS/ES provides isolation capability.

| Attribute | Value |
|-----------|-------|
| Type | CAN_ISOLATE |
| Direction | DS/ES → Equipment |
| Semantic | Switch can isolate equipment |
| Visual | Isolation zone indicator |

### R-005: Measurement

**Description**: CT/PT measures electrical quantities.

| Attribute | Value |
|-----------|-------|
| Type | MEASURES |
| Direction | Instrument → Measured equipment |
| Semantic | Provides metering/protection signals |
| Visual | Instrument symbol |

---

# PART 4: STATE DEFINITIONS

## State Machine Summary

### CB (SLD-001) State Machine

```
        ┌──────────────────────────────────────┐
        │                                      │
        ▼                                      │
    ┌───────┐     command      ┌───────┐     │
    │CLOSED│ ───────────────▶ │ OPEN  │     │
    └───┬───┘                  └───┬───┘     │
        │                         │          │
        │ protection              │ command  │
        │ action                  │          │
        ▼                         │          │
    ┌────────┐                   │          │
    │TRIPPED │ ◀─────────────────┘          │
    └───┬────┘                             │
        │                                  │
        │ reset +                         │
        │ command                          │
        ▼                                  │
    ┌────────┐                            │
    │LOCKED  │─────────────────────────────┘
    └────────┘        unlock
```

### DS (SLD-002) State Machine

```
    ┌───────┐     command      ┌───────┐
    │CLOSED│ ───────────────▶ │ OPEN  │
    └───┬───┘                  └───┬───┘
        │                         │
        │◀────────────────────────┘
        │    interlocking sequence
```

### ES (SLD-003) State Machine

```
    ┌───────┐     command      ┌───────┐
    │CLOSED│ ───────────────▶ │ OPEN  │
    └───┬───┘                  └───┬───┘
        │                         │
        │◀────────────────────────┘
        │    safety sequence
```

---

## State Visualization Matrix

| Primitive | CLOSED | OPEN | TRIPPED | UNKNOWN |
|-----------|--------|------|---------|---------|
| CB | Red fill | Green outline | Red flash | Dashed |
| DS | Red knife 0° | Green knife 40° | N/A | Hidden |
| ES | Red knife + ground | Green knife | N/A | Hidden |
| Busbar | Voltage color | Gray | Red flash | Gray |
| Transformer | Filled lines | Hollow lines | N/A | Gray |
| Line | Voltage color | Gray | Red flash | Gray |

---

# PART 5: VALIDATION RULES

## V-001: Connectivity Validation

**Rule**: All equipment must connect to at least one other element.

**Severity**: ERROR
**Check**: Every primitive except ground must have at least one connection.

## V-002: Voltage Consistency

**Rule**: Connected equipment should have compatible voltage levels.

**Severity**: WARNING
**Check**: Equipment connected to same bus should share voltage level.

## V-003: Feeder Pattern

**Rule**: Feeder must follow DS-CB-ES-DS pattern.

**Pattern**: ```
BUS ── DS_TOP ── CB ── ES ── DS_BOTTOM ── LINE
```

**Severity**: ERROR
**Check**: If ES present in feeder, must have DS on both sides.

## V-004: Ground Connection

**Rule**: ES must have ground connection point connected.

**Severity**: ERROR
**Check**: ES bottom connection must connect to ground reference.

## V-005: Busbar Continuity

**Rule**: Busbar sections require switching devices at gaps.

**Severity**: WARNING
**Check**: Busbar gaps should have CB or DS for sectioning.

## V-006: Transformer Connection

**Rule**: Transformer must connect primary and secondary voltage levels.

**Severity**: ERROR
**Check**: Primary and secondary must not connect to same voltage level.

## V-007: Isolation Coordination

**Rule**: Upstream switch must be open before downstream.

**Severity**: WARNING
**Check**: DS upstream of CB should be open if CB is open.

## V-008: Label Completeness

**Rule**: Equipment must have required labels.

**Severity**: WARNING
**Check**: All equipment must have equipment_id.

---

# PART 6: RENDERING REQUIREMENTS

## RR-001: Stroke Styles

| Element | Stroke Width | Style | Cap |
|---------|-------------|-------|-----|
| Conductors | 4px | Solid | Butt |
| Busbar | 6px | Solid | Butt |
| Contacts | 3px | Solid | Round |
| Ground bars | 3px | Solid | Butt |
| Chevrons | 2.5px | Solid | Round |
| Knife blades | 5px | Solid | Round |
| Pivot circles | 2px | No fill | N/A |

## RR-002: Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Equipment ID | Sans-serif | 12px | Bold |
| Voltage Label | Sans-serif | 10px | Regular |
| Values (MW/MVAR) | Monospace | 12px | Regular |
| Bus Name | Sans-serif | 14px | Bold |

## RR-003: Animation

| Animation | Duration | Trigger |
|-----------|----------|---------|
| State change | 200ms | On state update |
| Value update | 100ms | On value change |
| Alarm flash | 500ms-2s | Until acknowledged |
| Zoom | 300ms | On zoom action |

## RR-004: Color Palette

| Purpose | Light Mode | Dark Mode |
|---------|------------|-----------|
| Background | #F0F0F0 | #1A1A1A |
| Text | #000000 | #FFFFFF |
| Selection | #FFFFFF outline | #FFFFFF outline |
| Highlight | #00FFFF | #00FFFF |

---

# PART 7: ASSUMPTIONS

| ID | Assumption | Confidence |
|----|-----------|------------|
| A-001 | NGCP voltage color profile applies | HIGH |
| A-002 | IEEE C37.2 device numbering convention | HIGH |
| A-003 | IEC 61850 naming applies | MEDIUM |
| A-004 | Web-based SVG rendering | HIGH |
| A-005 | Single-line representation only | HIGH |
| A-006 | Horizontal busbar orientation | HIGH |

---

# PART 8: RISKS

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R-001 | Symbol standard variation | MEDIUM | Support both IEEE and IEC |
| R-002 | Color-blind accessibility | MEDIUM | Add shape differentiation |
| R-003 | Real-time update latency | HIGH | Design for WebSocket updates |
| R-004 | Large diagram performance | MEDIUM | Implement viewport culling |

---

# PART 9: KNOWLEDGE GAPS

| ID | Gap | Priority | Source |
|----|-----|----------|--------|
| G-001 | Three-winding transformer | MEDIUM | Future |
| G-002 | Auto-transformer | MEDIUM | Future |
| G-003 | Protection relay symbols | LOW | Future |
| G-004 | Capacitor/Reactor banks | LOW | Future |
| G-005 | Generator symbols | LOW | Future |

---

# CONCLUSION

**Status**: SLD Domain Sufficiently Defined

## Deliverables Completed

| Deliverable | Status |
|------------|--------|
| Primitive Catalog (8 primitives) | ✅ Complete |
| Primitive Specifications | ✅ Complete |
| Connection Point Definitions | ✅ Complete |
| Relationship Definitions | ✅ Complete |
| State Definitions | ✅ Complete |
| Validation Rule Catalog (8 rules) | ✅ Complete |
| Rendering Requirement Specification | ✅ Complete |
| Assumptions | ✅ Complete |
| Risks | ✅ Complete |
| Knowledge Gaps | ✅ Complete |

---

## Recommended Next Investigation

**TREXA-INV-007**: SLD Domain Integration

Validate that the 34 platform capabilities (from TREXA-INV-002) can implement the SLD domain specification.

---

**Investigation Status**: COMPLETE
**Confidence**: HIGH

**Awaiting human review.**
