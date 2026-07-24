# Investigation: TREXA-EXP-002

**ID**: TREXA-EXP-002  
**Title**: Laboratory Artifact Organization Investigation  
**Status**: COMPLETE  
**Date**: 2026-07-24  
**Author**: OpenHands Agent  
**Type**: Experiment Investigation

---

## Investigation Scope

Investigate whether laboratory artifacts should be organized as single markdown files or self-contained directories.

---

## 1. Current Laboratory Assessment

### 1.1 Current State

**Finding**: The laboratory uses a flat file structure with single markdown files.

**Evidence**:
```
laboratory/
├── decisions/
│   ├── TDR-001.md
│   ├── TDR-002.md
│   └── TDR-003.md
├── investigations/
│   ├── TREXA-INV-001.md
│   ├── TREXA-INV-001_CON.md
│   ├── TREXA-INV-001_INDEX.md
│   ├── TREXA-INV-001_OBS.md
│   ├── TREXA-INV-001_SYN.md
│   ├── TREXA-INV-001_VAL.md
│   └── ... (40 total files)
├── methodology/
└── experiments/
```

**Artifact Count**:
- Total files: 41
- Markdown files: 41
- Single-file artifacts: 37
- Multi-file artifacts: 4 (INV-001, INV-002, INV-003, INV-008)

**Advantages**:
- Simple structure
- Easy to create
- Git-friendly
- Quick to navigate (in small numbers)

**Disadvantages**:
- Naming collisions (e.g., TREXA-INV-001_CON.md, TREXA-INV-002_CON.md)
- No logical grouping of related files
- Cannot contain binary artifacts (screenshots, datasets)
- No embedded structure for lifecycle phases

**ROE Assessment**: ⚠️ ACCEPTABLE (current scale) → ❌ PROBLEMATIC (future scale)

---

## 2. Organization Alternatives

### Option A: Single Markdown Files (Current)

**Structure**:
```
laboratory/
└── experiments/
    ├── TREXA-EXP-001.md
    └── TREXA-EXP-002.md
```

**Advantages**:
- Simple and familiar
- Git-native (diffs, merges work well)
- Easy to create and edit
- Quick to search

**Disadvantages**:
- Cannot contain non-text artifacts
- No internal structure enforcement
- File naming becomes complex with suffixes
- Becomes unwieldy at scale

### Option B: Self-Contained Experiment Directory

**Structure**:
```
laboratory/
└── experiments/
    └── TREXA-EXP-001/
        ├── SPEC.md
        ├── EXECUTION.md
        ├── RESULT.md
        ├── evidence/
        │   └── *.png, *.json, *.log
        └── artifacts/
            └── generated files
```

**Advantages**:
- Natural containment of all artifacts
- Clear lifecycle phases
- Scalable file naming
- Supports binary artifacts
- Explicit structure

**Disadvantages**:
- More complex to create
- Requires directory management
- Git operations more complex
- Overhead for simple experiments

### Option C: Hybrid Approach (Current Evidence Suggests)

**Finding**: The current organization ALREADY uses multi-file patterns for complex artifacts.

**Evidence**:
```
TREXA-INV-001: 6 files (986 lines total)
TREXA-INV-002: 7 files
TREXA-INV-003: 6 files
```

Current naming convention uses suffixes:
- `_CON.md` = Conclusion
- `_OBS.md` = Observations
- `_SYN.md` = Synthesis
- `_VAL.md` = Validation

**Advantages**:
- Preserves current practice
- Incremental improvement
- Already proven in the laboratory
- Minimal change

**Disadvantages**:
- Still flat structure
- No explicit directories
- Naming conventions become complex

---

## 3. Comparative Analysis

### 3.1 Scalability Assessment

| Scale | Option A (Flat) | Option B (Directory) | Option C (Hybrid) |
|-------|-----------------|---------------------|-------------------|
| 10 artifacts | ✅ Simple | ⚠️ Overhead | ✅ Optimal |
| 100 artifacts | ⚠️ Manageable | ✅ Optimal | ✅ Optimal |
| 1000 artifacts | ❌ Unmanageable | ✅ Optimal | ⚠️ Complex |
| Binary artifacts | ❌ Not supported | ✅ Supported | ❌ Limited |
| Nested content | ❌ Not supported | ✅ Supported | ⚠️ Limited |

### 3.2 Evidence Management Capability

| Evidence Type | Option A | Option B | Option C |
|--------------|----------|----------|----------|
| Screenshots | ❌ | ✅ | ❌ |
| Datasets | ❌ | ✅ | ❌ |
| Execution logs | ⚠️ External | ✅ Embedded | ⚠️ External |
| Generated files | ❌ | ✅ | ❌ |
| AI conversations | ⚠️ Copy/paste | ✅ Embedded | ⚠️ Copy/paste |
| Scripts | ❌ | ✅ | ❌ |

### 3.3 Scientific Integrity

| Criterion | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Reproducibility | ⚠️ External | ✅ Self-contained | ⚠️ Partial |
| Traceability | ⚠️ Manual | ✅ Explicit | ⚠️ Manual |
| Evidence chain | ❌ Weak | ✅ Strong | ⚠️ Weak |
| Lifecycle clarity | ❌ Blurred | ✅ Clear | ⚠️ Implicit |

---

## 4. Future KDE Evolution Assessment

### 4.1 Evidence from Current Artifacts

**Finding**: Current investigations ALREADY span multiple files.

**Evidence**:
- TREXA-INV-001: 6 files (CON, INDEX, OBS, SYN, VAL, main)
- TREXA-INV-002: 7 files (CAP, CLS, CON, DEP, INT, RISK, main)
- TREXA-INV-003: 6 files (ANAL, CON, MAT, PROF, TAX, main)
- TREXA-INV-008: Multiple files (main, 008A)

**Implication**: The laboratory already requires multi-file artifacts but uses flat naming.

### 4.2 Artifact Type Assessment

| Artifact Type | Current Files | Future Likely Needs |
|--------------|---------------|-------------------|
| Experiments | 1 | Evidence, artifacts, traces |
| Investigations | 1-7 | Research, analysis, evidence |
| Reviews | 1 | Comments, responses |
| Decisions | 1 | Supporting analysis |
| Planning | 1 | Task details, estimates |

**Finding**: Experiments and Investigations are most likely to require multi-file support.

---

## 5. Recommended Organization

### 5.1 Finding

**Finding**: Option B (Self-Contained Directory) provides superior long-term value for Experiments and Investigations. Option A remains acceptable for simpler artifacts (Decisions, Reviews, Planning).

### 5.2 Recommendation Matrix

| Artifact Type | Recommended Structure | Rationale |
|--------------|---------------------|-----------|
| Experiments | Option B (Directory) | Highest evidence needs |
| Investigations | Option B (Directory) | Complex, multi-phase |
| Reviews | Option A (File) | Simple, text-focused |
| Decisions | Option A (File) | Decision is final |
| Planning | Option A (File) | Simple lists |

### 5.3 Proposed Standard

```
laboratory/
├── experiments/
│   └── TREXA-EXP-NNN/
│       ├── SPEC.md           # Hypothesis, criteria
│       ├── EXECUTION.md       # Execution log
│       ├── RESULT.md          # Conclusions
│       ├── evidence/          # Screenshots, data
│       └── artifacts/         # Generated files
│
├── investigations/
│   └── TREXA-INV-NNN/
│       ├── SPEC.md            # Research questions
│       ├── ANALYSIS.md       # Research findings
│       ├── CONCLUSION.md      # Conclusions
│       ├── evidence/          # Supporting materials
│       └── artifacts/         # Analysis outputs
│
├── decisions/
│   └── TDR-NNN.md            # Single file (final)
│
├── reviews/
│   └── REVIEW-NNN.md         # Single file (final)
│
└── planning/
    └── PLAN-NNN.md           # Single file (final)
```

---

## 6. Migration Impact Assessment

### 6.1 Effort Estimation

**Finding**: Migration from current flat structure to Option B requires significant effort.

| Artifact Type | Count | Migration Effort |
|--------------|-------|------------------|
| Experiments | 1 | Low |
| Investigations | 38 | Medium |
| Decisions | 3 | Low |
| Reviews | 0 | None |
| Planning | 0 | None |

**Estimated Effort**: 2-4 hours for full migration.

### 6.2 Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Git history loss | Medium | Preserve old files in archive |
| Link breaks | High | Update all cross-references |
| Agent confusion | Low | Document new structure |

---

## 7. Final Recommendation

### 7.1 Conclusion

**Finding**: The hypothesis is **PARTIALLY CONFIRMED**.

| Aspect | Finding |
|--------|---------|
| Self-contained directories superior for Experiments | ✅ CONFIRMED |
| Self-contained directories superior for Investigations | ✅ CONFIRMED |
| Self-contained directories needed for Decisions/Reviews | ❌ NOT CONFIRMED |
| Migration immediately necessary | ❌ NOT CONFIRMED |

### 7.2 Decision

| Recommendation | Decision |
|----------------|----------|
| Adopt Option B for Experiments | RECOMMENDED |
| Adopt Option B for Investigations | RECOMMENDED |
| Retain Option A for Decisions | RECOMMENDED |
| Retain Option A for Reviews | RECOMMENDED |
| Immediate migration | DEFER |

### 7.3 Next Steps (Future Experiment)

If migration is approved in a future experiment:
1. Create migration script
2. Archive current structure
3. Migrate experiments first
4. Migrate investigations
5. Update cross-references
6. Document new standards

---

## 8. Investigation Conclusion

**Status**: COMPLETE

**Summary**: Self-contained directories (Option B) provide superior organization for Experiments and Investigations due to evidence management requirements and scientific integrity needs. However, simpler artifacts (Decisions, Reviews, Planning) remain well-suited to single-file organization.

**Recommendation**: Adopt Option B for Experiments and Investigations. Defer migration pending approval.

---

*Investigation conducted per TREXA-EXP-002 authorization*
*No repository modifications made*
