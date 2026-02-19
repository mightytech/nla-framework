# Structure Integration Intent

What directory structure and reference files the NLA should have after installing
the NLA Framework.

---

## Directory Layout

A framework-based NLA should have this structure:

```
my-nla/
├── app/                          # The application (operative channel)
│   ├── overview.md               # How the pieces connect
│   ├── config-spec.md            # What's configurable (developer-defined)
│   ├── shared/                   # Context shared across all tasks
│   │   ├── voice-and-values.md   # Tone, personality, editorial standards
│   │   ├── common-patterns.md    # Recurring patterns the LLM should recognize
│   │   └── output-spec.md        # Output format specification (optional — see below)
│   └── [task-name].md            # One doc per task (the actual application logic)
├── reference/                    # Maintenance records (non-executing channel)
│   ├── design-rationale.md       # Why the system is built this way
│   ├── friction-log.md           # Internal observations, pending and active
│   ├── friction-log-archive.md   # Resolved friction log entries
│   ├── feedback-log.md           # Accepted external feedback, pending implementation
│   ├── feedback-log-archive.md   # Resolved feedback log entries
│   ├── installed-packages.md     # Record of installed NLA packages
│   ├── system-status.md          # Current state of the NLA
│   └── sessions/                 # Maintenance session logs
├── config.md                     # User preferences (gitignored)
├── config/                       # Sub-config files (gitignored)
├── lib/                          # Traditional code helpers
├── .claude/skills/               # Skill wrappers (see skills-intent.md)
├── CLAUDE.md                     # Runtime identity (see CLAUDE-intent.md)
├── README.md                     # Developer-facing documentation
└── .gitignore                    # Excludes config.md and config/
```

## Two Channels

The structure embodies a separation between two channels:

- **`app/`** — The operative channel. The LLM reads these docs and executes them.
  This IS the application.
- **`reference/`** — The maintenance channel. Not read during normal operation.
  Read during `/maintain` sessions. Contains history, rationale, and learning logs.

## Reference Files

### Friction Log (`reference/friction-log.md`)

Running log of things noticed during NLA operation — problems, surprises, things
that worked well. Internal observations from the NLA's own sessions.

**Fed by:** `/friction-log` skill, direct observation during work.
**Consumed by:** `/maintain` sessions.
**Archive:** Resolved entries move to `friction-log-archive.md`.

### Feedback Log (`reference/feedback-log.md`)

Accepted items from external feedback — things others noticed that the maintainer
agreed with after triage. The sibling of the friction log.

**Fed by:** `/check-feedback` or any external feedback mechanism that deposits
accepted items after triage.
**Consumed by:** `/maintain` sessions.
**Archive:** Resolved entries move to `feedback-log-archive.md`.

Together, these two logs form the maintenance pipeline:
- **Friction log** = internal observations
- **Feedback log** = external feedback (post-triage)
- **`/maintain`** processes both into documentation changes

### Design Rationale (`reference/design-rationale.md`)

Records *why* the NLA is built the way it is. Captures decisions, alternatives
considered, and trade-offs. Prevents well-intentioned changes from breaking things
that work.

### Session Logs (`reference/sessions/`)

Records of maintenance sessions — what was intended, what changed, what decisions
were made, and where things stand. Provides session continuity and intent history.

### System Status (`reference/system-status.md`)

Current state of the NLA — what tasks exist, what skills are available, what's
working, what's in progress.

## Configuration Files

- **`config.md`** — Always-loaded quarterback. Routes to sub-configs by context.
- **`config/`** — Sub-config files loaded conditionally.
- **`app/config-spec.md`** — Developer-defined specification of what's configurable.
- Both `config.md` and `config/` are gitignored — they belong to the user.

## What NOT to Change

When updating an existing NLA's structure:

- Don't remove or overwrite existing `app/` content
- Don't alter existing reference files' content (add new files, don't rewrite old ones)
- Don't touch `config.md` or `config/` (user-owned)
- Structure additions are additive — new files alongside existing ones

---

## Reference File Structures

These describe the expected sections and shape of each framework-provided file. The AI
generating these files uses these as structural guidance — matching the section organization
and purpose, not copying literal text.

### `reference/design-rationale.md`

- **Title / Audience / Purpose** — Who this document is for (maintainers) and why it
  exists (prevent well-intentioned changes from breaking things that work).
- **"Why an NLA?"** — Why this domain problem is better solved with an NLA than
  traditional code.
- **"Why This Structure"** — Rationale for the two-channel architecture, naming choices,
  framework-domain separation.
- **Key Design Decisions** — Individual decisions with what was decided, why, alternatives
  considered, and what it affects. One subsection per decision.
- **"Adding Decisions"** — Instructions for future maintainers on how to document new
  decisions.

### `reference/friction-log.md`

- **"How to Use This Log"** — When to add entries, entry types (output, process,
  documentation), severity includes positive.
- **Entry Format** — Template showing all fields: Date/title heading, Type, Severity,
  Task, Status, Observation, Before/After, Confirmed reason, Generalizable,
  Affected documentation, Proposed fix, Notes. Note that not all fields are required.
- **Resolution process** — How `/maintain` updates the Status field with date and
  description when resolving entries.
- **Entries** — Section header for chronological entries (newest first). May include
  one example entry demonstrating the format.
- **"Patterns to Watch"** — Recurring themes the NLA is monitoring, seeded with
  domain-relevant patterns.

### `reference/feedback-log.md`

- **Purpose** — Accepted items from external feedback, waiting for implementation.
- **Relationship to friction log** — Friction log = things you noticed; feedback log =
  things others noticed that you agreed with. Both feed into `/maintain`.
- **"How to Use This Log"** — When items are added (after triage), when resolved (during
  `/maintain`), archive destination.
- **Entry Format** — Template: Date/title heading, Source, Verdict, Status, What to do,
  Why it was accepted, Resolved line. Not all fields required.
- **Entries** — Section header for chronological entries (newest first).

### `reference/system-status.md`

- **Last Updated** — Date of last status update.
- **Tasks table** — Table of domain tasks with columns: Task, Status, Notes.
- **Skills table** — Table of all skills with columns: Skill, Status, Notes. Includes
  both framework wrappers and domain skills.
- **Recent Changes** — Brief log of what changed recently.

### `reference/installed-packages.md`

- **Purpose** — What this file tracks and how `/install` and `/update` maintain it.
- **Per-package sections** — Each installed package gets a section with: package name,
  install date, state at install (commit hash or date), what was done, and update records
  appended over time.

### `reference/friction-log-archive.md`

- **Title** — "Friction Log Archive"
- **How entries arrive** — Moved from `friction-log.md` during `/maintain` sessions.
  `/friction-log` skill searches here before creating new entries.
- **Entries** — Section header for archived entries in reverse chronological order.

### `reference/feedback-log-archive.md`

- **Title** — "Feedback Log Archive"
- **How entries arrive** — Moved from `feedback-log.md` during `/maintain` sessions.
- **Entries** — Section header for archived entries in reverse chronological order.

### `README.md`

- **Title** — Project name, one-line description with link to framework.
- **Prerequisites** — Framework at `../nla-framework/`, Claude Code installed.
- **Quick Start** — Numbered steps: start Claude Code, `/startup`, run domain task,
  review, `/friction-log` for learnings.
- **Directory tree** — Annotated tree showing actual project structure.
- **Customization table** — Table of files to customize with what to change in each.
- **Configuration** — Brief explanation of `/preferences` and the config system.
- **Improvement loop** — The observe → `/friction-log` → `/maintain` cycle.
- **Adding tasks** — How to add new domain tasks (create task doc, skill, update tables).
- **Framework updates** — `git pull` the framework; thin wrappers pick up changes.

### `config.md`

- **"Always Active" section** — Simple directives that always apply (framework path,
  universal preferences).
- **"Contextual" section** — Routing rules that load sub-configs based on context
  (mode, task, conditions).

### `app/config-spec.md`

- **"What's Configurable" section** — Subsections for each configurable area, each with
  description and defaults. Areas depend on the domain but typically include: voice/tone
  adjustments, formatting preferences, framework path, tracing levels.
- **"Constraints" section** — What's NOT configurable (core values, cardinal rule, etc.).
- **"Guidance for the Config Conversation"** — What to start with when users aren't sure,
  advice for first-time users.

### Mechanical File Templates

These files have fixed content that doesn't vary by domain:

**`.gitignore`:**
```
config.md
config/
```

**`.gitkeep`** (for `lib/`, `reference/sessions/`, `config/`):
Empty file — directory placeholder only.

---

*This describes intent, not literal text. The installing AI should create missing
structure elements in whatever way fits the NLA's existing organization.*
