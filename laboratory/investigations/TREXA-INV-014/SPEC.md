# TREXA-INV-014: Engineering Entry & Decision Process Investigation

**ID**: TREXA-INV-014
**Title**: Engineering Entry & Decision Process Investigation
**Type**: Investigation
**Status**: COMPLETE
**Date**: 2026-07-24
**Author**: OpenHands Agent

---

## Precondition Verification

| Component | Status | Evidence |
|-----------|--------|----------|
| KDE Bootstrap | ✅ VERIFIED | config.yaml v1.0.0, bootstrap_date: 2026-07-24 |
| KDE Runtime | ✅ VERIFIED | state.json: "initialized", "ready", 9 modules loaded |

---

# 1. Engineering Entry Analysis

## 1.1 Current Entry Points

The repository currently has no explicit entry point definition. Work enters through:

| Entry Point | Source | Evidence |
|-------------|--------|----------|
| Human request | Human authorization | laboratory/README.md - "Human Authorization" |
| Investigation trigger | AI or Human | No formal trigger defined |
| Experiment trigger | Authorization | No formal trigger defined |
| Bug report | External | No formal process |
| Feature request | External | No formal process |

**Finding**: No systematic entry point model exists.

## 1.2 Current Routing Logic

From existing code (ai/classifier/classifier.py):

```
Task Input
    ↓
TaskCategory (31 categories)
    - RETRIEVAL_SIMPLE, RETRIEVAL_COMPLEX
    - VALIDATION_STANDARD, VALIDATION_SAFETY, VALIDATION_CRITICAL
    - GENERATION_SIMPLE, GENERATION_STANDARD, GENERATION_CREATIVE
    - ANALYSIS_STANDARD, ANALYSIS_COMPLEX
    - SYNTHESIS, EXPLANATION
    - PLANNING_SIMPLE, PLANNING_COMPLEX
    - DEBUGGING, DIAGNOSIS
    ↓
ComplexityLevel (5 levels)
    - TRIVIAL (1), LOW (2), MEDIUM (3), HIGH (4), VERY_HIGH (5)
    ↓
TaskCharacteristics
    - category, complexity, context_required, verification_level, safety_critical
```

**Finding**: AI classifier exists but routes to reasoning profiles, not to KDE workflows.

## 1.3 Current Workflow Assignment

From laboratory/README.md Engineering Principles:

| Principle | Implication |
|-----------|-------------|
| Evidence Over Intuition | All decisions need evidence |
| Investigation Before Implementation | Investigation always required |
| Human Authorization | Human approval always required |
| Traceability Always | Documentation always required |

**Finding**: Current principles imply ALL work requires full process, which is inefficient.

---

# 2. Classification Alternatives

## 2.1 Intent-Based Classification

| Intent | Definition | Example |
|--------|------------|---------|
| Bug | Defect correction | Fix NPE |
| Feature | New capability | Add zoom |
| Research | Knowledge gathering | Evaluate alternatives |
| Experiment | Hypothesis validation | Test approach |
| Investigation | Systematic analysis | Evaluate technology |
| Documentation | Information creation | Update README |
| Refactoring | Internal improvement | Rename variable |
| Architecture | Structural change | Redesign module |
| Governance | Policy change | New naming rule |
| Maintenance | Sustaining work | Dependency update |
| Emergency | Urgent response | Production hotfix |

**Pros**:
- Intuitive for humans
- Matches mental models
- Easy to determine

**Cons**:
- Doesn't indicate complexity
- Doesn't indicate risk
- Doesn't determine workflow

**Assessment**: Good starting point, insufficient alone.

## 2.2 Risk-Based Classification

| Risk Level | Definition | Example |
|------------|------------|---------|
| Trivial | No functional impact | Typo fix |
| Low | Minor, easily reversible | Format change |
| Medium | Moderate impact | New API endpoint |
| High | Significant impact | Architecture change |
| Critical | Safety/security | Security vulnerability |

**Pros**:
- Directly maps to verification effort
- Industry standard
- Balances speed and safety

**Cons**:
- Subjective determination
- Requires experience
- Risk can be underestimated

**Assessment**: Strong for workflow determination.

## 2.3 Scope-Based Classification

| Scope | Definition | Example |
|-------|------------|---------|
| File | Single file | One README |
| Module | Logical grouping | ai/routing |
| Subsystem | Major component | ai/ entire module |
| Repository | Whole repository | Major restructure |

**Pros**:
- Clear boundaries
- Impact visibility
- Parallel work enablement

**Cons**:
- Doesn't indicate complexity
- Scope can expand
- Doesn't map to workflow

**Assessment**: Useful for work breakdown, not workflow selection.

## 2.4 Impact-Based Classification

| Impact Type | Definition | Example |
|-------------|------------|---------|
| User | Affects end users | UI change |
| Knowledge | Changes understanding | New standards |
| Architecture | Structural impact | API redesign |
| Runtime | Affects execution | Performance |
| Repository | Governance/compliance | License change |

**Pros**:
- Shows consequence
- Prioritization support
- Stakeholder communication

**Cons**:
- Multiple impacts possible
- Difficult to categorize
- Doesn't determine workflow

**Assessment**: Good for prioritization, insufficient for workflow.

## 2.5 Recommended: Hybrid Classification

Based on evidence, a hybrid model combining Intent + Risk is optimal:

| Primary | Secondary | Purpose |
|---------|-----------|---------|
| Intent | What type of work | Workflow category |
| Risk | Impact severity | Verification rigor |

**Evidence**: ai/classifier/classifier.py already uses similar hybrid (category + complexity)

---

# 3. Decision Model Comparison

## 3.1 Model A: Classification → Decision → Workflow

```
Engineering Activity
    ↓
CLASSIFICATION
    Intent + Risk
    ↓
DECISION
    "What workflow applies?"
    ↓
WORKFLOW
    Assigned process
```

**Pros**:
- Simple mental model
- Fast routing
- Clear boundaries

**Cons**:
- Classification errors cascade
- Limited context consideration
- Rigid

**Assessment**: Fast but potentially inaccurate.

## 3.2 Model B: Question → Investigation → Decision → Workflow

```
Engineering Activity
    ↓
QUESTION
    "What is the right approach?"
    ↓
INVESTIGATION
    Systematic analysis
    ↓
DECISION
    Evidence-based conclusion
    ↓
WORKFLOW
    Based on decision
```

**Pros**:
- Thorough analysis
- Evidence-based
- Accommodates complexity

**Cons**:
- Slow
- Overhead for simple tasks
- Investigation for its own sake

**Assessment**: Thorough but inefficient for trivial work.

## 3.3 Model C: Hybrid Classification with Escalation

```
Engineering Activity
    ↓
INITIAL CLASSIFICATION
    (Intent + Risk quick assessment)
    ↓
┌─────────────────────────────────────────┐
│  IF TRIVIAL/LOW RISK                    │
│      ↓                                  │
│  DIRECT TO SIMPLE WORKFLOW              │
│      (Self-review, push)                │
│                                         │
│  IF MEDIUM/HIGH RISK                    │
│      ↓                                  │
│  INVESTIGATION REQUIRED                  │
│      ↓                                  │
│  DECISION RECORD                        │
│      ↓                                  │
│  FULL WORKFLOW                          │
└─────────────────────────────────────────┘
```

**Pros**:
- Fast for simple tasks
- Thorough for complex tasks
- Scalable
- Matches existing AI classifier pattern

**Cons**:
- Classification accuracy critical
- Escalation criteria must be clear
- May miss edge cases

**Assessment**: Best balance of speed and rigor.

---

# 4. Proposed Decision Tree

## 4.1 Minimal Decision Tree

The objective is the smallest number of decisions required to route correctly:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ENGINEERING ENTRY DECISION TREE                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  START: New engineering activity arrives                              │
│      │                                                               │
│      ▼                                                               │
│  ┌─────────────────────────────────────────┐                         │
│  │  DECISION 1: Is this work TRIVIAL?      │                         │
│  │                                                                  │ │
│  │  Criteria:                                                       │ │
│  │  • Single file change                                           │ │
│  │  • No functional behavior change                                 │ │
│  │  • Easily reversible                                             │ │
│  │  • No safety/security impact                                    │ │
│  │                                                                  │ │
│  │  Examples: Typo, format, comment, README                        │ │
│  │                                                                  │ │
│  └───────────────────┬─────────────────────────────────┘             │
│          YES         │         NO                                 │
│          │           │         │                                   │
│          ▼           │         ▼                                   │
│  ┌───────────────┐   │   ┌─────────────────────────────────┐        │
│  │  TRIVIAL      │   │   │  DECISION 2: What is the INTENT? │        │
│  │  WORKFLOW     │   │   │                                  │        │
│  │               │   │   │  • Bug                          │        │
│  │  AI → Push    │   │   │  • Feature                      │        │
│  │  (Self-review)│   │   │  • Investigation                │        │
│  └───────────────┘   │   │  • Research                     │        │
│                      │   │  • Documentation                │        │
│                      │   │  • Refactoring                  │        │
│                      │   │  • Architecture                  │        │
│                      │   │  • Governance                   │        │
│                      │   │  • Maintenance                  │        │
│                      │   │  • Emergency                    │        │
│                      │   └──────────┬──────────────────────┘        │
│                      │              │                                │
│                      │              ▼                                │
│                      │   ┌─────────────────────────────────┐        │
│                      │   │  DECISION 3: What is the RISK?    │        │
│                      │   │                                  │        │
│                      │   │  • Low (bug fix, refactor)       │        │
│                      │   │  • Medium (new feature)          │        │
│                      │   │  • High (architecture)           │        │
│                      │   │  • Critical (security)           │        │
│                      │   └──────────┬──────────────────────┘        │
│                      │              │                                │
│                      │              ▼                                │
│                      │   ┌─────────────────────────────────┐        │
│                      │   │  DECISION 4: Human required?     │        │
│                      │   │                                  │        │
│                      │   │  YES if:                         │        │
│                      │   │  • Medium+ risk                   │        │
│                      │   │  • Architecture change           │        │
│                      │   │  • Governance change             │        │
│                      │   │  • Unknown cause                 │        │
│                      │   │                                  │        │
│                      │   │  NO if:                          │        │
│                      │   │  • Low risk                      │        │
│                      │   │  • Known fix                     │        │
│                      │   │  • Trivial                      │        │
│                      │   └─────────────────────────────────┘        │
│                      │              │                                │
│                      │      ┌───────┴───────┐                       │
│                      │      ▼               ▼                       │
│                      │  ┌────────┐     ┌────────────┐               │
│                      │  │   NO   │     │    YES     │               │
│                      │  │        │     │            │               │
│                      │  │ Simple │     │ Investigation│              │
│                      │  │Workflow│     │ + Decision  │              │
│                      │  │        │     │ + Full     │              │
│                      │  │        │     │ Workflow   │               │
│                      │  └────────┘     └────────────┘               │
│                      │                                           │
└──────────────────────┴───────────────────────────────────────────┘
```

## 4.2 Decision Summary

| Decision | Question | Options | Outcome |
|----------|----------|---------|---------|
| 1 | Is it trivial? | Yes/No | Trivial workflow or continue |
| 2 | What is intent? | Bug/Feature/etc | Workflow category |
| 3 | What is risk? | Low/Medium/High/Critical | Verification rigor |
| 4 | Human required? | Yes/No | Delegation or autonomy |

**Total Decisions**: 4 (minimal)

---

# 5. Scenario Evaluation

## 5.1 Test Scenarios

| Scenario | Decision 1 | Decision 2 | Decision 3 | Decision 4 | Workflow |
|----------|-----------|-----------|-----------|-----------|----------|
| Typo correction | YES (trivial) | - | - | - | Trivial |
| README improvement | YES (trivial) | - | - | - | Trivial |
| Small bug fix | NO | Bug | Low | NO | Simple |
| Critical production bug | NO | Bug | Critical | YES | Investigation + Fix |
| Feature request | NO | Feature | Medium/High | YES | Investigation + TDR |
| Major architectural redesign | NO | Architecture | High | YES | Full KDE |
| Research idea | NO | Research | Medium | YES | Investigation |
| Scientific investigation | - | Investigation | - | YES | Full Investigation |
| Laboratory experiment | - | Experiment | - | YES | Full Experiment |
| Repository restructuring | NO | Architecture | High | YES | Full KDE |
| Governance update | NO | Governance | Medium | YES | Investigation + TDR |
| Performance optimization | NO | Feature | Medium | YES | Investigation + TDR |
| Security vulnerability | NO | Bug | Critical | YES | Emergency + Fix |

## 5.2 Scenario Path Verification

| Scenario | Expected Path | Correct? |
|----------|--------------|----------|
| Typo | Trivial → Direct | ✅ |
| README | Trivial → Direct | ✅ |
| Small bug | Low → Simple | ✅ |
| Critical bug | Investigation → Fix | ✅ |
| Feature | Investigation → TDR → Implementation | ✅ |
| Architecture | Full KDE | ✅ |
| Research | Investigation | ✅ |
| Experiment | Full Experiment | ✅ |
| Governance | Investigation → TDR | ✅ |
| Security | Emergency process | ✅ |

**Assessment**: All scenarios follow correct path.

---

# 6. Advantages and Disadvantages

## 6.1 Advantages

| Advantage | Evidence | Impact |
|-----------|----------|--------|
| Minimal decisions | 4 decisions only | Fast routing |
| Hybrid classification | Matches existing AI | Leverages investment |
| Trivial bypass | Observation of bottlenecks | Velocity improvement |
| Clear escalation | Risk-based | Quality preservation |
| Intent awareness | Workflow category | Appropriate rigor |
| Human involvement clarity | Explicit decision point | No ambiguity |

## 6.2 Disadvantages

| Disadvantage | Mitigation | Risk |
|--------------|------------|------|
| Classification errors | Clear criteria | Medium |
| Risk underestimation | Conservative defaults | Medium |
| Intent misclassification | Training/examples | Low |
| Decision tree maintenance | Document decisions | Low |
| Edge case handling | Exception process | Low |

---

# 7. Risks

## 7.1 Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Trivial misclassification | MEDIUM | HIGH | Conservative classification |
| Risk underestimation | MEDIUM | HIGH | Default to higher risk |
| Decision tree complexity | LOW | MEDIUM | Keep minimal (4 decisions) |
| Edge case bypass | LOW | MEDIUM | Exception handling |
| Human bottleneck | MEDIUM | MEDIUM | Clear delegation rules |

## 7.2 Risk Mitigation Strategy

| Risk | Strategy |
|------|----------|
| Classification errors | When uncertain, escalate to higher risk |
| Risk underestimation | Default to Medium when uncertain |
| Human bottleneck | Explicit NO paths for trivial/low |

---

# 8. Final Recommendation

## 8.1 Recommended Model

**Adopt Hybrid Classification with Escalation (Model C)**:

```
Engineering Activity
    ↓
Initial Classification (Intent + Risk)
    ↓
┌─────────────────────────────────────────┐
│  TRIVIAL → Direct (Self-review, push)  │
│  LOW + Known → Simple Workflow          │
│  MEDIUM+ or Unknown → Full Process      │
└─────────────────────────────────────────┘
```

## 8.2 Minimal Decision Tree Summary

| # | Decision | Purpose |
|---|----------|---------|
| 1 | Is trivial? | Bypass or continue |
| 2 | What intent? | Workflow category |
| 3 | What risk? | Verification rigor |
| 4 | Human required? | Delegation/Autonomy |

## 8.3 Integration with Existing AI

The proposed model complements existing ai/classifier/classifier.py:

| AI Classifier Output | Decision Tree Input |
|---------------------|--------------------|
| TaskCategory (31) | Intent classification |
| ComplexityLevel (5) | Risk classification |
| TaskCharacteristics | Decision support |

## 8.4 Comparison to Previous Investigation

TREXA-INV-013 proposed risk-gated workflows. This investigation refines the entry point:

| INV-013 Finding | INV-014 Refinement |
|----------------|-------------------|
| Risk-gated model | Entry point classification |
| Workflow selection | 4-decision routing |
| Missing trivial workflow | Explicit trivial bypass |

## 8.5 Next Step

This investigation provides the decision model. A future investigation or experiment should:

1. Formalize the classification criteria
2. Define the trivial/low thresholds
3. Create the exception handling process
4. Integrate with existing AI classifier

---

*Investigation completed per KDE Runtime governance*
*Awaiting human review for recommendation adoption*
