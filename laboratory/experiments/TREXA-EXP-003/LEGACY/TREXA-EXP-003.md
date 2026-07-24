# Investigation: TREXA-EXP-003

**ID**: TREXA-EXP-003  
**Title**: Laboratory Artifact Migration Planning  
**Status**: COMPLETE  
**Date**: 2026-07-24  
**Author**: OpenHands Agent  
**Type**: Migration Specification  
**Purpose**: Design migration plan (NO implementation)

---

## Investigation Scope

Design a complete migration strategy to reorganize the Laboratory per TREXA-EXP-002 conclusions.

---

## 1. Laboratory Inventory

### 1.1 Complete Artifact List

| # | Path | Type | Size | Lines |
|---|------|------|------|-------|
| 1 | README.md | Documentation | - | - |
| 2 | decisions/TDR-001.md | Decision | - | - |
| 3 | decisions/TDR-002.md | Decision | - | - |
| 4 | decisions/TDR-003.md | Decision | - | - |
| 5 | evidence/README.md | Documentation | - | - |
| 6 | experiments/README.md | Documentation | - | - |
| 7 | experiments/TREXA-EXP-001.md | Experiment | - | 119 |
| 8 | experiments/TREXA-EXP-002.md | Experiment | - | 330 |
| 9 | investigations/TREXA-INV-001.md | Investigation | - | 85 |
| 10 | investigations/TREXA-INV-001_CON.md | Investigation Part | - | 151 |
| 11 | investigations/TREXA-INV-001_INDEX.md | Investigation Part | - | 82 |
| 12 | investigations/TREXA-INV-001_OBS.md | Investigation Part | - | 225 |
| 13 | investigations/TREXA-INV-001_SYN.md | Investigation Part | - | 297 |
| 14 | investigations/TREXA-INV-001_VAL.md | Investigation Part | - | 146 |
| 15 | investigations/TREXA-INV-002.md | Investigation | - | - |
| 16 | investigations/TREXA-INV-002_CAP.md | Investigation Part | - | - |
| 17 | investigations/TREXA-INV-002_CLS.md | Investigation Part | - | - |
| 18 | investigations/TREXA-INV-002_CON.md | Investigation Part | - | - |
| 19 | investigations/TREXA-INV-002_DEP.md | Investigation Part | - | - |
| 20 | investigations/TREXA-INV-002_INT.md | Investigation Part | - | - |
| 21 | investigations/TREXA-INV-002_RISK.md | Investigation Part | - | - |
| 22 | investigations/TREXA-INV-003.md | Investigation | - | - |
| 23 | investigations/TREXA-INV-003_ANAL.md | Investigation Part | - | - |
| 24 | investigations/TREXA-INV-003_CON.md | Investigation Part | - | - |
| 25 | investigations/TREXA-INV-003_MAT.md | Investigation Part | - | - |
| 26 | investigations/TREXA-INV-003_PROF.md | Investigation Part | - | - |
| 27 | investigations/TREXA-INV-003_TAX.md | Investigation Part | - | - |
| 28 | investigations/TREXA-INV-004.md | Investigation | - | - |
| 29 | investigations/TREXA-INV-005.md | Investigation | - | - |
| 30 | investigations/TREXA-INV-006.md | Investigation | - | - |
| 31 | investigations/TREXA-INV-007.md | Investigation | - | - |
| 32 | investigations/TREXA-INV-007A.md | Investigation Part | - | - |
| 33 | investigations/TREXA-INV-007B.md | Investigation Part | - | - |
| 34 | investigations/TREXA-INV-007C.md | Investigation Part | - | - |
| 35 | investigations/TREXA-INV-008.md | Investigation | - | - |
| 36 | investigations/TREXA-INV-008A.md | Investigation Part | - | - |
| 37 | investigations/TREXA-INV-010.md | Investigation | - | - |
| 38 | investigations/TREXA-INV-011.md | Investigation | - | 881 |
| 39 | investigations/TREXA-REV-001.md | Review | - | - |
| 40 | methodology/AI-FIRST-METHODOLOGY.md | Methodology | - | - |
| 41 | planning/README.md | Documentation | - | - |
| 42 | reviews/README.md | Documentation | - | - |

---

## 2. Artifact Classification Matrix

| Category | Count | Migration Required | Action |
|----------|-------|------------------|--------|
| Experiments | 2 | YES | Convert to directories |
| Investigations | 30 | YES | Convert to directories |
| Decisions | 3 | NO | Retain flat structure |
| Reviews | 1 | NO | Retain flat structure |
| Methodology | 1 | NO | Retain flat structure |
| Planning | 1 | NO | Retain flat structure |
| Documentation | 5 | NO | Retain flat structure |

### 2.1 Experiments Summary

| ID | Name | Parts | Migration Target |
|----|------|-------|-----------------|
| TREXA-EXP-001 | KDE Runtime Verification | 1 | Directory |
| TREXA-EXP-002 | Laboratory Organization Investigation | 1 | Directory |

### 2.2 Investigations Summary

| ID | Name | Parts | Migration Target |
|----|------|-------|-----------------|
| TREXA-INV-001 | Engineering Implications | 6 | Directory |
| TREXA-INV-002 | Platform Capability Discovery | 7 | Directory |
| TREXA-INV-003 | AI Architecture | 6 | Directory |
| TREXA-INV-004 | Repository Structure | 1 | Directory |
| TREXA-INV-005 | Domain Definition | 1 | Directory |
| TREXA-INV-006 | SLD Domain | 1 | Directory |
| TREXA-INV-007 | Technology Selection | 4 | Directory |
| TREXA-INV-008 | Foundation Architecture | 2 | Directory |
| TREXA-INV-010 | (unnamed) | 1 | Directory |
| TREXA-INV-011 | Foundation Architecture | 1 | Directory |

---

## 3. Target Directory Specification

### 3.1 Experiment Target Structure

**Finding**: Experiments have a clear lifecycle: SPEC → EXECUTION → RESULT

**Evidence**:
- TREXA-EXP-001 has: Hypothesis, Precondition, Success Criteria, Execution Log, Conclusion
- TREXA-EXP-002 has: Investigation Scope, Analysis Sections, Conclusion

**Target Structure**:
```
laboratory/experiments/
└── TREXA-EXP-NNN/
    ├── SPEC.md              # Hypothesis, criteria, preconditions
    ├── EXECUTION.md         # Execution log, test results
    ├── RESULT.md            # Conclusions, findings
    ├── README.md            # Quick reference
    ├── evidence/            # Screenshots, data (if any)
    └── artifacts/           # Generated files (if any)
```

### 3.2 Investigation Target Structure

**Finding**: Investigations have phases: SCOPE → RESEARCH → ANALYSIS → CONCLUSION

**Evidence**:
- Current suffixes: _CON (Conclusion), _OBS (Observations), _SYN (Synthesis), _VAL (Validation), _ANAL (Analysis), _CAP (Capabilities), etc.

**Target Structure**:
```
laboratory/investigations/
└── TREXA-INV-NNN/
    ├── SPEC.md              # Scope, questions, intent
    ├── RESEARCH.md          # Research findings
    ├── ANALYSIS.md          # Analysis results (combines OBS, SYN, TAX, etc.)
    ├── CONCLUSION.md        # Final conclusions (combines CON, VAL)
    ├── README.md            # Quick reference
    ├── evidence/            # Supporting materials
    └── artifacts/           # Generated analysis files
```

### 3.3 Decision Target Structure

**Finding**: Decisions are final, single-purpose documents.

**Evidence**:
- TDRs contain: Context, Decision, Consequences only
- No supporting files in current structure

**Target Structure**: RETAIN AS IS (single file)
```
laboratory/decisions/
└── TDR-NNN.md              # No change
```

### 3.4 Review Target Structure

**Finding**: Reviews are final assessment documents.

**Target Structure**: RETAIN AS IS
```
laboratory/reviews/
└── REVIEW-NNN.md            # No change
```

---

## 4. Naming Convention Specification

### 4.1 Directory Names

| Artifact Type | Convention | Example |
|--------------|------------|---------|
| Experiments | TREXA-EXP-NNN | TREXA-EXP-001 |
| Investigations | TREXA-INV-NNN | TREXA-INV-001 |
| Decisions | TDR-NNN | TDR-001 |
| Reviews | REVIEW-NNN | REVIEW-001 |

### 4.2 Primary Document Names

| Document | Filename | Rationale |
|----------|----------|----------|
| Experiment Spec | SPEC.md | Defines hypothesis and criteria |
| Experiment Execution | EXECUTION.md | Records test execution |
| Experiment Result | RESULT.md | Contains conclusions |
| Investigation Spec | SPEC.md | Defines scope and questions |
| Investigation Research | RESEARCH.md | Research findings |
| Investigation Analysis | ANALYSIS.md | Analysis results |
| Investigation Conclusion | CONCLUSION.md | Final conclusions |

### 4.3 Evidence Folder

```
evidence/
├── sources/                # External sources cited
├── screenshots/            # UI screenshots
├── data/                  # Raw data files
├── logs/                  # Execution logs
└── conversations/          # AI conversation logs
```

### 4.4 Artifacts Folder

```
artifacts/
├── generated/              # Files generated during experiment
├── scripts/                # Scripts used
├── temporary/              # Temporary files (to be cleaned)
└── outputs/                # Final outputs
```

---

## 5. Migration Sequence

### 5.1 Phase Order Justification

**Finding**: Migration should proceed from low-risk to high-risk to allow verification at each step.

**Rationale**:
1. Archive first (safety net)
2. Documentation (non-breaking)
3. Decisions/Reviews (no change needed)
4. Experiments (newer, smaller)
5. Investigations (larger, more complex)
6. Verification (confirm integrity)

### 5.2 Migration Phases

| Phase | Name | Items | Risk Level |
|-------|------|-------|------------|
| 1 | Pre-Migration Archive | All files | NONE |
| 2 | Documentation Update | 5 README files | LOW |
| 3 | Decisions (Verify No Change) | 3 TDRs | NONE |
| 4 | Experiments Migration | 2 experiments | MEDIUM |
| 5 | Investigations Migration | 30 investigation files | HIGH |
| 6 | Cross-Reference Update | All referencing files | MEDIUM |
| 7 | Post-Migration Verification | All artifacts | NONE |

### 5.3 Detailed Migration Steps

#### Phase 1: Pre-Migration Archive
```bash
# Create archive with timestamp
cp -r laboratory laboratory_BACKUP_YYYYMMDD_HHMMSS
```

#### Phase 2: Documentation Update
```bash
# Update laboratory/README.md
# Update experiments/README.md
# Update investigations/README.md
# Update decisions/README.md
# Update reviews/README.md
```

#### Phase 3: Decisions Verification
```bash
# Verify decisions require no changes
# Document findings
```

#### Phase 4: Experiments Migration

For each experiment (TREXA-EXP-001, TREXA-EXP-002):
```bash
# Create directory
mkdir -p laboratory/experiments/TREXA-EXP-NNN/{evidence,artifacts}

# Extract sections from original .md
# Write to appropriate SPEC.md, EXECUTION.md, RESULT.md

# Preserve original as legacy reference
mv laboratory/experiments/TREXA-EXP-NNN.md \
   laboratory/experiments/TREXA-EXP-NNN/LEGACY.md
```

#### Phase 5: Investigations Migration

For each investigation:
```bash
# Create directory
mkdir -p laboratory/investigations/TREXA-INV-NNN/{evidence,artifacts}

# Merge suffix files into consolidated documents
# SPEC.md = main .md content
# RESEARCH.md = merged OBS, INDEX files
# ANALYSIS.md = merged TAX, ANAL, CLS, CAP, MAT, PROF, DEP, INT, RISK, SYN files
# CONCLUSION.md = merged CON, VAL files

# Preserve originals as LEGACY/
mkdir -p laboratory/investigations/TREXA-INV-NNN/LEGACY
mv laboratory/investigations/TREXA-INV-NNN*.md \
   laboratory/investigations/TREXA-INV-NNN/LEGACY/
```

#### Phase 6: Cross-Reference Update
```bash
# Update all cross-references in:
# - README files
# - Investigation documents
# - Decision documents
# - External documentation
```

#### Phase 7: Post-Migration Verification
```bash
# Run verification script (see Section 8)
```

---

## 6. Compatibility Strategy

### 6.1 Legacy File Preservation

**Finding**: Historical references may point to original file locations.

**Evidence**:
- TREXA-INV-001_INDEX.md references `.kde/knowledge/...`
- README.md references investigation files

**Strategy**:
| Item | Action | Justification |
|------|--------|---------------|
| Original files | Move to LEGACY/ subdirectory | Preserve git history |
| Cross-references | Update to new paths | Maintain integrity |
| External references | Add redirect notes | External links may exist |

### 6.2 LEGACY Directory Contents

Each migrated artifact directory shall contain:
```
TREXA-INV-NNN/
├── SPEC.md
├── ANALYSIS.md
├── CONCLUSION.md
├── LEGACY/                    # Preserved original files
│   ├── TREXA-INV-NNN.md
│   ├── TREXA-INV-NNN_CON.md
│   └── ...
└── README.md                  # Links to LEGACY/
```

### 6.3 Backward Compatibility Index

Create `laboratory/COMPATIBILITY_INDEX.md`:
```markdown
# Legacy File Index

This index maps old file paths to new directory locations.

## Experiments
| Old Path | New Path |
|----------|----------|
| TREXA-EXP-001.md | TREXA-EXP-001/SPEC.md |

## Investigations
| Old Path | New Path |
|----------|----------|
| TREXA-INV-001.md | TREXA-INV-001/SPEC.md |
| TREXA-INV-001_CON.md | TREXA-INV-001/CONCLUSION.md |
...
```

---

## 7. Rollback Strategy

### 7.1 Rollback Triggers

| Trigger | Severity | Rollback Action |
|---------|----------|-----------------|
| Verification failure | HIGH | Full rollback |
| Artifact count mismatch | HIGH | Full rollback |
| Evidence modification detected | HIGH | Full rollback |
| Reference broken | MEDIUM | Partial fix then continue |
| Documentation incomplete | LOW | Continue with fix |

### 7.2 Rollback Procedure

```bash
# If rollback required:
rm -rf laboratory
mv laboratory_BACKUP_YYYYMMDD_HHMMSS laboratory

# Report rollback to human
```

### 7.3 Rollback Verification

After rollback, verify:
1. All original files present
2. All original content intact
3. Git history preserved
4. No orphaned artifacts

---

## 8. Migration Verification Procedure

### 8.1 Verification Script (Pseudocode)

```python
def verify_migration():
    """Verify migration integrity"""
    
    # 1. Artifact Count Verification
    expected_counts = {
        'experiments': 2,
        'investigations': 10,
        'decisions': 3,
        'reviews': 1,
    }
    
    for category, expected in expected_counts.items():
        actual = count_directories(f'laboratory/{category}')
        assert actual == expected, f"{category}: expected {expected}, got {actual}"
    
    # 2. Required Files Verification
    required_files = {
        'TREXA-EXP-001': ['SPEC.md', 'EXECUTION.md', 'RESULT.md'],
        'TREXA-INV-001': ['SPEC.md', 'ANALYSIS.md', 'CONCLUSION.md'],
    }
    
    for artifact_id, files in required_files.items():
        for f in files:
            path = find_artifact_path(artifact_id) + f
            assert os.path.exists(path), f"Missing: {path}"
    
    # 3. Content Preservation Verification
    for old_file, new_file in legacy_mapping.items():
        old_content = read_file(f"laboratory_BACKUP/{old_file}")
        new_content = extract_from_directory(f"laboratory/{new_file}")
        assert old_content in new_content, f"Content mismatch: {old_file}"
    
    # 4. Cross-Reference Verification
    broken_refs = find_broken_references()
    assert len(broken_refs) == 0, f"Broken references: {broken_refs}"
    
    # 5. Evidence Preservation
    for evidence in original_evidence:
        assert evidence_exists(evidence), f"Missing evidence: {evidence}"
    
    return True
```

### 8.2 Verification Checklist

| Check | Command | Expected Result |
|-------|---------|-----------------|
| Directory count | `find laboratory -type d -name "TREXA-EXP-*"` | 2 directories |
| Directory count | `find laboratory -type d -name "TREXA-INV-*"` | 10 directories |
| File presence | `ls laboratory/experiments/TREXA-EXP-001/` | SPEC.md, etc. |
| LEGACY present | `ls laboratory/investigations/TREXA-INV-001/LEGACY/` | Original files |
| No .md in root | `ls laboratory/experiments/*.md 2>/dev/null` | Empty |

---

## 9. Risk Assessment

### 9.1 Risk Matrix

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Git history loss | LOW | HIGH | Archive before migration |
| Content corruption | LOW | CRITICAL | Backup verification |
| Reference breakage | MEDIUM | HIGH | Cross-reference update phase |
| Partial migration | LOW | HIGH | Atomic migration per artifact |
| Human error | MEDIUM | MEDIUM | Scripted migration |
| Rollback failure | VERY LOW | CRITICAL | Tested rollback procedure |

### 9.2 Risk Mitigation Summary

| Mitigation | Implementation |
|------------|----------------|
| Full backup | Archive to `_BACKUP_YYYYMMDD` before any changes |
| Incremental verification | Verify after each phase |
| Scripted migration | Automate file operations |
| LEGACY preservation | Keep all originals for reference |
| COMPATIBILITY_INDEX | Map old paths to new |

---

## 10. Complete Migration Specification

### 10.1 Migration Summary

| Item | Value |
|------|-------|
| Total artifacts to migrate | 32 files → 12 directories |
| Experiments | 2 → 2 directories |
| Investigations | 30 → 10 directories |
| Decisions | 0 (no change) |
| Estimated time | 2-4 hours |
| Risk level | MEDIUM |

### 10.2 Migration Commands

```bash
#!/bin/bash
# TREXA-EXP-003 Migration Script
# WARNING: This script is SPECIFICATION ONLY
# Do NOT execute until authorized

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LAB_BACKUP="laboratory_BACKUP_${TIMESTAMP}"

# Pre-migration
echo "Creating backup: ${LAB_BACKUP}"
cp -r laboratory "${LAB_BACKUP}"

# Phase 4: Migrate Experiments
echo "Migrating experiments..."
for exp in TREXA-EXP-001 TREXA-EXP-002; do
    mkdir -p "laboratory/experiments/${exp}/{evidence,artifacts,LEGACY}"
    # Extract and reorganize content
    # (Implementation details in Phase 4)
done

# Phase 5: Migrate Investigations
echo "Migrating investigations..."
for inv in TREXA-INV-001 TREXA-INV-002 TREXA-INV-003 TREXA-INV-004 \
          TREXA-INV-005 TREXA-INV-006 TREXA-INV-007 TREXA-INV-008 \
          TREXA-INV-010 TREXA-INV-011; do
    mkdir -p "laboratory/investigations/${inv}/{evidence,artifacts,LEGACY}"
    # Extract and reorganize content
    # (Implementation details in Phase 5)
done

# Phase 6: Update Cross-References
echo "Updating cross-references..."
# (Implementation details in Phase 6)

# Phase 7: Verify
echo "Verifying migration..."
# (Run verification procedure)
```

### 10.3 Post-Migration Expected Structure

```
laboratory/
├── README.md                    # Updated
├── COMPATIBILITY_INDEX.md      # NEW - maps old to new paths
│
├── experiments/
│   ├── README.md               # Updated
│   ├── TREXA-EXP-001/
│   │   ├── SPEC.md             # NEW
│   │   ├── EXECUTION.md        # NEW
│   │   ├── RESULT.md           # NEW
│   │   ├── README.md
│   │   ├── LEGACY/             # Preserved originals
│   │   │   └── TREXA-EXP-001.md
│   │   ├── evidence/
│   │   └── artifacts/
│   └── TREXA-EXP-002/
│       └── ... (same structure)
│
├── investigations/
│   ├── README.md               # Updated
│   ├── TREXA-INV-001/
│   │   ├── SPEC.md             # Consolidated
│   │   ├── ANALYSIS.md         # Consolidated
│   │   ├── CONCLUSION.md       # Consolidated
│   │   ├── README.md
│   │   ├── LEGACY/             # Preserved originals
│   │   │   ├── TREXA-INV-001.md
│   │   │   ├── TREXA-INV-001_CON.md
│   │   │   └── ...
│   │   ├── evidence/
│   │   └── artifacts/
│   └── TREXA-INV-002/
│       └── ... (same structure)
│
├── decisions/                   # NO CHANGE
│   ├── README.md
│   ├── TDR-001.md
│   ├── TDR-002.md
│   └── TDR-003.md
│
├── reviews/                    # NO CHANGE
│   ├── README.md
│   └── TREXA-REV-001.md
│
├── methodology/                # NO CHANGE
│   └── AI-FIRST-METHODOLOGY.md
│
├── evidence/                   # NO CHANGE
│   └── README.md
│
├── planning/                   # NO CHANGE
│   └── README.md
│
└── reviews/                    # NO CHANGE
    └── README.md
```

---

## 11. Investigation Conclusion

**Status**: COMPLETE

**Summary**: Complete migration specification designed for TREXA-EXP-002 reorganization.

**Key Decisions**:
1. Migrate Experiments to self-contained directories
2. Migrate Investigations to self-contained directories
3. Consolidate investigation suffix files into ANALYSIS.md and CONCLUSION.md
4. Preserve all original files in LEGACY/ subdirectory
5. Create COMPATIBILITY_INDEX.md for backward references
6. 7-phase migration with verification after each phase

**Next Steps**:
1. Human review of this specification
2. Authorization for migration experiment
3. Execute migration in authorized experiment

---

*Migration specification produced per TREXA-EXP-003 authorization*
*No implementation performed - specification only*
