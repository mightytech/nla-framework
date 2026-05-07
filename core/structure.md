# Framework Structure

This document is the framework's *as-built* directory record — what's
here, why it's here, and where each piece came from. It exists so future
sessions can place files correctly without re-deriving the layout, and so
structural change happens with a checkpoint and a record rather than
silently.

The discipline behind this file lives in `CLAUDE.md` ("Structural change
discipline"). The shape — every entry attributed to a source or
`[judgment]` with rationale, **Judgment note** callouts for non-obvious
tradeoffs, Decision Sources table at the bottom — borrows from
facebook-moderation's compile-time `build-guide.md`. See also
`reference/design-rationale.md` (the "Structure Decisions Protocol"
entry) for the design reasoning, and
`reference/experiments/structure-decisions-protocol/experiment-report.md`
for the empirical validation.

---

## Project Tree

```
nla-framework/
├── CLAUDE.md                  # Framework runtime identity and modes
├── README.md                  # Developer-facing introduction
├── CONTRIBUTING.md            # How to contribute (NLA-shaped contribution flow)
├── LICENSE                    # MIT license
├── VERSION                    # Framework version string
├── config.md                  # Framework maintainer's preferences (gitignored)
├── config-spec.md             # What's configurable in the framework
├── config/                    # Sub-config files (gitignored)
├── .gitignore                 # Excludes config.md, config/
├── .gitmodules                # Submodule pointers
├── .claude/skills/            # Skill wrappers Claude Code discovers
├── core/                      # Universal NLA infrastructure (consumer-facing)
│   ├── nla-foundations.md     # NLA concepts and principles
│   ├── README.md              # core/ orientation
│   ├── structure.md           # This file
│   └── skills/                # Skill logic files
├── install/                   # Intent files (source of truth for project generation)
├── lib/                       # Traditional code helpers (e.g., export.py)
├── packages/                  # Submodule dependencies (penny-post, process-helpers)
└── reference/                 # Framework maintenance records (internal-only)
    ├── design-rationale.md
    ├── friction-log.md
    ├── friction-log-archive.md
    ├── feedback-log.md
    ├── feedback-log-archive.md
    ├── installed-packages.md
    ├── designs/               # Design documents
    ├── experiments/           # Experiment reports
    ├── feedback/              # Feedback letters drafts/archives
    ├── plans/                 # Warm-context plans for later-session execution
    ├── sessions/              # Maintenance session logs
    ├── specs/                 # Specifications
    └── standards/             # Quality standards (writing, etc.)
```

---

## Top-Level Files

| Path | Purpose | Attribution |
|------|---------|-------------|
| `CLAUDE.md` | Framework's runtime identity. Sets default mode (project creation), maintenance mode entry, and global behavioral discipline (skill invocation, structural change). Loaded automatically by Claude Code at session start. | `[framework default]` (analog to domain projects' CLAUDE.md). Dual-mode pattern per design rationale "Dual-Mode Framework CLAUDE.md" (2026-02-18). |
| `README.md` | Developer-facing introduction — what NLAs are, getting started, the thin wrapper pattern, structure overview. | `[judgment]` — every framework needs a README. Content shape mirrors `install/structure-intent.md`'s README guidance for domain projects. |
| `CONTRIBUTING.md` | Contribution flow. Explains why this project doesn't accept PRs and how to contribute via observations and friction logs. | `[judgment]` — added to make the non-traditional contribution model explicit to outside contributors. |
| `LICENSE` | MIT license. | `[git/repo convention]` |
| `VERSION` | Framework version string. | `[git/repo convention]` |
| `config.md` | Framework maintainer's preferences (e.g., maintenance verbosity). Gitignored. | `[framework default]` per `install/structure-intent.md` "Configuration Files." |
| `config-spec.md` | Specification of what's configurable. | `[framework default]` per `install/structure-intent.md`. |
| `.gitignore` | Excludes `config.md`, `config/`. | `[framework default]` per `install/structure-intent.md`. |
| `.gitmodules` | Submodule pointers (penny-post, process-helpers). | `[git/repo convention]`, populated by the packages migration (design rationale 2026-04-15 "The new model" — sibling-to-submodules). |

**Judgment note (config files in framework root):** Domain projects'
`config.md` is the user's preferences. The framework's `config.md` is
the framework maintainer's preferences for how `/maintain`, `/create-app`,
etc. behave when running *in* the framework. Same mechanism, different
audience.

---

## `core/`

Universal NLA infrastructure. Every domain project consumes this via
`packages/nla-framework/core/`. Highest blast radius in the framework —
changes here affect every NLA on next `/update`.

| Path | Purpose | Attribution |
|------|---------|-------------|
| `core/nla-foundations.md` | NLA concepts, principles, and working rhythms. Loaded at startup by every domain project via `/startup`. The shared mental model. | `[design rationale: "core/ for Framework Executable Docs"]` (separates infrastructure from domain content). |
| `core/README.md` | Orientation for the `core/` directory itself. | `[judgment]` — short directory-level orientation pattern (one of the few READMEs inside `core/`). |
| `core/structure.md` | This file — the framework's as-built structure record. | `[design rationale: "Structure Decisions Protocol" 2026-05-07]`. Borrowed shape from facebook-moderation's `lib/ingest-build-o/build-guide.md`. |
| `core/skills/` | Skill logic files that domain project wrappers delegate to. 21 files covering universal skills (maintain, install, update, friction-log, debrief, close, etc.) plus the validate skill family. | `[design rationale: "Thin Wrapper Skills"]` and `[design rationale: "Framework Self-Maintenance"]`. |
| `core/skills/README.md` | Orientation for skill authoring (registration steps, intent file updates). Referenced from `/maintain` "Adding a New Skill" common task. | `[judgment]` — added during the 2026-02-19 maintenance session that surfaced the "Adding a New Skill" checklist gap (now archived friction entry). |

**Judgment note (validate skill family):** The validate skill is split
across `validate.md` (entry/dispatch) and per-mode files
(`validate-architecture.md`, `validate-coherence.md`,
`validate-debug.md`, `validate-scenario.md`, `validate-standards.md`,
`validate-structural.md`). Each per-mode file is self-contained.
Splitting was a judgment call to keep individual mode logic readable —
not documented in design rationale, but the precedent is clear from the
file naming.

---

## `install/`

Intent files — single source of truth for what `/create-app`, `/install`,
and `/update` need. Domain-agnostic descriptions of what NLAs should
have, not literal templates.

| Path | Purpose | Attribution |
|------|---------|-------------|
| `install/install.md` | The package manifest — what the framework provides at install time, prerequisites, integration points. Read by `/install` when this framework is installed into a project. | `[design rationale: "Intent Files as Single Source of Truth"]`. |
| `install/CLAUDE-intent.md` | What runtime identity an NLA's CLAUDE.md should establish. | Same. |
| `install/structure-intent.md` | What directory structure and reference files an NLA needs. The prescriptive analog of the present file. | Same. |
| `install/skills-intent.md` | Skill wrappers and reference implementations. | Same. |
| `install/package-intent.md` | What an NLA package should expose to `/install` and `/update`. | Same; refined in the packages migration session 2026-04-15. |
| `install/example-catalog.md` | Catalog of example NLA projects backing `/install-app`. | Created when `/install-app` replaced `/create-sample-app` (2026-02 era). |
| `install/update-notes.md` | Running changelog for consumers — what changed, what to know, optional mirror updates. | `[design rationale: "Update Notes" entry]` (added when the convention emerged). |
| `install/README.md` | Orientation for `install/` and intent file format. | `[judgment]`. |

---

## `reference/`

Framework maintenance records. Internal-only — not shipped to consumers.
The non-executing channel (read during `/maintain`, not during normal
operation).

### Top-level reference files

| Path | Purpose | Attribution |
|------|---------|-------------|
| `reference/design-rationale.md` | *Why* the framework is built the way it is. Captures decisions, alternatives considered, and trade-offs. | `[framework default]` per `install/structure-intent.md`. |
| `reference/friction-log.md` | Internal observations awaiting resolution. | Same. |
| `reference/friction-log-archive.md` | Resolved/closed friction entries. | Same. |
| `reference/feedback-log.md` | External feedback accepted in triage, awaiting implementation. | Same. |
| `reference/feedback-log-archive.md` | Resolved/closed feedback entries. | Same. |
| `reference/installed-packages.md` | What packages are installed in this framework, when, with which intent files applied. | Same. |

### Reference subdirectories

| Path | Purpose | Attribution |
|------|---------|-------------|
| `reference/sessions/` | Maintenance session logs (one per substantive session). 41 logs as of 2026-05-07. | `[framework default]` per `install/structure-intent.md`. |
| `reference/designs/` | Design documents that don't fit the rationale-entry shape — long-form design exploration before convergence. | First added 2026-02-15 (commit a60fafa, "feedback channel design"). Used since for design docs that are too long for inline in design-rationale.md (cowork-plugin-export, export-skill, feedback-channel). `[judgment]`. |
| `reference/feedback/` | Feedback letter drafts and archives — outbound and inbound text that informs the framework but isn't a triaged feedback log entry yet. | First added 2026-02-15 (commit a60fafa). Used by penny post pattern (drafts before sending, archived copies). `[judgment]`. |
| `reference/specs/` | Specifications for traditional-code helpers in `lib/`. | First added 2026-04-16 (commit 8690dd3, "export session outcomes: archival, spec draft"). Holds `export-service.md`. `[judgment]`. |
| `reference/standards/` | Quality standards documents (writing, future Python implementation, etc.). | Added 2026-04-17 (commit cd27c25) per the 2026-04-17 NLA writing standards work. Documented in design rationale; one of the named conventions for accumulating standards docs. |
| `reference/experiments/` | Experiment reports for prose-as-code controlled experiments. | Added 2026-05-06 (commit 9535218) via the skill-invocation discipline experiments. Modeled on facebook-moderation's `reference/experiments/` pattern. `[judgment, modeling-on-existing-pattern]`. |
| `reference/plans/` | Warm-context plans for execution in a later session. Pattern: when a plan needs to be drafted with full context but executed cold (e.g., publication arcs), it lands here for the future session to consume. | Added 2026-05-06 (commit cd857e2) via skill-invocation discipline publication plan. Modeled on `reference/standards/` and `reference/experiments/`. `[judgment]`. |

**Judgment note (subdirectory accretion):** Five of the seven
subdirectories above (`designs/`, `feedback/`, `specs/`, `experiments/`,
`plans/`) accreted before the structural change discipline existed.
This file is the first place all seven are documented together. The
`install/structure-intent.md` file lists only `sessions/` — it should be
updated to mention these accreted directories when domain-project
propagation happens (deferred to publication plan).

---

## `lib/`

Traditional code helpers. Currently sparse — the framework is mostly
prose.

| Path | Purpose | Attribution |
|------|---------|-------------|
| `lib/export.py` | Mechanical work for `/export` (path rewrites, frontmatter surgery, archive bundling). Stdlib-only, no pip. | `[design rationale: "Mechanism: hybrid AI + Python script"]` (added 2026-04-16 with the view-source plugin model). |
| `lib/.gitkeep` | Directory placeholder. | `[framework default]` per `install/structure-intent.md`. |

**Judgment note (lib/ standards gap):** `lib/export.py` was hand-rolled
without implementation standards. The friction log carries a pending
entry "No implementation standards for Python scripts in the framework"
flagging this. When Python standards land, `lib/` may need a
`reference/standards/python.md` to govern future additions.

---

## `packages/`

Submodule dependencies. Flat (no `--recursive`); each NLA pulls its own
direct dependencies.

| Path | Purpose | Attribution |
|------|---------|-------------|
| `packages/nla-penny-post/` | Feedback conventions and inter-NLA letters. First NLA extension package. | `[design rationale: "The new model"]` (packages/submodules migration 2026-04-15) plus per-package design rationale on penny post. |
| `packages/nla-process-helpers/` | Facilitation techniques (brainstorming, steelmanning, devil's advocate, unpack). | Same; created 2026-02-22. |

**Judgment note (no recursive submodules):** Each NLA pulls its own
dependencies directly. The framework does not transitively pull
penny-post's or process-helpers's dependencies. Per the migration design
rationale.

---

## `.claude/skills/`

Skill wrappers Claude Code discovers. 21 wrappers at present. Each is a
short SKILL.md with frontmatter (name, description) and a delegation
pointer (`Read and follow core/skills/[name].md` for thin wrappers, or
the full skill body for skills not in `core/`).

Categories:

- **Universal framework skills** (delegate to `core/skills/`): maintain,
  install, update, check-updates, friction-log, debrief, close,
  preferences, validate, think, session-checkpoint, guide, export.
- **Framework-only skills** (full skills, no core/ delegate):
  create-app, install-app, check-feedback, write-letter (the last two
  via penny-post). These exist in framework only because they don't apply
  in domain-project contexts.
- **Process helper skills** (delegate to `packages/nla-process-helpers/`):
  brainstorm-cluster, steelman, devils-advocate, unpack.

**Judgment note (no `/startup` in framework):** Domain projects have
`/startup` to load context at session start. The framework doesn't —
its working directory IS the framework, so paths like
`packages/nla-framework/core/...` would be self-referential. The
framework's CLAUDE.md handles startup directly. (Per design rationale
"Framework Self-Maintenance.")

**Judgment note (skill invocation discipline):** All 21 wrappers carry
constraint-bearing descriptions per the convention adopted 2026-05-06.
See `reference/experiments/skill-invocation-discipline/experiment-report.md`
and `CLAUDE.md` "Skill invocation discipline" subsection.

---

## Decision Sources (scan view)

| Decision | Attribution |
|----------|-------------|
| `core/` for executable framework docs | Design rationale: "core/ for Framework Executable Docs" |
| `app/` reserved for domain content (not present in framework) | Same |
| `reference/` for maintenance records | Design rationale: "reference/ Stays As-Is" |
| Thin wrapper skills in `.claude/skills/` | Design rationale: "Thin Wrapper Skills" |
| Framework's own skills are full (not wrappers) | Design rationale: "Framework Self-Maintenance" |
| Intent files as source of truth for `/create-app` | Design rationale: "Intent Files as Single Source of Truth" |
| Dual-mode framework CLAUDE.md | Design rationale: "Dual-Mode Framework CLAUDE.md" |
| Submodules at `packages/` (not sibling dirs) | Design rationale: "The new model" (2026-04-15) |
| `lib/export.py` as hybrid AI + Python script | Design rationale: "Mechanism: hybrid AI + Python script" |
| `reference/standards/` for quality standards | 2026-04-17 NLA writing standards session |
| `reference/experiments/` for experiment reports | 2026-05-06 skill-invocation discipline session |
| `reference/plans/` for warm-context plans | 2026-05-06 skill-invocation discipline session |
| `reference/feedback/`, `reference/designs/` | `[judgment]` — accreted, documented here for the first time |
| `reference/specs/` | `[judgment]` — accreted with `lib/export.py` work 2026-04-16 |
| Skill-invocation constraint-bearing descriptions | 2026-05-06 experiment report |
| `core/structure.md` and the structural change discipline | Design rationale: "Structure Decisions Protocol" 2026-05-07 |

---

## Maintenance

When a structural change is needed (new directory, new top-level file,
reorganization), follow the protocol in `CLAUDE.md` ("Structural change
discipline"): propose to the human, get approval, update *this file* in
the same operation, then act. Recording is part of the change, not
separate hygiene.

When a structural change has happened *outside* this protocol (drift,
external commits, accreted directories), update this file when the
drift is noticed. A described-but-missing entry or an existing-but-not-
described directory is a signal worth flagging.

The scan check: every entry in this file should exist on the
filesystem; every consequential directory or top-level file on the
filesystem should be in this file. Periodic verification matches the
discipline that gives the file value.
