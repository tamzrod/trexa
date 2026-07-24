# Reasoning Profile Taxonomy: TREXA-INV-003

**Investigation**: TREXA-INV-003
**Title**: AI Engine Selection and Reasoning Strategy
**Date**: 2026-07-23T09:00:00Z
**Status**: COMPLETE

---

## Reasoning Profile Taxonomy

This document defines reasoning profiles that match different task requirements.

---

## Profile Definitions

### Profile 1: FAST

**Description**: Minimal reasoning for simple, factual tasks.

**Characteristics**:
| Attribute | Value |
|-----------|-------|
| **Depth** | Shallow (1-2 steps) |
| **Context Window** | Small (≤8K tokens) |
| **Retrieval** | Optional |
| **Verification** | None |
| **Latency** | Minimal (<1s) |
| **Cost** | Minimal |

**Use Cases**:
- Simple factual lookups
- Direct rule application
- Single primitive generation
- Basic symbol retrieval

**Task Match**: TASK-001, TASK-002, TASK-003

**Profile Example**:
```
Input: "What color is 115kV bus?"
Output: "Cyan (#00FFFF) per NGCP standard"
```

---

### Profile 2: BALANCED

**Description**: Standard reasoning for common engineering tasks.

**Characteristics**:
| Attribute | Value |
|-----------|-------|
| **Depth** | Medium (3-5 steps) |
| **Context Window** | Standard (≤32K tokens) |
| **Retrieval** | Optional |
| **Verification** | Light |
| **Latency** | Moderate (1-5s) |
| **Cost** | Moderate |

**Use Cases**:
- Standard validation
- Multi-step generation
- Basic analysis
- Routine explanation

**Task Match**: TASK-004, TASK-005, TASK-006, TASK-007, TASK-008

**Profile Example**:
```
Input: "Validate this feeder pattern: DS-CB-ES-DS"
Output: "Valid. Pattern matches standard. All connection points aligned."
```

---

### Profile 3: DEEP RESEARCH

**Description**: Extensive reasoning for complex analysis and synthesis.

**Characteristics**:
| Attribute | Value |
|-----------|-------|
| **Depth** | Deep (10+ steps) |
| **Context Window** | Large (≤128K tokens) |
| **Retrieval** | Extensive |
| **Verification** | Thorough |
| **Latency** | Higher (10-30s) |
| **Cost** | Higher |

**Use Cases**:
- Complex analysis
- Multi-source synthesis
- Comprehensive validation
- Root cause debugging

**Task Match**: TASK-010, TASK-011, TASK-012, TASK-013, TASK-014, TASK-015

**Profile Example**:
```
Input: "Analyze single points of failure in this SLD topology"
Output: [Multi-paragraph analysis with identified risks, 
         probability assessment, mitigation recommendations]
```

---

### Profile 4: VERIFICATION

**Description**: Rigorous validation with proof-like reasoning.

**Characteristics**:
| Attribute | Value |
|-----------|-------|
| **Depth** | Step-by-step |
| **Context Window** | Standard (≤32K tokens) |
| **Retrieval** | Rules/Standards only |
| **Verification** | Exhaustive |
| **Latency** | Moderate (5-15s) |
| **Cost** | Moderate-High |
| **Confidence** | Explicit |

**Use Cases**:
- Safety-critical validation
- Standards compliance checking
- Formal verification
- Audit trails

**Task Match**: TASK-004, TASK-005, TASK-006 (safety-critical variants)

**Profile Example**:
```
Input: "Verify IEC 61850 compliance of this SLD"
Output: "Step 1: Check Logical Node naming... ✓
         Step 2: Verify Data Object representation... ✓
         Step 3: Validate control function visualization... ✓
         Conclusion: COMPLIANT (95% coverage, 3 warnings)"
```

---

### Profile 5: CREATIVE

**Description**: Generative reasoning with novel synthesis.

**Characteristics**:
| Attribute | Value |
|-----------|-------|
| **Depth** | Variable |
| **Context Window** | Large (≤128K tokens) |
| **Retrieval** | Extensive |
| **Verification** | Deferred |
| **Latency** | Higher (10-30s) |
| **Cost** | Higher |
| **Novelty** | Actively sought |

**Use Cases**:
- Novel symbol design
- Alternative routing suggestions
- Creative engineering solutions
- Prototype generation

**Task Match**: TASK-013, TASK-014, TASK-015, TASK-020, TASK-021

**Profile Example**:
```
Input: "Suggest alternative SLD layouts for redundancy"
Output: [Multiple layout alternatives with trade-off analysis]
```

---

### Profile 6: HYBRID IR+R

**Description**: Combines retrieval-augmented generation with reasoning.

**Characteristics**:
| Attribute | Value |
|-----------|-------|
| **Retrieval** | Active (RAG) |
| **Reasoning** | Medium-Deep |
| **Context Window** | Large (≤128K tokens) |
| **Citations** | Required |
| **Latency** | Moderate-High (5-20s) |
| **Cost** | Moderate-High |

**Use Cases**:
- Knowledge-grounded generation
- Standards-based explanation
- Cited analysis
- Document-grounded reasoning

**Task Match**: TASK-016, TASK-017, TASK-018, TASK-007

**Profile Example**:
```
Input: "Explain SLD busbar color standards with citations"
Output: [Explanation citing IEC 61850, IEEE C37.2, NGCP guidelines]
```

---

### Profile 7: DIAGNOSTIC

**Description**: Systematic debugging and root cause analysis.

**Characteristics**:
| Attribute | Value |
|-----------|-------|
| **Approach** | Hypothesis-driven |
| **Depth** | Deep (until root cause) |
| **Context Window** | Large (≤128K tokens) |
| **Verification** | Each hypothesis |
| **Explanation** | Full trail |
| **Latency** | Variable (until resolved) |

**Use Cases**:
- Validation failure diagnosis
- Data quality debugging
- Error investigation
- Troubleshooting

**Task Match**: TASK-022, TASK-023, TASK-024

**Profile Example**:
```
Input: "Why is this SLD validation failing?"
Output: "Hypothesis 1: Connection type mismatch... Rejected
         Hypothesis 2: Missing connection point... Accepted
         Root Cause: DS component missing bottom connection"
```

---

## Profile Comparison Matrix

| Profile | Speed | Cost | Depth | Retrieval | Verification | Best For |
|--------|-------|------|-------|-----------|--------------|---------|
| **FAST** | ★★★★★ | ★ | ★ | ○ | ○ | Factual lookups |
| **BALANCED** | ★★★ | ★★ | ★★★ | ○ | ○ | Standard tasks |
| **DEEP RESEARCH** | ★ | ★★★ | ★★★★★ | ★★ | ★★★ | Complex analysis |
| **VERIFICATION** | ★★ | ★★★ | ★★★★ | ★ | ★★★★★ | Safety validation |
| **CREATIVE** | ★★ | ★★★ | ★★★★ | ★★ | ○ | Novel solutions |
| **HYBRID IR+R** | ★★ | ★★★ | ★★★★ | ★★★ | ★★ | Grounded answers |
| **DIAGNOSTIC** | ★★ | ★★★ | ★★★★★ | ★ | ★★★ | Debugging |

Legend: ★ = High/Good, ○ = None/Low

---

## Resource Requirements

### Context Window Requirements

| Profile | Min Context | Max Context | Typical Usage |
|---------|------------|------------|---------------|
| **FAST** | 1K | 8K | 80% |
| **BALANCED** | 8K | 32K | 50% |
| **DEEP RESEARCH** | 32K | 128K | 20% |
| **VERIFICATION** | 8K | 64K | 30% |
| **CREATIVE** | 32K | 128K | 15% |
| **HYBRID IR+R** | 32K | 128K | 40% |
| **DIAGNOSTIC** | 16K | 128K | 25% |

### Compute Cost Relative to FAST

| Profile | Relative Cost | Relative Latency |
|---------|---------------|------------------|
| **FAST** | 1x | 1x |
| **BALANCED** | 2-3x | 2-5x |
| **DEEP RESEARCH** | 5-10x | 10-30x |
| **VERIFICATION** | 3-5x | 5-15x |
| **CREATIVE** | 4-8x | 10-30x |
| **HYBRID IR+R** | 3-6x | 5-20x |
| **DIAGNOSTIC** | 4-8x | Variable |

---

## Profile Applicability by Task

| Task Category | Primary Profile | Secondary Profiles |
|--------------|---------------|-------------------|
| **Retrieval** | FAST | HYBRID IR+R (for complex) |
| **Validation** | VERIFICATION | BALANCED |
| **Generation** | BALANCED | CREATIVE |
| **Analysis** | DEEP RESEARCH | HYBRID IR+R |
| **Synthesis** | DEEP RESEARCH | CREATIVE |
| **Explanation** | HYBRID IR+R | BALANCED |
| **Planning** | DEEP RESEARCH | CREATIVE |
| **Debugging** | DIAGNOSTIC | DEEP RESEARCH |

---

## Profile Selection Triggers

### Speed Priority Triggers
- User requested "quick check"
- Interactive editing session
- Batch processing mode
- Mobile/low-bandwidth context

### Quality Priority Triggers
- Safety-critical validation
- Final approval workflows
- Complex multi-system analysis
- Audit documentation

### Cost Priority Triggers
- Budget constraints
- High-volume batch operations
- Development/testing phases
- Non-critical review cycles

---

**Profile Taxonomy Status**: COMPLETE
**Total Profiles Defined**: 7

**Next**: Selection Criteria and Decision Matrix
