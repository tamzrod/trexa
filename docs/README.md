# Trexa Documentation

**Version**: 1.0.0
**Architecture**: Tripartite Documentation (per TREXA-INV-020)
**Status**: Approved

---

## Documentation Overview

This directory contains all human-readable documentation for Trexa, organized into two primary domains:

| Domain | Location | Purpose |
|--------|----------|---------|
| **Application** | `application/` | Product documentation for users and developers |
| **KDE Methodology** | `kde/` | Engineering methodology and principles |

## Quick Navigation

### For Users and Developers

| Topic | Location |
|-------|----------|
| Product Overview | [application/README.md](application/README.md) |
| Getting Started | [application/getting-started/](application/getting-started/) |
| User Guides | [application/guides/](application/guides/) |
| API Documentation | [application/api/](application/api/) |
| Architecture | [application/architecture/](application/architecture/) |

### For Engineers and AI Agents

| Topic | Location |
|-------|----------|
| KDE Methodology | [kde/methodology/](kde/methodology/) |
| Engineering Principles | [kde/principles/](kde/principles/) |
| Governance Policies | [kde/governance/](kde/governance/) |
| Runtime Concepts | [kde/runtime-concepts/](kde/runtime-concepts/) |

## Documentation Architecture

```
docs/
├── application/              # Product documentation
│   ├── README.md            # Product overview
│   ├── getting-started/      # Quick start guides
│   ├── guides/              # User guides
│   ├── api/                 # API documentation
│   ├── reference/            # Technical reference
│   ├── architecture/         # Product architecture
│   └── roadmap/             # Product roadmap
│
└── kde/                     # KDE methodology
    ├── README.md            # KDE methodology overview
    ├── methodology/         # AI-First methodology
    ├── principles/          # Engineering principles
    ├── governance/          # Governance policies
    ├── runtime-concepts/    # KDE runtime concepts
    ├── reviews/             # KDE reviews
    └── history/             # KDE evolution history
```

## Related Documentation

| Documentation | Location | Purpose |
|--------------|----------|---------|
| **Engineering Laboratory** | `laboratory/` | Evidence-based decisions and investigations |
| **KDE Runtime** | `.kde/` | Runtime framework (not human-readable) |
| **Source Code** | `src/` | Implementation (future) |

## Contributing to Documentation

### Documentation Types

| Type | Location | Owner |
|------|----------|-------|
| Product docs | `application/` | Product Owner |
| Methodology | `kde/methodology/` | Engineering Lead |
| Governance | `kde/governance/` | KDE Governance |

### Guidelines

1. **Single Source**: Each topic exists in one authoritative location
2. **Cross-Reference**: Use explicit links between domains
3. **Consumer-Focused**: Write for the intended audience
4. **Evidence-Based**: Engineering decisions reference `laboratory/`

---

*Documentation architecture per TREXA-INV-020*
*Approved: 2026-07-24*
