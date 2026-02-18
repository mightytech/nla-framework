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
│   │   └── output-spec.md        # Output format specification
│   └── [task-name].md            # One doc per task (the actual application logic)
├── reference/                    # Maintenance records (non-executing channel)
│   ├── design-rationale.md       # Why the system is built this way
│   ├── friction-log.md           # Internal observations, pending and active
│   ├── friction-log-archive.md   # Resolved friction log entries
│   ├── feedback-log.md           # Accepted external feedback, pending implementation
│   ├── feedback-log-archive.md   # Resolved feedback log entries
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

*This describes intent, not literal text. The installing AI should create missing
structure elements in whatever way fits the NLA's existing organization.*
