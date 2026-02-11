# NLA Framework

A framework for building Natural Language Applications — software where documentation is source code and an LLM is the runtime.

---

## What is an NLA?

A Natural Language Application is software where the "code" is written in natural language (Markdown) and "executed" by an LLM. When you want to change behavior, you edit the docs. When you want to add features, you write more docs. The LLM reads the docs and does what they say.

NLAs excel at tasks that require judgment — formatting decisions, pattern recognition, tone, style. Things that are easier to explain than to code. Traditional code handles the deterministic parts (API calls, file I/O, validation). The NLA handles the intelligence.

For the full conceptual foundation, see [core/nla-foundations.md](core/nla-foundations.md).

---

## Getting Started

### 1. Clone the framework

```bash
git clone <framework-repo-url> nla-framework
```

### 2. Create your project

```bash
cp -r nla-framework/scaffold my-project
cd my-project
git init
```

The scaffold gives you a working project with a sample article formatter. You can test it immediately.

### 3. Start using it

```bash
# In your project directory, start Claude Code
claude

# Then:
/startup        # Load foundational context
/format-article # Format some content
```

### 4. Customize

Replace the sample content with your domain:

| File | What to customize |
|------|-------------------|
| `app/shared/voice-and-values.md` | Your brand's tone and editorial identity |
| `app/shared/common-patterns.md` | Transformations specific to your content |
| `app/shared/output-spec.md` | Your output format (Markdown, HTML, JSON, etc.) |
| `app/format-article.md` | Replace with your domain task, or rename and adapt |
| `.claude/skills/format-article/` | Replace with your domain skill |
| `CLAUDE.md` | Update the skills table and environment section |

---

## How It Works

### The thin wrapper pattern

Your project has skill files in `.claude/skills/` that Claude Code discovers. Framework skills are thin wrappers — they delegate to logic files in the framework:

**Your project** (`.claude/skills/startup/SKILL.md`):
```markdown
---
name: startup
description: Initialize the NLA runtime.
---
Read and follow `../nla-framework/core/skills/startup.md`.
```

**Framework** (`core/skills/startup.md`):
Contains the full skill logic. Updated when you `git pull` the framework.

**Domain skills** (like `/format-article`) are full skill files in your project — they don't delegate to the framework because they contain your domain-specific logic.

### Path resolution

The LLM always operates from your project's working directory:
- **Your files:** `app/overview.md`, `reference/friction-log.md`
- **Framework files:** `../nla-framework/core/nla-foundations.md`

The framework must be a sibling directory to your project. If you put it elsewhere, update the skill wrappers and the note in CLAUDE.md.

---

## What's in the Framework

```
core/
├── nla-foundations.md     # What NLAs are, key principles, the hybrid model
└── skills/
    ├── startup.md         # Load foundational context at session start
    ├── maintain.md        # System maintenance mode
    ├── friction-log.md    # Capture observations to the learning journal
    └── plan.md            # Planning mode for new tasks or major changes
```

These are universal NLA building blocks. They work with any domain content.

---

## What's in a Domain Project

```
my-project/
├── CLAUDE.md                    # Runtime identity and configuration
├── app/                         # The application (LLM reads and executes)
│   ├── overview.md              # What this NLA does
│   ├── shared/                  # Shared context (voice, patterns, output spec)
│   └── [task docs]              # Your domain tasks
├── reference/                   # Maintenance records (not loaded at runtime)
│   ├── design-rationale.md
│   ├── friction-log.md
│   └── sessions/
├── .claude/skills/              # Skill entry points
│   ├── startup/SKILL.md         # Wrapper → framework
│   ├── maintain/SKILL.md        # Wrapper → framework
│   └── [domain skills]          # Your full skill files
└── lib/                         # Traditional code helpers
```

---

## Upgrading

```bash
cd ../nla-framework
git pull
```

That's it. The thin wrappers in your project point to framework files, so updated logic takes effect immediately.

| Updated by `git pull` | Requires manual sync (rare) |
|---|---|
| nla-foundations.md | Grounding principles in your CLAUDE.md |
| All skill logic | Friction log format changes |
| Framework README, docs | Scaffold improvements (new projects only) |

---

## Ejecting a Skill

If you need to customize a framework skill, replace the thin wrapper with a full skill file:

1. Read the framework logic file (e.g., `core/skills/maintain.md`)
2. Copy its content into your project's `.claude/skills/maintain/SKILL.md`
3. Add YAML frontmatter at the top
4. Customize as needed

The ejected skill won't receive framework updates, but you have full control. You can always re-wrap it later.

---

## Adding Domain Skills

Create domain skills alongside framework wrappers:

1. Create `app/my-task.md` with the task instructions
2. Create `.claude/skills/my-task/SKILL.md` with the skill entry point
3. Add to the skills table in `CLAUDE.md` and `app/overview.md`

Domain skills reference `app/` files directly — they don't go through the framework.

---

## Key Concepts

These are explained in depth in [core/nla-foundations.md](core/nla-foundations.md):

- **The Cardinal Rule** — The human must always be able to compare changes against the original and easily revert.
- **Judgment Over Rules** — Explain *why*, not just *what*. Purpose enables edge-case handling.
- **The Structure Gradient** — Humans provide flexibility, the LLM adds structure, traditional code handles determinism.
- **Iterate Through Documentation** — The system improves by improving documentation, formalized through the friction log and maintenance cycle.

---

## Extension Examples

The framework provides the universal improvement pipeline (`/friction-log` + `/maintain`). Domain projects can extend it. For example, a content-transformation NLA might add a `/learning-feedback` skill for structured correction analysis — comparing human edits against NLA output to capture rich "before/after" learnings. The framework's pipeline handles the general case; extensions handle domain-specific patterns.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on proposing changes to the framework.
