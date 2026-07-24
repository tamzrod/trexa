# AI-First Software Engineering Methodology

**Document ID**: METHODOLOGY-AI-FIRST-001
**Version**: 1.0.0
**Date**: 2026-07-23
**Status**: APPROVED
**Authority**: Human

---

## Purpose

This document defines the AI-First Software Engineering evaluation methodology for Trexa technology selection decisions.

---

## Background

Trexa adopts AI-First Software Engineering as its engineering methodology. This means:

- Development is primarily AI engineering agents and LLM-assisted
- Traditional human-centric evaluation criteria may be less relevant
- AI-specific criteria must be evaluated to determine technology suitability

This methodology was validated through:
- TREXA-INV-008: Initial programming language evaluation
- TREXA-INV-008A: AI-first methodology validation

---

## Core Principle

**Traditional human-centric evaluation criteria shall no longer be the primary methodology for Trexa technology selection.**

Programming language evaluations shall prioritize:
1. **Engineering Quality** — Type safety, maintainability, correctness
2. **AI-Assisted Software Evolution** — How AI agents can develop, maintain, and extend the technology

Over:
- Human learning curve
- Developer availability
- Hiring market
- Traditional development workflow

---

## Evaluation Criteria Framework

### Valid Criteria (Retained)

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| **Engineering Capability** | 25% | Core quality unchanged |
| **Ecosystem** | 15% | Package availability unchanged |
| **Web Compatibility** | 20% | Platform requirements unchanged |
| **Licensing & Sustainability** | 10% | Legal requirements unchanged |
| **Strategic Control** | 10% | Long-term independence unchanged |

### Replaced Criterion

| Traditional | Replaced With |
|-------------|---------------|
| Developer Productivity (20%) | AI-Enabled Productivity (20%) |

### New AI-First Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| AI Code Generation Quality | 10% | Quality of AI-generated code |
| AI Refactoring Reliability | 5% | Safety of AI refactoring |
| AI Debugging Effectiveness | 5% | AI debugging capability |

---

## AI-First Criteria Definitions

### AI-001: AI Code Generation Quality

**Definition**: Quality of AI-generated code in that language.

**Assessment Factors**:
- Training corpus size
- Type information availability
- Syntax clarity
- Pattern commonality

### AI-002: AI Refactoring Reliability

**Definition**: How reliably AI can refactor code safely.

**Assessment Factors**:
- Type safety enables safe refactoring
- IDE refactoring tool support
- Compilation catches errors
- Test coverage possibilities

### AI-003: AI Debugging Effectiveness

**Definition**: How effectively AI can debug issues.

**Assessment Factors**:
- Type information narrows causes
- Error message quality
- Stack trace clarity
- Runtime vs compile-time errors

### AI-004: AI Tooling Availability

**Definition**: Availability and quality of AI development tools.

**Assessment Factors**:
- Cursor, Copilot, Claude Code support
- Language server quality
- Agent implementation maturity

---

## Traditional Criteria That Are Deprecated

The following criteria should NOT dominate technology decisions:

| Deprecated Criterion | Reason |
|--------------------|--------|
| Human Learning Curve | AI agents don't have learning curves |
| Developer Availability | No hiring needed for AI agents |
| Hiring Market | No recruitment for AI development |
| Traditional Workflow | Agentic workflow differs |

**Note**: These may still be evaluated for completeness but should not be weighted heavily.

---

## Decision Matrix Template

| Criterion | Weight | Language A | Language B | Language C |
|----------|--------|------------|------------|-------------|
| Engineering Capability | 25% | X/10 | X/10 | X/10 |
| AI-Enabled Productivity | 20% | X/10 | X/10 | X/10 |
| Ecosystem | 15% | X/10 | X/10 | X/10 |
| Web Compatibility | 20% | X/10 | X/10 | X/10 |
| Licensing & Sustainability | 10% | X/10 | X/10 | X/10 |
| Strategic Control | 10% | X/10 | X/10 | X/10 |
| **TOTAL** | 100% | **X.XX** | **X.XX** | **X.XX** |

---

## Application Guidance

### When to Apply AI-First Methodology

| Scenario | Methodology |
|----------|-------------|
| Trexa technology selection | AI-First |
| Human-led development projects | Either (prefer AI-First) |
| External dependency evaluation | AI-First if AI-maintained |
| Runtime/framework selection | AI-First |

### When Traditional Criteria May Dominate

Only when explicitly required by human:
- Regulatory compliance requirements
- Specific vendor contracts
- Legacy system integration constraints
- Hardware-specific requirements

---

## Evidence Standards

### Required Evidence for AI-First Criteria

| Criterion | Evidence Type |
|-----------|--------------|
| AI Code Generation | LLM benchmark results, community reports |
| AI Refactoring | Type system analysis, case studies |
| AI Debugging | Error analysis, tooling documentation |
| AI Tooling | Official AI tool compatibility lists |

### Evidence Hierarchy

1. **Direct Evidence**: Benchmark data, performance metrics
2. **Indirect Evidence**: Community reports, documentation
3. **Inferential Evidence**: Language properties that imply AI capability

---

## Human Review Requirements

All AI-First evaluations require human review to confirm:

1. AI-first criteria are appropriately weighted
2. Traditional criteria reduction is justified
3. Recommendation aligns with project constraints
4. Evidence is sufficient for decision

---

## Revision History

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-23 | Initial approved version |

---

## Related Documents

| Document | Relationship |
|----------|-------------|
| TDR-002 | First application of AI-First methodology |
| TREXA-INV-008 | Initial validation |
| TREXA-INV-008A | Methodology validation |

---

**Document Status**: APPROVED
**Authority**: Human
**Review Date**: Upon significant AI engineering changes
