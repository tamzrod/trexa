# Investigation Analysis: TREXA-INV-031A

**Investigation**: TREXA-INV-031A
**Title**: UX Architecture Clarification — Module-Agnostic Workspace
**Status**: IN_PROGRESS

---

# PART 1: ARCHITECTURE CLARIFICATION

## 1.1 Current Terminology Analysis

### Current Expression (TREXA-INV-031)

```
┌─────────────────────────────────────────────────────────────────┐
│ Menu Bar                                                          │
├────┬────────────────────────────────────────┬───────────────────┤
│ A  │                                        │ Properties        │
│ C  │                                        │                   │
│ T  │            CANVAS                       │ Layers            │
│ I  │         (JointJS)                      │                   │
│ V  │                                        │ Validation        │
│ I  │  [Activity Toolbar]                    │                   │
│ T  │                                        │                   │
├────┴────────────────────────────────────────┴───────────────────┤
│ Status Bar                                                        │
└─────────────────────────────────────────────────────────────────┘
```

### Issue Identified

| Term | Issue |
|------|-------|
| "Canvas" | Implies 2D drawing surface |
| "(JointJS)" | Technology-specific reference |

**Impact**: Creates mental model that all engineering is diagram-based.

## 1.2 Module Spectrum Analysis

### Engineering Modules in Trexa

| Module | Visualization | Rendering | Navigation |
|--------|--------------|-----------|------------|
| SLD | Diagram | JointJS | Pan/zoom |
| P&ID | Diagram | JointJS | Pan/zoom |
| GIS | Map | Leaflet/Mapbox | Pan/zoom/rotate |
| SCADA | Mimic | Custom | Pan/zoom |
| Protection | Coordination Curve | Chart.js | Time-based |
| Report | Document | PDF/HTML | Scroll |
| Simulation | Data Grid | Custom | Sort/filter |
| Asset Explorer | Tree/Grid | Custom | Navigate |

### Finding

**Not all modules are canvas-based.** The term "Canvas (JointJS)" does not accurately describe all engineering modules.

---

# PART 2: MODULE-AGNOSTIC TERMINOLOGY

## 2.1 Alternative Terminology

| Alternative | Description | Assessment |
|------------|-------------|------------|
| **Active Engineering Module** | The currently active module workspace | RECOMMENDED |
| **Engineering Workspace** | General workspace area | Good |
| **Module View** | Current module's view | Good |
| **Central Area** | Neutral term | Too vague |

## 2.2 Recommended Terminology

**Primary Term**: Active Engineering Module

**Rationale**:
1. **Accurate**: Represents whatever module is active
2. **Neutral**: No assumptions about visualization type
3. **Extensible**: Future modules fit naturally
4. **Consistent**: Matches "Module Navigation" concept

## 2.3 Module Context Statement

**PRINCIPLE**: The central workspace represents the currently active engineering module.

The module itself determines:
- Visualization type (diagram, map, chart, document)
- Rendering technology (JointJS, Leaflet, Chart.js, Custom)
- Interaction model (pan/zoom, scroll, navigate)
- Module-specific toolbar

---

# PART 3: UPDATED CONCEPTUAL LAYOUT

## 3.1 Module-Agnostic Expression

```
┌─────────────────────────────────────────────────────────────────┐
│ Menu Bar                                                          │
├────┬────────────────────────────────────────┬───────────────────┤
│ A  │                                        │ Properties        │
│ C  │                                        │                   │
│ T  │                                        │ Layers            │
│ I  │       ACTIVE ENGINEERING MODULE        │                   │
│ V  │                                        │ Validation        │
│ I  │   (SLD / GIS / P&ID / SCADA / ...)    │                   │
│ T  │                                        │                   │
│    │      [Module-Specific Toolbar]         │                   │
├────┴────────────────────────────────────────┴───────────────────┤
│ Status Bar (shows current domain/module)                         │
└─────────────────────────────────────────────────────────────────┘
```

## 3.2 Module-Specific Elements

### Activity Bar (Context-Sensitive)

| Active Module | Activity Bar Content |
|---------------|---------------------|
| SLD | Symbol palette, drawing tools |
| GIS | Layer controls, map tools |
| P&ID | Instrument library, line types |
| SCADA | Symbol library, real-time data |
| Protection | Relay settings, curve tools |
| Report | Template gallery, export options |

### Module Toolbar (Context-Sensitive)

| Active Module | Toolbar Content |
|---------------|----------------|
| SLD | Draw, Connect, Label, Rotate |
| GIS | Pan, Zoom, Measure, Query |
| P&ID | Draw, Connect, Tag, Annotate |
| SCADA | Configure, Monitor, Alarm |
| Protection | Select, Move, Zoom, Time |
| Report | Edit, Format, Preview |

---

# PART 4: PLATFORM CONSISTENCY ASSESSMENT

## 4.1 Consistent Elements

These elements remain **constant** regardless of active module:

| Element | Behavior | Rationale |
|---------|----------|-----------|
| **Menu Bar** | Static | Platform-level actions |
| **Activity Bar** | Context-sensitive | Adapts to module |
| **Explorer** | Static | Project navigation |
| **Properties Panel** | Context-sensitive | Shows selected object |
| **Layers Panel** | Module-specific | Layers vary by module |
| **Validation Panel** | Module-specific | Rules vary by domain |
| **Status Bar** | Context-sensitive | Shows module info |
| **Command Palette** | Static | All commands available |
| **Docking System** | Static | Panel behavior unchanged |

## 4.2 Variable Elements

These elements change based on **active module**:

| Element | Variation | Rationale |
|---------|-----------|-----------|
| **Central Workspace** | Module-specific | Diagram, map, chart, etc. |
| **Module Toolbar** | Module-specific | Domain tools |
| **Activity Content** | Module-specific | Symbol palettes |
| **Status Content** | Module-specific | Domain indicators |

## 4.3 Assessment

**Finding**: The surrounding application shell (panels, navigation, docking) is **module-agnostic**. Only the central workspace is module-specific.

---

# PART 5: UX ARCHITECTURE STATEMENT UPDATE

## 5.1 Updated Statement

**Original (TREXA-INV-031)**:

> The central workspace is the JointJS canvas where engineering diagrams are edited.

**Updated**:

> The central workspace is the **Active Engineering Module**. This module determines the visualization type (diagram, map, chart, document) and provides module-specific tools. The surrounding application shell remains consistent across all modules.

## 5.2 Module-Agnostic Workspace Principle

**PRINCIPLE**: Trexa's UX architecture defines the application shell as module-agnostic. Only the central workspace is module-specific.

| Layer | Module-Agnostic | Description |
|-------|----------------|-------------|
| **Application Shell** | YES | Menu, Activity Bar, Explorer, Properties, Docking |
| **Central Workspace** | NO | Determined by active module |
| **Module Toolbar** | NO | Provided by active module |
| **Panel Content** | PARTIAL | Some panels adapt to module |

---

# PART 6: TERMINOLOGY COMPARISON

## 6.1 Canvas vs Active Engineering Module

| Criterion | Canvas (JointJS) | Active Engineering Module |
|-----------|-----------------|--------------------------|
| **Accuracy** | Partial | Accurate |
| **SLD focus** | High | Neutral |
| **GIS fit** | Poor | Good |
| **P&ID fit** | Good | Good |
| **SCADA fit** | Poor | Good |
| **Extensibility** | Limited | Unlimited |
| **Mental model** | Diagram-centric | Module-centric |

## 6.2 Recommendation

**Replace**: "Canvas (JointJS)"

**With**: "Active Engineering Module"

**Supplementary**: "(Diagram / Map / Chart / Document / ...)" for context

---

# PART 7: IMPACT ANALYSIS

## 7.1 Documentation Updates

| Document | Update Required | Scope |
|----------|----------------|-------|
| TREXA-INV-031 CONCLUSION | Minor | Terminology only |
| TDR-016 (UX Architecture) | Minor | Terminology only |
| TDR-017 (Navigation System) | None | Already correct |

## 7.2 Architecture Impact

| Aspect | Impact | Rationale |
|--------|--------|-----------|
| Approved decisions | None | Terminology clarification only |
| Implementation | None | Same behavior |
| Future modules | Positive | Clear integration path |

## 7.3 Recommendation: Clarification Only

**Decision**: This is a terminology clarification, not an architecture change.

- TREXA-INV-031 decisions remain valid
- Only terminology changes
- No implementation changes required
- Documentation update recommended

---

**Analysis Status**: IN_PROGRESS

**Next**: Complete CONCLUSION.md
