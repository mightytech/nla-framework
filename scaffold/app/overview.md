# System Overview

This document describes what this NLA does and how its pieces fit together. For what NLAs are and the principles behind them, see [nla-foundations.md](../nla-framework/core/nla-foundations.md).

---

## What This NLA Does

This system formats raw, unstructured content into polished articles. It takes drafts — often rough, informal, written quickly — and transforms them into well-structured, consistent, publication-ready pieces.

| Task | Purpose | Trigger |
|------|---------|---------|
| **Format Article** | Format raw content into a polished article | User provides content |

### Format Article

The primary NLA task. Takes raw, unformatted content and applies editorial standards:
- Adds structure (headers at topic shifts, logical section breaks)
- Converts URLs to descriptive links
- Identifies and formats special sections (resources, calls to action)
- Adds emphasis for powerful quotes or key points
- Cleans up formatting artifacts
- Adds TK notes for uncertain decisions

**Source:** `format-article.md`

### How It Connects

```
                    ┌─────────────────┐
                    │  Shared Context │
                    │  - Voice/Values │
                    │  - Patterns     │
                    │  - Output Spec  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────┐
                    │   Format    │
                    │   Article   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Polished   │
                    │  Content    │
                    └─────────────┘
```

The task reads shared context (voice, patterns, output spec) and applies it to transform content. As you add more tasks, they all share the same foundation.

### Invocation via Skills

Each task has an explicit entry point — a Claude Code skill:

| Skill | Purpose |
|-------|---------|
| `/startup` | Load foundational context at session start |
| `/format-article` | Format raw content into a polished article |
| `/preferences` | Create or edit user configuration |
| `/friction-log` | Log observations to the friction log from any context |
| `/maintain` | Edit the NLA system itself |
| `/validate` | Check system consistency, trace scenarios, debug behavior |
| `/plan` | Planning mode for new tasks or major changes |

Skills live in `.claude/skills/` and load their context on demand — `CLAUDE.md` provides the runtime identity, and each skill pulls in the specific docs it needs. `/startup` can also be re-run mid-session to reload foundational context after a long conversation.

### The Improvement Pipeline

The system improves through the friction log:

```
Observation from any context → /friction-log captures it → Friction Log → /maintain implements
```

`/friction-log` captures observations from any context — during content formatting, maintenance, or casual conversation. Entries accumulate in the friction log, where patterns emerge over time. `/maintain` processes them into doc changes. Resolved entries are archived to `friction-log-archive.md`.

This separation exists because capturing observations and editing system docs are different tasks with different guardrails. The friction log is the handoff contract between them.

---

## For Humans

**To change AI behavior:**
- Identify which document governs that behavior
- Edit the document
- The change takes effect immediately (next run)

**To debug unexpected output:**
- Check which documents the AI read
- Look for ambiguity or missing guidance
- Add clarification or examples

**To add a new task:**
1. Create a new file in `app/` (e.g., `app/my-new-task.md`)
2. Follow the structure of existing task docs
3. Create a skill in `.claude/skills/my-new-task/SKILL.md`
4. Add it to the skills table in this overview and in CLAUDE.md
5. The new task inherits all shared context

---

## Document Hierarchy

```
app/
├── overview.md                      ← This file
│
├── shared/
│   ├── voice-and-values.md          ← Tone and editorial identity
│   ├── common-patterns.md           ← Shared transformations
│   └── output-spec.md               ← Output format
│
├── config-spec.md                   ← What users can configure (developer-defined)
│
└── format-article.md                ← Article formatting task

config.md                            ← User preferences (gitignored in real projects)
config/                              ← Context-specific sub-configs

../nla-framework/core/
├── nla-foundations.md               ← What NLAs are (framework)
└── skills/                          ← Skill logic (framework)

reference/
├── design-rationale.md              ← Why the system is built this way
├── friction-log.md                  ← Learning journal (active entries)
├── friction-log-archive.md          ← Resolved entries (searchable history)
├── system-status.md                 ← Current state snapshot
└── sessions/                        ← Maintenance session archives
```

---

## Document Index

### Shared Context
- [Voice and Values](shared/voice-and-values.md) — Tone, principles, editorial identity
- [Common Patterns](shared/common-patterns.md) — Transformations all tasks share
- [Output Spec](shared/output-spec.md) — Output format details
- [Config Spec](config-spec.md) — What users can configure and how

### Tasks
- [Format Article](format-article.md) — Format raw content into polished articles

### Reference
- [Design Rationale](../reference/design-rationale.md) — Why the system is built the way it is
- [Friction Log](../reference/friction-log.md) — Running log of issues and improvements
- [System Status](../reference/system-status.md) — Current state snapshot

---

## Getting Started

### First-Time Setup

1. Read [nla-foundations.md](../nla-framework/core/nla-foundations.md) — understand NLA concepts
2. Read this overview
3. Read shared context documents
4. Read the task document for your work

### Running the Formatter

1. Start Claude Code and run `/startup`
2. Run `/format-article`
3. Provide raw content
4. Review the formatted output
5. Make any corrections

---

*This is a living document. As the NLA system evolves, update this overview to reflect the current state.*
