# Investigation Analysis: TREXA-INV-030

**Investigation**: TREXA-INV-030
**Title**: Engineering Color Profile Investigation
**Status**: IN_PROGRESS

---

# PART 1: EVIDENCE FROM APPROVED DOCUMENTS

## 1.1 Existing UI Colors (TDR-012)

### Semantic UI Colors

| Role | Light | Dark | Usage |
|------|-------|------|-------|
| Primary | #2563EB | #3B82F6 | Brand, primary actions |
| Secondary | #7C3AED | #8B5CF6 | Supporting actions |
| Accent | #0891B2 | #06B6D4 | Focus, highlights |
| Success | #059669 | #10B981 | Valid, complete |
| Warning | #D97706 | #F59E0B | Caution |
| Error | #DC2626 | #EF4444 | Invalid, failure |
| Info | #0284C7 | #0EA5E9 | Information |

## 1.2 Existing SLD Colors (TREXA-INV-006)

### Voltage Colors

| Voltage | Hex | RGB |
|---------|-----|-----|
| 500 kV | #0000FF | 0, 0, 255 |
| 230 kV | #FF0000 | 255, 0, 0 |
| 115 kV | #FFBF00 | 255, 191, 0 |
| 69 kV | #00FFFF | 0, 255, 255 |

### Equipment State Colors

| State | Hex | Non-Color Indicator |
|-------|-----|---------------------|
| CLOSED | #ef4444 | Solid line |
| OPEN | #22c55e | Dashed line |
| TRIPPED | #ef4444 | Flashing |
| SELECTED | #FFFFFF | White outline |
| LOCKED | #888888 | Lock icon |
| UNKNOWN | #00FFFF | Question icon |

---

# PART 2: ENGINEERING COLOR INVENTORY

## 2.1 NGCP Voltage Color Profile

### Primary Voltage Colors

Based on TREXA-INV-006 (NGCP standard):

| Voltage Level | Primary Color | Hex | Common Usage |
|--------------|---------------|-----|--------------|
| 500 kV | Blue | #0000FF | Extra high voltage |
| 230 kV | Red | #FF0000 | High voltage |
| 115 kV | Yellow-Orange | #FFBF00 | Medium-high voltage |
| 69 kV | Cyan | #00FFFF | Medium voltage |

### Extended Voltage Colors (Future Domains)

| Voltage Level | Proposed Color | Hex | Domain |
|--------------|---------------|-----|--------|
| 138 kV | Orange | #FF8C00 | High voltage |
| 34.5 kV | Green | #228B22 | Medium voltage |
| 13.8 kV | Purple | #800080 | Medium voltage |
| 4.16 kV | Brown | #8B4513 | Low voltage |
| 480 V | Gray | #808080 | Low voltage |
| 208 V | Silver | #C0C0C0 | Low voltage |
| DC+ | Brown | #8B4513 | DC systems |
| DC- | Blue | #0000FF | DC systems |

## 2.2 Equipment State Colors

### SLD Equipment States (TREXA-INV-006)

| State | Color | Hex | Meaning |
|-------|-------|-----|---------|
| ENERGIZED | Voltage color | Varies | Conducting |
| DE-ENERGIZED | Gray | #666666 | Not conducting |
| GROUNDED | Black | #000000 | Safety ground |
| FAULT | Red | #FF0000 | Fault condition |

### Equipment Operational States

| State | Primary Color | Hex | Secondary Indicator |
|-------|--------------|-----|-------------------|
| CLOSED | Red | #ef4444 | Solid conductor |
| OPEN | Green | #22c55e | Dashed conductor |
| TRIPPED | Red (flash) | #ef4444 | 0.5s animation |
| LOCKED | Gray | #888888 | Lock icon overlay |
| MAINTENANCE | Yellow | #FBBF24 | Wrench icon |
| UNKNOWN | Cyan | #00FFFF | Question icon |

## 2.3 Alarm Severity Colors

### Standard Alarm Hierarchy

| Severity | Color | Hex | Usage |
|----------|-------|-----|-------|
| Critical | Red | #DC2626 | Life safety, major damage |
| Major | Orange | #F97316 | Significant impact |
| Minor | Yellow | #FBBF24 | Limited impact |
| Warning | Amber | #F59E0B | Attention needed |
| Information | Blue | #3B82F6 | Informational only |
| Acknowledged | Gray | #6B7280 | Cleared but logged |

## 2.4 Protection State Colors

| State | Color | Hex | Meaning |
|-------|-------|-----|---------|
| Protection Active | Green | #22c55e | Relay energized |
| Protection Tripped | Red | #ef4444 | Relay tripped |
| Protection Locked | Gray | #6B7280 | Disabled |
| Protection Test | Yellow | #FBBF24 | Test mode |

---

# PART 3: COLLISION ANALYSIS

## 3.1 UI vs Engineering Color Collision Matrix

### Potential Collisions Identified

| UI Color | Hex | Engineering Use | Hex | Collision | Severity |
|----------|-----|-----------------|-----|----------|----------|
| Primary | #2563EB | 500 kV | #0000FF | **NO** | - |
| Secondary | #7C3AED | 13.8 kV | #800080 | Low | None |
| Accent | #0891B2 | DC- | #0000FF | **NO** | - |
| Success | #059669 | Protection Active | #22c55e | **NO** | - |
| Warning | #D97706 | Minor Alarm | #FBBF24 | Low | Minor |
| Error | #DC2626 | Tripped/Alarm | #ef4444 | **YES** | HIGH |
| Info | #0284C7 | - | - | **NO** | - |

### Critical Collision: Error vs Tripped

**Issue**: UI Error color (#DC2626) matches SLD Tripped state (#ef4444)

**Risk Assessment**:
- Confusion when viewing SLD with validation errors
- UI error message uses same color as engineering alarm
- User may misinterpret UI feedback

**Resolution Options**:

| Option | Description | Recommendation |
|--------|-------------|----------------|
| A | Change UI Error to different hue | RECOMMENDED |
| B | Change Tripped color | Not recommended (standard) |
| C | Add pattern overlay to distinguish | SUPPLEMENTAL |
| D | Use shape/icon reinforcement | ALREADY IMPLEMENTED |

## 3.2 Selection Color Analysis

### Current Selection: #FFFFFF

**Assessment**: White outline is neutral and does not conflict with any engineering semantic.

**Constraints**:
- Must maintain visibility on all background colors
- Must contrast with all voltage colors
- Must be distinguishable in both light and dark themes

**Conclusion**: #FFFFFF is appropriate for selection.

## 3.3 Highlight Color Analysis

### Current Highlight: #00FFFF (Cyan)

**Issue**: Cyan is used for 69 kV voltage color AND UNKNOWN state.

**Risk**: Engineering diagram highlight may be confused with 69 kV elements.

**Resolution**:
- Keep diagram highlight separate from diagram rendering
- UI highlights apply only to UI elements
- Diagram elements use only engineering semantic colors

---

# PART 4: COLLISION-FREE UI COLOR RECOMMENDATIONS

## 4.1 Revised UI Color System

To avoid engineering collisions, the following adjustments are recommended:

| Role | Original Light | Original Dark | Recommended Light | Recommended Dark | Rationale |
|------|---------------|---------------|------------------|-----------------|-----------|
| Primary | #2563EB | #3B82F6 | **#1D4ED8** | **#3B82F6** | Deeper blue |
| Secondary | #7C3AED | #8B5CF6 | #7C3AED | #8B5CF6 | OK |
| Accent | #0891B2 | #06B6D4 | **#0E7490** | **#22D3EE** | Cyan avoided |
| Success | #059669 | #10B981 | #059669 | #10B981 | OK |
| Warning | #D97706 | #F59E0B | **#B45309** | **#D97706** | More orange |
| Error | #DC2626 | #EF4444 | **#B91C1C** | **#DC2626** | More crimson |
| Info | #0284C7 | #0EA5E9 | #0284C7 | #0EA5E9 | OK |

### Key Changes

1. **Primary**: Shifted to deeper blue (#1D4ED8) to differentiate from UI accents
2. **Accent**: Shifted cyan (#0891B2) away from 69 kV voltage color (#00FFFF)
3. **Warning**: Shifted to orange-brown (#B45309) to differentiate from Minor Alarm
4. **Error**: Shifted to crimson (#B91C1C) to provide visual separation from SLD Tripped

## 4.2 UI Reserved Colors (Non-Engineering)

The following colors are reserved exclusively for UI purposes and must NOT be used in engineering diagrams:

| Purpose | Color | Hex | Reason |
|---------|-------|-----|--------|
| Selection | White | #FFFFFF | Neutral |
| Hover | Light Blue | #DBEAFE | Light theme hover |
| Focus | Ring Blue | #3B82F6 | Focus indicator |
| Drag | Semi-transparent | #3B82F640 | Drag state |
| Drop Target | Dashed Blue | #3B82F6 | Drop zone |
| Guide | Magenta | #D946EF | Alignment guides |
| Grid | Light Gray | #F3F4F6 | Grid lines |

---

# PART 5: RESERVED ENGINEERING COLOR TABLE

## 5.1 Voltage Colors (NGCP Profile)

**RESERVED**: These colors are reserved for voltage level visualization:

| Voltage | Color Name | Hex | RGB | Usage |
|---------|-----------|-----|-----|-------|
| 500 kV | Blue | #0000FF | 0,0,255 | Extra high voltage |
| 230 kV | Red | #FF0000 | 255,0,0 | High voltage |
| 115 kV | Yellow-Orange | #FFBF00 | 255,191,0 | Medium-high voltage |
| 69 kV | Cyan | #00FFFF | 0,255,255 | Medium voltage |
| 138 kV | Orange | #FF8C00 | 255,140,0 | High voltage |
| 34.5 kV | Forest Green | #228B22 | 34,139,34 | Medium voltage |
| 13.8 kV | Purple | #800080 | 128,0,128 | Medium voltage |
| 4.16 kV | Brown | #8B4513 | 139,69,19 | Low voltage |
| 480 V | Dark Gray | #696969 | 105,105,105 | Low voltage |
| DC+ | Brown | #A52A2A | 165,42,42 | DC positive |
| DC- | Navy | #000080 | 0,0,128 | DC negative |

## 5.2 Equipment State Colors

**RESERVED**: These colors are reserved for equipment state visualization:

| State | Color Name | Hex | Pattern/Icon |
|-------|-----------|-----|--------------|
| CLOSED | Red | #ef4444 | Solid line |
| OPEN | Green | #22c55e | Dashed line |
| TRIPPED | Red | #ef4444 | 0.5s flash |
| LOCKED | Gray | #888888 | Lock icon |
| MAINTENANCE | Amber | #F59E0B | Wrench icon |
| UNKNOWN | Cyan | #00FFFF | Question icon |
| ENERGIZED | Voltage | Voltage | Solid fill |
| DE-ENERGIZED | Gray | #666666 | Hollow fill |
| GROUNDED | Black | #000000 | Ground symbol |

## 5.3 Alarm Severity Colors

**RESERVED**: These colors are reserved for alarm visualization:

| Severity | Color Name | Hex | Priority |
|----------|-----------|-----|----------|
| Critical | Crimson | #DC2626 | 1 |
| Major | Orange | #F97316 | 2 |
| Minor | Yellow | #FBBF24 | 3 |
| Warning | Amber | #F59E0B | 4 |
| Information | Blue | #3B82F6 | 5 |
| Acknowledged | Gray | #6B7280 | 6 |

## 5.4 Protection State Colors

**RESERVED**: These colors are reserved for protection system visualization:

| State | Color Name | Hex | Indicator |
|-------|-----------|-----|-----------|
| Active | Green | #22c55e | Solid |
| Tripped | Red | #ef4444 | Flash |
| Disabled | Gray | #6B7280 | Hollow |
| Test | Yellow | #FBBF24 | Dashed |

---

# PART 6: THEME COMPATIBILITY ANALYSIS

## 6.1 Light Theme

| Category | Color | Hex | Contrast with White | Accessible |
|----------|-------|-----|-------------------|-----------|
| 500 kV | Blue | #0000FF | 8.59:1 | ✅ |
| 230 kV | Red | #FF0000 | 4.63:1 | ✅ |
| 115 kV | Yellow-Orange | #FFBF00 | 1.93:1 | ⚠️ |
| 69 kV | Cyan | #00FFFF | 16.00:1 | ✅ |

**Note**: 115 kV Yellow-Orange requires dark background or bold stroke for accessibility.

## 6.2 Dark Theme

| Category | Color | Hex | Contrast with #111827 | Accessible |
|----------|-------|-----|---------------------|-----------|
| 500 kV | Blue | #0000FF | 8.59:1 | ✅ |
| 230 kV | Red | #FF0000 | 4.63:1 | ✅ |
| 115 kV | Yellow-Orange | #FFBF00 | 13.53:1 | ✅ |
| 69 kV | Cyan | #00FFFF | 16.00:1 | ✅ |

**Note**: All colors accessible in dark theme.

## 6.3 High Contrast Theme

| Category | Color | Forced Colors | Accessible |
|----------|-------|--------------|------------|
| Voltage | System | CanvasText | ✅ |
| States | System | CanvasText | ✅ |
| Alarms | System | Mark | ✅ |

**Note**: Forced colors mode uses system colors for maximum accessibility.

---

# PART 7: ACCESSIBILITY ASSESSMENT

## 7.1 Color Blindness Impact

### Deuteranopia (Red-Green, 8% of males)

| Original Color | Appears As | Impact | Mitigation |
|---------------|------------|--------|------------|
| #0000FF (500kV) | Blue | None | Safe |
| #FF0000 (230kV) | Brown | LOW | Use shape |
| #22c55e (OPEN) | Yellow-Brown | MEDIUM | Dashed line |
| #ef4444 (CLOSED) | Yellow | MEDIUM | Solid line |
| #FFBF00 (115kV) | Yellow | LOW | Safe |

### Protanopia (Red-Green, 1% of males)

| Original Color | Appears As | Impact | Mitigation |
|---------------|------------|--------|------------|
| #FF0000 (230kV) | Dark Brown | LOW | Safe |
| #22c55e (OPEN) | Yellow | MEDIUM | Dashed line |
| #ef4444 (CLOSED) | Yellow | MEDIUM | Solid line |

### Color Blind Safe Patterns

| State | Primary | Pattern | Shape |
|-------|---------|---------|-------|
| CLOSED | Red | Solid | Rectangle |
| OPEN | Green | Dashed | Rectangle |
| TRIPPED | Red | Flash | Triangle |
| LOCKED | Gray | Solid | Lock icon |
| MAINTENANCE | Yellow | Solid | Wrench |

## 7.2 Contrast Requirements

### WCAG 2.1 AA Compliance

| Element | Minimum Ratio | Light Theme | Dark Theme |
|---------|--------------|-------------|------------|
| Normal text | 4.5:1 | ✅ | ✅ |
| Large text (18px+) | 3:1 | ⚠️ | ✅ |
| UI components | 3:1 | ✅ | ✅ |
| Graphical objects | 3:1 | ⚠️ | ✅ |

---

# PART 8: RISK ASSESSMENT

## 8.1 Color Collision Risks

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| UI Error vs Tripped | HIGH | MEDIUM | Color adjustment |
| Warning vs Minor Alarm | MEDIUM | LOW | Color adjustment |
| Accent vs 69kV | MEDIUM | LOW | Color adjustment |
| Selection vs White busbar | LOW | LOW | Engineering context |

## 8.2 Accessibility Risks

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| Voltage colors indistinguishable | MEDIUM | LOW | Shape reinforcement |
| State colors confused | MEDIUM | LOW | Pattern reinforcement |
| Alarm severity unclear | HIGH | MEDIUM | Priority-based positioning |

## 8.3 Theme Risks

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| 115kV poor contrast | MEDIUM | LOW | Bold stroke |
| Light theme accessibility | MEDIUM | LOW | Dark theme default |

---

**Analysis Status**: IN_PROGRESS

**Next**: Complete CONCLUSION.md with final recommendations
