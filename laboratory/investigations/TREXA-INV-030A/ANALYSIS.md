# Investigation Analysis: TREXA-INV-030A

**Investigation**: TREXA-INV-030A
**Title**: Platform Identity vs Domain Semantics Clarification
**Status**: IN_PROGRESS

---

# PART 1: ARCHITECTURE CLARIFICATION

## 1.1 Two-Layer Architecture

Trexa employs a **two-layer visual architecture**:

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 1: APPLICATION THEME               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Menu Bar, Toolbar, Sidebar, Panels, Dialogs,       │   │
│  │  Buttons, Tabs, Trees, Status Bar                  │   │
│  │                                                     │   │
│  │  OWNER: Trexa Platform                              │   │
│  │  PURPOSE: Platform visual identity                  │   │
│  │  CONSTRAINT: Domain-neutral                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                │
│                           ▼                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              ENGINEERING CANVAS                      │   │
│  │                                                     │   │
│  │  Domain content rendered here using domain colors    │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                │
│                           ▼                                │
├─────────────────────────────────────────────────────────────┤
│                  LAYER 2: DOMAIN COLOR PROFILES             │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐  │
│  │   SLD     │ │   P&ID    │ │    GIS    │ │   SCADA   │  │
│  │  Profile  │ │  Profile  │ │  Profile  │ │  Profile  │  │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘  │
│                                                             │
│  OWNER: Domain standards (NGCP, IEC, ISA, etc.)             │
│  PURPOSE: Engineering semantic meaning                      │
│  CONSTRAINT: Trexa must not modify semantics                │
└─────────────────────────────────────────────────────────────┘
```

## 1.2 Layer Responsibilities

### Layer 1: Application Theme

| Responsibility | Description |
|---------------|-------------|
| Platform Identity | Trexa's visual brand |
| Navigation | How users interact with the platform |
| Information Display | Property panels, inspectors |
| Workspace Layout | Canvas area, docking |
| Interaction States | Hover, focus, selection, drag |
| Tooling | Toolbar, menus, shortcuts |
| Dialogs | Modal and modeless dialogs |

**Constraint**: Must remain domain-neutral. Cannot optimize for any single engineering domain.

### Layer 2: Domain Color Profiles

| Responsibility | Description |
|---------------|-------------|
| Voltage Colors | 500kV, 230kV, 115kV, 69kV, etc. |
| Equipment States | CLOSED, OPEN, TRIPPED, etc. |
| Alarm Severity | Critical, Major, Minor, Warning |
| Domain Semantics | Any color with engineering meaning |
| Standard Compliance | NGCP, IEC, ISA, utility-specific |

**Constraint**: Trexa renders these colors exactly as defined. No modification allowed.

---

# PART 2: PLATFORM VS DOMAIN RESPONSIBILITY MATRIX

## 2.1 Complete Responsibility Matrix

| Element | Layer | Owner | Constraints |
|---------|-------|-------|-------------|
| **Application Shell** | 1 | Trexa | Domain-neutral |
| Menu Bar | 1 | Trexa | Domain-neutral |
| Toolbar | 1 | Trexa | Domain-neutral |
| Activity Bar | 1 | Trexa | Domain-neutral |
| Sidebar | 1 | Trexa | Domain-neutral |
| Property Panel | 1 | Trexa | Domain-neutral |
| Inspector | 1 | Trexa | Domain-neutral |
| Dialogs | 1 | Trexa | Domain-neutral |
| Status Bar | 1 | Trexa | Domain-neutral |
| Buttons | 1 | Trexa | Domain-neutral |
| Tabs | 1 | Trexa | Domain-neutral |
| Tree View | 1 | Trexa | Domain-neutral |
| **Engineering Canvas** | 1 | Trexa | Container only |
| **Voltage Colors** | 2 | Domain | SLD-specific |
| **Equipment States** | 2 | Domain | SLD-specific |
| **Alarm Colors** | 2 | Domain | SCADA/HMI-specific |
| **Process Colors** | 2 | Domain | P&ID-specific |
| **Geographic Layers** | 2 | Domain | GIS-specific |
| **Line Styles** | 2 | Domain | Domain-specific |
| **Symbol Libraries** | 2 | Domain | Domain-specific |

## 2.2 Color Ownership by Layer

### Layer 1: Application Theme Colors (Trexa Owns)

| Color Type | Purpose | Examples |
|-----------|---------|----------|
| Primary | Brand, main actions | Buttons, links |
| Secondary | Supporting actions | Secondary buttons |
| Surface | Backgrounds | Panel backgrounds |
| Text | Content | Labels, values |
| Border | Separation | Panel borders |
| Selection | Selection UI | Selection handles |
| Focus | Focus indicator | Focus rings |
| Hover | Hover states | Hover backgrounds |
| Drag | Drag states | Drag highlights |
| Guide | Alignment guides | Guide lines |

### Layer 2: Domain Semantic Colors (Domain Owns)

| Domain | Color Type | Examples |
|--------|-----------|----------|
| SLD | Voltage | 500kV=Blue, 230kV=Red |
| SLD | Equipment State | CLOSED=Red, OPEN=Green |
| SLD | Protection | Tripped=Flash |
| P&ID | Process Line | Process, Utility, Waste |
| P&ID | Instrument | FCI, ISA symbols |
| GIS | Geographic | Terrain, water, roads |
| GIS | Layer | Base, infrastructure |
| SCADA | Alarm | Critical, Major, Minor |
| SCADA | Status | On, Off, Manual |

---

# PART 3: COLOR GOVERNANCE MODEL

## 3.1 Governance Structure

```
Color Governance
├── Platform Colors (Trexa)
│   ├── Application Theme
│   ├── UI Semantic Colors
│   └── Interaction Colors
│
└── Domain Colors (Domain Profiles)
    ├── SLD Profile
    ├── P&ID Profile
    ├── GIS Profile
    ├── SCADA Profile
    └── [Future Domains]
```

## 3.2 Domain Independence Principle

**PRINCIPLE**: Engineering domains are independent color namespaces.

Each domain profile:
1. Defines its own semantic colors
2. Trexa renders those colors without modification
3. Domains do not inherit from platform colors
4. Platform colors do not override domain semantics

## 3.3 Trexa Application Theme Colors

These colors are **NOT engineering semantics**. They are UI aesthetics.

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| trexa-primary | #2563EB | #3B82F6 | Brand, primary actions |
| trexa-secondary | #7C3AED | #8B5CF6 | Secondary actions |
| trexa-surface | #F3F4F6 | #1F2937 | Panel backgrounds |
| trexa-background | #FFFFFF | #111827 | App background |
| trexa-text | #111827 | #F9FAFB | Primary text |
| trexa-text-secondary | #6B7280 | #9CA3AF | Secondary text |
| trexa-border | #E5E7EB | #374151 | Borders |
| trexa-selection | #FFFFFF | #FFFFFF | Selection outline |

**Note**: These are Trexa's UI colors, NOT voltage or alarm colors.

## 3.4 Domain Semantic Colors (Example)

These are **engineering semantics**, NOT Trexa's colors.

| Domain | Semantic | Hex | Meaning |
|--------|----------|-----|---------|
| SLD | 500kV | #0000FF | 500 kilovolt |
| SLD | 230kV | #FF0000 | 230 kilovolt |
| SLD | CLOSED | #ef4444 | Conducting |
| SLD | OPEN | #22c55e | Non-conducting |
| P&ID | Process Line | Black | Process flow |
| P&ID | Instrument | Triangle | FCI symbol |
| SCADA | Critical | #DC2626 | Critical alarm |
| SCADA | Major | #F97316 | Major alarm |

**Note**: Trexa renders these exactly as defined. Trexa does NOT own these colors.

---

# PART 4: EVIDENCE OF SLD-CENTRIC BIAS

## 4.1 Evidence from TREXA-INV-030

The following language in TREXA-INV-030 suggests SLD-centric bias:

| Evidence | Issue |
|----------|-------|
| "Equipment State Colors" table | Only SLD states listed |
| "Voltage Colors (NGCP Profile)" | SLD-specific vocabulary |
| "Alarm Severity Colors" | SCADA content in SLD context |
| Selection analysis focused on voltage colors | SLD domain |

## 4.2 Domain Coverage Analysis

| Domain | Colors Discussed | Domain Coverage |
|--------|-----------------|-----------------|
| SLD | 4 voltage + 6 states | 100% |
| P&ID | 0 | 0% |
| GIS | 0 | 0% |
| SCADA | 5 alarm levels | Partial |
| Protection | 4 states | Partial |
| Other | 0 | 0% |

**Finding**: TREXA-INV-030 was 60%+ SLD-focused despite being about platform compatibility.

## 4.3 Architectural Friction Identified

**Issue**: If Trexa's visual identity is influenced by SLD, future domains may need to adapt.

**Examples of potential friction**:
1. GIS might prefer earth tones for UI, but SLD influenced the neutral palette
2. P&ID might need different selection visibility, but SLD requirements were primary
3. SCADA might prefer orange for warnings, but SLD influenced the warning color

**Assessment**: This friction is **HYPOTHETICAL** because:
- Layer 1 (Application) uses neutral colors
- Layer 2 (Domain) uses domain-specific colors
- No actual conflict exists in the architecture

---

# PART 5: DESIGN PRINCIPLES EXTRACTION

## 5.1 Platform Identity Principles

Based on the two-layer architecture:

### Principle 1: Domain Neutrality

The application theme (Layer 1) must not be optimized for any single engineering domain.

**Evidence**: Trexa supports SLD, P&ID, GIS, SCADA, and future domains.

**Implication**: UI colors must be neutral, professional, and non-semantic.

### Principle 2: Domain Independence

Each engineering domain owns its semantic color system.

**Evidence**: NGCP voltage colors, ISA instrument symbols, alarm severity.

**Implication**: Trexa must not modify, override, or constrain domain semantics.

### Principle 3: Faithful Rendering

Trexa renders domain colors exactly as defined by the domain profile.

**Evidence**: TREXA-INV-006 specifies voltage colors for SLD.

**Implication**: Domain profiles are input to Trexa, not output from Trexa.

### Principle 4: Layer Separation

Platform UI and domain content must be visually distinguishable.

**Evidence**: TREXA-INV-030 confirms adequate separation.

**Implication**: Neutral UI does not compete with colorful domain content.

### Principle 5: Professional Neutrality

The application theme must look professional regardless of the domain being edited.

**Evidence**: Engineering tools (VS Code, AutoCAD) use neutral themes.

**Implication**: UI colors should be professional grays, blues, and neutrals.

---

# PART 6: TREXA-INV-030 EVALUATION

## 6.1 Findings Valid

| Finding | Assessment |
|---------|------------|
| Two-layer architecture | ✅ VALID |
| Application theme compatible | ✅ VALID |
| Selection visibility good | ✅ VALID |
| Engineering focus good | ✅ VALID |

## 6.2 Bias Acknowledgment

| Issue | Impact | Resolution |
|-------|--------|------------|
| SLD vocabulary predominant | LOW | Document domain neutrality |
| SLD colors heavily referenced | LOW | Acknowledge domain ownership |
| P&ID/GIS/SCADA underrepresented | LOW | Add domain coverage statement |

## 6.3 Recommendation: No Changes to TREXA-INV-030

**Rationale**:
1. TREXA-INV-030 conclusions are correct
2. The SLD-centric language does not affect conclusions
3. Architecture is sound regardless of vocabulary
4. Creating revision noise is not productive

**Alternative**: Addendum is sufficient to document the clarification.

---

# PART 7: UPDATED GOVERNANCE DOCUMENTS

## 7.1 Color Governance Statement

**Title**: Two-Layer Color Architecture

**Statement**: Trexa employs a two-layer color architecture:

1. **Application Theme Colors (Layer 1)**: These are Trexa's platform UI colors. They are neutral, professional, and domain-independent. Examples: Primary Blue, Surface Gray, Text Black.

2. **Domain Semantic Colors (Layer 2)**: These are engineering colors owned by domain standards. Trexa renders them faithfully without modification. Examples: 500kV Blue (SLD), Critical Red (SCADA), Process Black (P&ID).

**Separation**: Layer 1 and Layer 2 colors operate independently. Platform UI colors do not inherit from or override domain semantics.

## 7.2 Platform Identity Statement

**Title**: Domain-Neutral Platform

**Statement**: Trexa is a Visual Engineering Platform, not an SLD application. The platform is designed to support multiple engineering domains with equal capability. Engineering domains retain complete ownership of their semantic color systems.

**Domains Supported**:
- Single Line Diagram (SLD)
- Process & Instrumentation Diagram (P&ID)
- Geographic Information System (GIS)
- Supervisory Control and Data Acquisition (SCADA)
- Protection Systems
- Telecommunications
- Water Systems
- Process Engineering
- Civil Engineering
- Future domains

---

**Analysis Status**: IN_PROGRESS

**Next**: Complete CONCLUSION.md
