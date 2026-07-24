# Getting Started with Trexa

**Domain**: Application Documentation
**Audience**: Users and Developers

---

## Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

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

---

## Development Workflow

### 1. Review Approved Decisions

Technology decisions are documented in the Engineering Laboratory:

```
laboratory/
└── decisions/
    ├── TDR-001.md   # JointJS (Renderer)
    ├── TDR-002.md   # TypeScript (Language)
    └── TDR-003.md   # React (Framework)
```

### 2. Understand the Architecture

Architecture documentation is available at:

- [Foundation Architecture](..//laboratory/investigations/TREXA-INV-011/README.md)
- [Core Concepts](..//laboratory/investigations/TREXA-INV-011/SPEC.md)

### 3. Follow the Methodology

Trexa uses AI-First Software Engineering. Review the methodology:

- [AI-First Methodology](../kde/methodology/)
- [Engineering Principles](../kde/principles/)

### 4. Implement with AI

Trexa embraces AI-assisted development:

- **Cursor** — Primary AI development environment
- **Copilot** — Code completion
- **Claude Code** — Architecture and implementation assistance

---

## Project Structure

```
trexa/
├── .kde/                    # Knowledge Discovery Engine
├── ai/                      # AI routing module
├── docs/                    # This documentation
├── laboratory/              # Engineering evidence
├── src/                     # Source code (future)
├── README.md                # Project entry point
└── LICENSE                  # MIT License
```

---

## Next Steps

| Goal | Resource |
|------|----------|
| Learn about Trexa | [Application README](../README.md) |
| Understand the methodology | [KDE Methodology](../kde/methodology/) |
| View architecture | [Architecture](../architecture/) |
| Explore decisions | [Laboratory Decisions](../../laboratory/decisions/) |
| Contribute | [Contributing Guide](../..#contributing) |

---

*Getting started guide per TREXA-INV-020*
