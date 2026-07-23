# Trexa

**A Visual Engineering Platform for AI-Assisted Diagram Creation**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Overview

Trexa is a next-generation visual engineering platform designed for creating engineering diagrams using a WYSIWYG (What You See Is What You Get) interface. The platform combines the precision of traditional CAD tools with the power of AI-assisted engineering to accelerate the diagram creation process.

### Vision

Trexa aims to transform how engineering diagrams are created and maintained by:

- Providing an intuitive, visual interface for diagram creation
- Leveraging AI to understand engineering semantics
- Supporting multiple engineering domains from a common foundation
- Enabling teams to create, validate, and iterate on diagrams faster

### Goals

1. **Reduce Diagram Creation Time** — AI-assisted features accelerate diagram creation
2. **Improve Diagram Quality** — Engineering validation catches errors early
3. **Support Multiple Domains** — Common architecture for SLD, GIS, P&ID, and more
4. **Enable Team Collaboration** — Shared knowledge and consistent standards
5. **Maintain Long-term viability** — Open-source, extensible, and sustainable

---

## Key Features

### Core Features

| Feature | Description |
|---------|-------------|
| **WYSIWYG Editing** | Real-time visual editing of engineering diagrams |
| **Drag-and-Drop** | Intuitive primitive placement |
| **Connection Management** | Automatic connection routing and validation |
| **State Visualization** | Real-time display of equipment states |
| **Multi-Domain Support** | SLD, GIS, and extensible to P&ID, SCADA |

### AI Features

| Feature | Description |
|---------|-------------|
| **Smart Routing** | AI determines optimal reasoning profiles |
| **Domain Validation** | Engineering rules enforced automatically |
| **Intelligent Suggestions** | Context-aware recommendations |
| **Telemetry** | Continuous improvement through usage data |

---

## Current Status

### Development Phase

**Phase**: Pre-Implementation Foundation

The project is currently establishing its architectural foundation through systematic investigation and evidence-based decision-making.

### What's Complete

| Category | Status | Evidence |
|----------|--------|----------|
| Domain Definition | ✅ Complete | TREXA-INV-006 (SLD Domain) |
| Platform Capabilities | ✅ Complete | TREXA-INV-002 (34 capabilities) |
| AI Architecture | ✅ Complete | TREXA-INV-003 (AI Routing) |
| Technology Selection | 🔄 In Progress | TDR-001, TDR-002, TDR-003 |
| Foundation Architecture | ✅ Complete | TREXA-INV-011 (Core Concepts) |

### Approved Technology Stack

| Layer | Technology | Decision |
|-------|------------|----------|
| **Renderer** | JointJS | TDR-001 |
| **Language** | TypeScript | TDR-002 |
| **Framework** | React | TDR-003 |
| Build | TBD | Pending |
| State Management | TBD | Pending |
| Styling | TBD | Pending |

*Note: Full technology stack will be documented as decisions are approved.*

---

## Repository Philosophy

### Evidence-Based Development

Trexa follows an evidence-based approach to software development:

1. **Investigation Before Implementation** — Every significant decision is investigated
2. **KDE Governance** — All decisions pass through the Knowledge Discovery Engine
3. **Human Authorization** — Humans retain final approval authority
4. **Transparent Reasoning** — All decisions are documented with evidence

### Investigation Lifecycle

```
┌─────────────────────────────────────────────────────────┐
│                    INVESTIGATION                         │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐                │
│  │ Research │ → │ Analyze │ → │ Conclude │               │
│  └─────────┘   └─────────┘   └─────────┘                │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    HUMAN REVIEW                           │
│  ┌─────────────┐   ┌─────────────┐                      │
│  │  Approved  │ or │  Rejected   │                      │
│  └─────────────┘   └─────────────┘                      │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    DECISION RECORD                        │
│  ┌─────────────────────────────────────────┐            │
│  │  Technology Decision Record (TDR)        │            │
│  └─────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

---

## Development Methodology

### AI-First Engineering

Trexa embraces AI-First Software Engineering as its development methodology:

- **AI as Primary Developer** — AI agents handle most implementation
- **Human as Approver** — Humans review and authorize decisions
- **Structured Workflow** — Investigations, decisions, implementations

### KDE Integration

Trexa is governed by the Knowledge Discovery Engine (KDE), which provides:

- Systematic investigation framework
- Evidence-based decision making
- Transparent reasoning chains
- Continuous learning and improvement

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Evidence Over Intuition** | Decisions grounded in verifiable evidence |
| **Experiment Before Deployment** | Validate knowledge before operational use |
| **Preserve Ambiguity** | Do not prematurely resolve uncertainty |
| **Traceability Always** | Every conclusion traces to evidence |
| **Reproducibility Required** | All experiments must be reproducible |

---

## Getting Started

### Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| Node.js | 18+ | For frontend development |
| Python | 3.10+ | For AI module |
| Git | Latest | Version control |

### Installation

```bash
# Clone the repository
git clone https://github.com/tamzrod/trexa.git
cd trexa

# Install dependencies (pending project setup)
npm install
```

### Development Workflow

1. **Review Approved Decisions** — Check `laboratory/decisions/`
2. **Read Relevant Investigations** — Check `laboratory/investigations/`
3. **Follow Architecture** — Reference `laboratory/investigations/TREXA-INV-011.md`
4. **Implement with AI** — Use Cursor, Copilot, or Claude Code

---

## Repository Structure

```
trexa/
├── .kde/                    # Knowledge Discovery Engine runtime
│   ├── engines/             # KDE engine implementations
│   ├── experts/             # Domain expert knowledge
│   └── knowledge/           # Engineering knowledge base
│
├── ai/                     # AI routing module
│   ├── profiles/           # Reasoning profiles
│   ├── classifier/          # Task classification
│   ├── routing/             # Routing engine
│   ├── ir/                  # Information retrieval
│   └── telemetry/           # Telemetry system
│
├── laboratory/             # Investigation and decision records
│   ├── decisions/           # Technology Decision Records (TDRs)
│   ├── investigations/      # Investigation documents
│   ├── methodology/          # Development methodology
│   ├── experiments/          # Laboratory experiments
│   └── validations/         # Validation records
│
├── src/                    # Source code (pending)
│
├── README.md               # This document
├── LICENSE                # MIT License
└── .gitignore             # Git ignore rules
```

### Key Directories

| Directory | Purpose |
|-----------|---------|
| `.kde/` | KDE runtime and knowledge |
| `ai/` | AI routing and intelligence |
| `laboratory/` | Investigations and decisions |
| `src/` | Source code (to be created) |

---

## Roadmap

### Phase 1: Foundation (Current)

- [x] Domain definition (SLD)
- [x] Technology decisions (JointJS, TypeScript, React)
- [x] Foundation architecture
- [ ] Build tooling selection
- [ ] Project structure

### Phase 2: Core Implementation

- [ ] JointJS integration
- [ ] React component architecture
- [ ] Document model implementation
- [ ] Basic SLD primitives

### Phase 3: SLD MVP

- [ ] Circuit breaker primitive
- [ ] Disconnect switch primitive
- [ ] Busbar primitive
- [ ] Connection creation
- [ ] State visualization

### Phase 4: AI Integration

- [ ] AI module integration
- [ ] Profile selection UI
- [ ] Telemetry dashboard
- [ ] Intelligent suggestions

### Phase 5: Multi-Domain

- [ ] GIS domain
- [ ] Domain switching
- [ ] Custom domain support

---

## Contributing

### How to Contribute

1. **Read the Documentation** — Start with this README and approved TDRs
2. **Understand the Methodology** — Review `laboratory/methodology/`
3. **Follow the Investigation Process** — Don't implement without investigation
4. **Get Human Approval** — Significant changes require human authorization

### Contribution Types

| Type | Process |
|------|---------|
| Bug Reports | Open issue with evidence |
| Feature Requests | Propose via investigation |
| Documentation | Submit PR with updates |
| Code Changes | Implement after approval |

### Important Guidelines

- **Evidence Required** — All proposals need supporting evidence
- **KDE Process** — Follow investigation lifecycle
- **Human Authorization** — Major changes need human approval
- **AI-Friendly** — Write for AI comprehension

---

## License

Trexa is open-source software released under the [MIT License](LICENSE).

### License Summary

| Right | Status |
|-------|--------|
| Commercial use | ✅ Allowed |
| Modification | ✅ Allowed |
| Distribution | ✅ Allowed |
| Private use | ✅ Allowed |
| Attribution | ✅ Required |

---

## Credits

### Project Governance

| Role | Description |
|------|-------------|
| **Human Authority** | Final decision-maker on all significant changes |
| **KDE Runtime** | Knowledge Discovery Engine for investigation |
| **AI Agents** | Primary implementers of approved features |

### Technology Foundations

Trexa builds upon the following technologies:

- **JointJS** — SVG-based diagramming library
- **React** — UI framework
- **TypeScript** — Programming language
- **KDE** — Knowledge Discovery Engine methodology

### Knowledge Sources

Trexa's engineering knowledge is derived from validated domain expertise:

- **KDE SLD Expert** — Single Line Diagram specifications
- **IEEE Standards** — Electrical engineering standards
- **IEC Standards** — International electrotechnical standards

---

## Further Reading

| Document | Description |
|----------|-------------|
| [TREXA-INV-006](laboratory/investigations/TREXA-INV-006.md) | SLD Domain Definition |
| [TREXA-INV-011](laboratory/investigations/TREXA-INV-011.md) | Foundation Architecture |
| [AI-FIRST-METHODOLOGY](laboratory/methodology/AI-FIRST-METHODOLOGY.md) | Development Methodology |
| [TDR-001](laboratory/decisions/TDR-001.md) | JointJS Decision |
| [TDR-002](laboratory/decisions/TDR-002.md) | TypeScript Decision |
| [TDR-003](laboratory/decisions/TDR-003.md) | React Decision |

---

## Contact

For questions or discussions about Trexa:

- **Issues** — Use GitHub Issues for bugs and feature requests
- **Discussions** — Use GitHub Discussions for questions

---

*Last updated: 2026-07-23*
*Version: 0.1.0*
