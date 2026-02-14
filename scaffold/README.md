# My NLA Project

A Natural Language Application built on the [NLA Framework](../nla-framework/).

---

## Prerequisites

**NLA Framework** must be available at `../nla-framework/` (sibling directory to this project).

```bash
# If you haven't cloned it yet:
git clone <framework-repo-url> ../nla-framework
```

**Claude Code** must be installed. This project runs inside Claude Code sessions.

---

## Quick Start

1. Start Claude Code in this directory
2. Run `/startup` to load foundational context
3. Run `/format-article` and provide raw content
4. Review the formatted output
5. Make corrections, then use `/friction-log` to capture learnings

---

## What's Inside

```
├── CLAUDE.md                        # Runtime identity and configuration
├── app/                             # The application (LLM reads and executes)
│   ├── overview.md                  # What this NLA does, how pieces connect
│   ├── shared/
│   │   ├── voice-and-values.md      # Tone and editorial identity
│   │   ├── common-patterns.md       # Shared transformations
│   │   └── output-spec.md           # Output format
│   ├── config-spec.md               # What users can configure (developer-defined)
│   └── format-article.md            # Article formatting task (sample)
├── config.md                        # User preferences (quarterback config)
├── config/                          # Context-specific sub-configs
│   └── maintenance.md               # Preferences for maintenance mode
├── reference/                       # Maintenance records (not loaded at runtime)
│   ├── design-rationale.md          # Why the system is built this way
│   ├── friction-log.md              # Learning journal (active entries)
│   ├── friction-log-archive.md      # Resolved entries
│   ├── system-status.md             # Current state snapshot
│   └── sessions/                    # Maintenance session archives
├── .claude/skills/                  # Skill entry points
│   ├── startup/                     # Framework wrapper
│   ├── maintain/                    # Framework wrapper
│   ├── friction-log/                # Framework wrapper
│   ├── plan/                        # Framework wrapper
│   ├── preferences/                 # Framework wrapper
│   ├── validate/                    # Framework wrapper
│   └── format-article/              # Domain skill (sample)
└── lib/                             # Traditional code helpers
```

---

## What to Customize

| File | Purpose |
|------|---------|
| `app/shared/voice-and-values.md` | Replace with your brand's tone and editorial identity |
| `app/shared/common-patterns.md` | Replace with transformations specific to your content |
| `app/shared/output-spec.md` | Replace with your output format (Markdown, HTML, JSON, etc.) |
| `app/format-article.md` | Replace with your domain task |
| `.claude/skills/format-article/` | Replace with your domain skill |
| `CLAUDE.md` | Update the skills table and environment section for your project |
| `app/overview.md` | Update to describe what your NLA does |

The `reference/` directory works as-is — it uses the same friction log and maintenance patterns regardless of domain.

---

## Configuration

Users can personalize how the NLA behaves by running `/preferences`. This creates `config.md` and optionally `config/` sub-configs with user preferences — tone adjustments, formatting style, workflow modifications.

Config files are separate from the application. In a real project, they're gitignored so that `git pull` updates the app without touching user preferences. `app/config-spec.md` defines what's configurable.

---

## The Improvement Loop

```
Observe something → /friction-log captures it → Friction log stores it → /maintain implements changes
```

1. Use your NLA normally
2. Notice something that could be better (formatting, tone, missed pattern)
3. Run `/friction-log` to record the observation
4. When ready, run `/maintain` to process accumulated observations into doc changes
5. The docs improve, and the NLA behavior improves with them

---

## Adding Tasks

To add a new task beyond the sample formatter:

1. Create `app/my-task.md` following the structure of `format-article.md`
2. Create `.claude/skills/my-task/SKILL.md` as a skill entry point
3. Add the skill to the tables in `CLAUDE.md` and `app/overview.md`
4. Update `reference/system-status.md`

The new task automatically inherits shared context (voice, patterns, output spec).

---

## Framework Updates

```bash
cd ../nla-framework
git pull
```

Framework updates (skill logic, NLA foundations) take effect immediately through the thin wrapper pattern. Your domain content is never touched.

---

*For more about the NLA Framework, see the [framework README](../nla-framework/README.md).*
