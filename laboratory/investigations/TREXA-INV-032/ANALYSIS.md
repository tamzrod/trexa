# Investigation Analysis: TREXA-INV-032

**Investigation**: TREXA-INV-032
**Title**: Repository Architecture and Separation of Concerns Investigation
**Status**: IN_PROGRESS

---

# PART 1: THREE-LAYER ARCHITECTURE DEFINITION

## 1.1 Layer Definitions

### Layer 1: Engineering Knowledge (KDE)

**Purpose**: Document why decisions were made and what evidence supports them.

| Attribute | Value |
|-----------|-------|
| Owner | Engineering team |
| Contents | Investigations, TDRs, specifications, principles |
| Questions | Why? What evidence? What guidance? |
| Format | Markdown, diagrams, documents |
| Dependencies | None (foundation layer) |

**Examples**:
- `/laboratory/investigations/` - Investigation documents
- `/laboratory/decisions/` - Technology Decision Records
- `/laboratory/methodology/` - Engineering principles
- `/laboratory/evidence/` - Supporting evidence
- `/laboratory/reviews/` - Design reviews

### Layer 2: Software Development

**Purpose**: Implement software according to engineering guidance.

| Attribute | Value |
|-----------|-------|
| Owner | Development team |
| Contents | Source code, tests, build system |
| Questions | How? How organized? How tested? |
| Format | Code, scripts, configuration |
| Dependencies | Layer 1 (reads KDE for guidance) |

**Examples**:
- `/src/` - Source code
- `/tests/` - Test files
- `/build/` - Build configuration
- `/package.json` - Package manifest
- `/tsconfig.json` - TypeScript configuration

### Layer 3: Software Deployment

**Purpose**: Deliver software to users.

| Attribute | Value |
|-----------|-------|
| Owner | DevOps/Platform team |
| Contents | Dockerfiles, installers, scripts |
| Questions | How installed? How upgraded? How distributed? |
| Format | Docker, scripts, configuration |
| Dependencies | Layer 2 (builds software) |

**Examples**:
- `/docker/` - Docker configurations
- `/deploy/` - Deployment scripts
- `/scripts/` - Installation scripts
- `/kubernetes/` - K8s manifests
- `/.github/workflows/` - CI/CD pipelines

## 1.2 Dependency Direction

```
┌─────────────────────────┐
│   LAYER 1: KDE          │  Engineering Knowledge
│   (Investigations, TDRs) │  WHY decisions were made
└─────────────┬───────────┘
              │ Reads guidance
              ▼
┌─────────────────────────┐
│   LAYER 2: Development  │  Software Implementation
│   (Source, Tests)       │  HOW to implement
└─────────────┬───────────┘
              │ Builds
              ▼
┌─────────────────────────┐
│   LAYER 3: Deployment  │  Software Delivery
│   (Docker, Scripts)     │  WHERE to deliver
└─────────────────────────┘
```

**Rule**: Dependencies flow downward only. Reverse dependencies are prohibited.

---

# PART 2: CURRENT STATE ANALYSIS

## 2.1 Current Directory Assessment

| Directory | Current Layer | Assessment |
|-----------|--------------|------------|
| `laboratory/` | Layer 1: KDE | ✅ Correct |
| `ai/` | Layer 2: Development | ✅ Correct |
| `docs/` | Mixed | ⚠️ Needs clarification |
| `LICENSE` | Metadata | Neutral |
| `README.md` | Documentation | Neutral |

## 2.2 Current Issues

| Issue | Description | Severity |
|-------|-------------|----------|
| Mixed docs | `/docs/` contains both application and KDE docs | LOW |
| No deployment layer | Deployment configs not visible | MEDIUM |
| No src structure | `/ai/` is source but named for AI specifically | LOW |

---

# PART 3: PROPOSED REPOSITORY ORGANIZATION

## 3.1 Recommended Structure

```
/trexa/
├── README.md                      # Project overview
├── LICENSE                       # License
│
├── kde/                          # Layer 1: Engineering Knowledge
│   ├── laboratory/               # Investigations, decisions
│   │   ├── investigations/
│   │   ├── decisions/
│   │   ├── methodology/
│   │   ├── evidence/
│   │   ├── experiments/
│   │   ├── implementations/
│   │   └── reviews/
│   ├── principles/               # Engineering principles
│   ├── architecture/             # Architecture documentation
│   └── kde.md                    # KDE documentation guide
│
├── src/                          # Layer 2: Software Development
│   ├── main/                     # Main application source
│   ├── renderer/                 # Frontend (React)
│   ├── backend/                  # Backend services
│   ├── shared/                   # Shared libraries
│   ├── ai/                      # AI module
│   ├── tests/                   # Integration tests
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── jest.config.js
│
├── deploy/                       # Layer 3: Software Deployment
│   ├── docker/                   # Docker configurations
│   │   ├── Dockerfile
│   │   ├── docker-compose.yml
│   │   └── .dockerignore
│   ├── kubernetes/               # K8s manifests
│   ├── scripts/                  # Deployment scripts
│   ├── ci/                      # CI/CD configurations
│   │   └── .github/
│   │       └── workflows/
│   └── packaging/                # OS-specific packages
│
└── docs/                        # User documentation
    ├── user-guide/
    ├── api-reference/
    └── release-notes/
```

## 3.2 Layer Responsibilities

### Layer 1: kde/

| Directory | Purpose |
|-----------|---------|
| `laboratory/` | Investigations, TDRs, experiments |
| `principles/` | Engineering principles |
| `architecture/` | System architecture docs |

### Layer 2: src/

| Directory | Purpose |
|-----------|---------|
| `main/` | Core application logic |
| `renderer/` | React UI components |
| `backend/` | Server-side code |
| `shared/` | Shared utilities/types |
| `ai/` | AI module implementation |

### Layer 3: deploy/

| Directory | Purpose |
|-----------|---------|
| `docker/` | Container configurations |
| `kubernetes/` | K8s deployments |
| `scripts/` | Deployment scripts |
| `ci/` | CI/CD pipelines |
| `packaging/` | OS packages |

---

# PART 4: DEPENDENCY ANALYSIS

## 4.1 Allowed Dependencies

| From | To | Reason |
|------|----|--------|
| Layer 2 (src) | Layer 1 (kde) | Reads guidance |
| Layer 3 (deploy) | Layer 2 (src) | Builds software |
| Layer 3 (deploy) | Layer 1 (kde) | References standards |

## 4.2 Forbidden Dependencies

| From | To | Reason |
|------|----|--------|
| Layer 1 (kde) | Layer 2 (src) | Would create coupling |
| Layer 1 (kde) | Layer 3 (deploy) | Would create coupling |
| Layer 2 (src) | Layer 3 (deploy) | Would limit portability |

## 4.3 Dependency Rules

1. **KDE does not depend on Development or Deployment**
   - Engineering knowledge is timeless
   - Technology choices shouldn't affect principles

2. **Development reads KDE but doesn't depend on it**
   - KDE provides guidance
   - Source code implements decisions

3. **Deployment builds from Development output**
   - Layer 3 packages Layer 2 artifacts
   - No source code dependency

---

# PART 5: PLATFORM INDEPENDENCE ANALYSIS

## 5.1 Operating System Independence

| Concern | Implementation | Status |
|---------|---------------|--------|
| Source code | OS-agnostic (TypeScript, Python) | ✅ |
| Build system | Cross-platform (Vite, npm) | ✅ |
| Tests | Cross-platform (Vitest) | ✅ |
| Deployment | Platform-specific (Docker) | ⚠️ |

**Principle**: Source code and build are OS-agnostic. Deployment may be OS-specific.

## 5.2 Development Environment Independence

| Environment | Support | Implementation |
|-------------|---------|----------------|
| Windows | Yes | Standard tooling |
| Linux | Yes | Standard tooling |
| macOS | Yes | Standard tooling |
| WSL | Yes | Linux tooling |
| Remote | Yes | SSH + standard tools |
| Container | Yes | Dev container definition |

## 5.3 Deployment Target Independence

| Target | Support | Implementation |
|--------|---------|----------------|
| Native executable | Yes | Tauri builds |
| Docker | Yes | Dockerfile |
| Kubernetes | Yes | K8s manifests |
| Portable | Yes | Portable package |
| Installer | Yes | Platform installers |

**Principle**: Application architecture unchanged regardless of deployment target.

---

# PART 6: ARCHITECTURAL PRINCIPLES

## 6.1 Core Principles

### Principle 1: Separation of Concerns

Layer 1, Layer 2, and Layer 3 are logically independent.

**Evidence**: Each layer answers different questions (Why? How? Where?).

### Principle 2: Dependency Hierarchy

Dependencies flow downward only.

```
KDE → Development → Deployment
```

**Evidence**: Engineering decisions guide implementation. Implementation is packaged for delivery.

### Principle 3: Platform Agnosticism

Source code is independent of OS, IDE, and deployment target.

**Evidence**: TypeScript, Python, and standard tooling work on all platforms.

### Principle 4: KDE Longevity

Engineering knowledge outlives technology choices.

**Evidence**: Investigations document why decisions were made, not just what was built.

## 6.2 Supporting Principles

| Principle | Description |
|-----------|-------------|
| KDE First | Engineering guidance precedes implementation |
| Clean Architecture | Dependencies point inward |
| Immutable Artifacts | Deployment consumes artifacts, not source |
| Documentation Co-location | Docs live with what they document |

---

# PART 7: COMPARATIVE ANALYSIS

## 7.1 Monorepo vs Polyrepo

| Aspect | Monorepo | Polyrepo | Trexa Decision |
|--------|----------|----------|---------------|
| Governance | Centralized | Distributed | Monorepo |
| Shared dependencies | Easy | Hard | Monorepo |
| Cross-cutting changes | Simple | Complex | Monorepo |
| CI/CD | Complex | Simple | Manageable |
| Team autonomy | Limited | High | Layer-based |

**Decision**: Monorepo with clear layer separation.

## 7.2 Layered Repository Patterns

### Pattern A: Layered by Type

```
/repo
  /knowledge      # Layer 1
  /source         # Layer 2
  /distribution   # Layer 3
```

**Assessment**: Simple, clear separation.

### Pattern B: Layered by Concern

```
/repo
  /kde           # Layer 1
  /app           # Layer 2
  /ops           # Layer 3
```

**Assessment**: More descriptive names.

### Pattern C: Hybrid

```
/repo
  /laboratory    # Layer 1 (current)
  /src           # Layer 2 (proposed)
  /deploy        # Layer 3 (proposed)
```

**Assessment**: Evolution of current structure. RECOMMENDED.

---

# PART 8: MIGRATION STRATEGY

## 8.1 Current to Proposed

| Step | Action | Risk |
|------|--------|------|
| 1 | Create `/kde/` directory | LOW |
| 2 | Move `laboratory/` to `/kde/` | LOW |
| 3 | Create `/src/` directory | LOW |
| 4 | Move `ai/` to `/src/ai/` | MEDIUM |
| 5 | Create `/deploy/` directory | LOW |
| 6 | Add deployment configs | LOW |
| 7 | Update references | MEDIUM |

## 8.2 Migration Order

1. Create new structure (no changes to existing)
2. Move files to new structure
3. Update documentation
4. Update CI/CD
5. Update IDE configurations

---

**Analysis Status**: IN_PROGRESS

**Next**: Complete CONCLUSION.md
