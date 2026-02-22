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

Start Claude Code in the framework directory and run `/create-app`. It asks about your domain, voice, and tasks, then generates a complete project tailored to what you're building.

```bash
cd nla-framework
claude

# Then:
/create-app
```

The conversation takes a few minutes. You'll have a working project at the end.

### 3. Initialize and use

```bash
cd ../my-project
git init && git add -A && git commit -m "Initial NLA project"
claude

# Then:
/startup          # Load foundational context
/my-task          # Run your domain task
```

### See a working example first

If you want to explore a complete NLA before building your own, run `/install-app`. It presents a catalog of example NLA projects you can clone and try immediately.

```bash
cd nla-framework
claude

# Then:
/install-app
```

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
nla-framework/
├── core/
│   ├── nla-foundations.md     # What NLAs are, key principles, the hybrid model
│   └── skills/               # Skill logic (delegated to by domain project wrappers)
├── install/                   # Intent files — what NLAs need (source of truth for /create-app)
│   ├── CLAUDE-intent.md       # Runtime identity intent
│   ├── skills-intent.md       # Skill wrapper intent with reference implementations
│   ├── structure-intent.md    # Directory structure and reference file intent
│   ├── example-catalog.md     # Example NLA projects catalog
│   ├── install.md             # Install manifest
│   ├── update-notes.md        # Changelog for domain projects (read by /update)
│   └── README.md              # How intent files work
├── reference/                 # Framework maintenance records
│   ├── design-rationale.md    # Why the framework is built this way
│   ├── friction-log.md        # Internal observations and learnings
│   ├── friction-log-archive.md # Resolved friction log entries
│   ├── feedback-log.md        # Accepted external feedback
│   ├── feedback-log-archive.md # Resolved feedback log entries
│   ├── installed-packages.md  # Packages installed in this project
│   ├── designs/               # Design documents for future work
│   ├── feedback/              # Feedback intake drafts
│   └── sessions/              # Maintenance session logs
├── config-spec.md             # What's configurable (developer-defined)
├── CONTRIBUTING.md            # Contribution guidelines
└── .claude/skills/            # Framework-level skills
    ├── create-app/            # Conversational project creation
    ├── install-app/           # Browse and install example NLAs
    ├── maintain/              # Framework maintenance mode
    ├── validate/              # System validation (structural, architecture, scenarios, debug)
    ├── friction-log/          # Log observations to the friction log
    ├── preferences/           # Create or edit framework preferences
    ├── install/               # Install NLA packages
    ├── update/                # Update installed packages
    ├── check-feedback/        # Discover and triage external feedback
    ├── write-letter/          # Draft and submit feedback to other projects
    ├── export/                # Export NLA projects as plugins
    ├── think/                 # Collaborative design exploration
    └── debrief/               # Reflect on completed work
```

`core/` contains universal NLA building blocks — they work with any domain content. `install/` contains intent files that describe what a well-formed NLA should have — the single source of truth that `/create-app` reads when generating projects.

---

## What's in a Domain Project

```
my-project/
├── CLAUDE.md                    # Runtime identity and configuration
├── app/                         # The application (LLM reads and executes)
│   ├── overview.md              # What this NLA does
│   ├── shared/                  # Shared context (values, voice, patterns, output spec)
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
| Framework README, docs | Intent file improvements (affect new projects only) |

For intent-file-level changes (new skills, changed structure expectations), run `/update` in your project. It compares the framework's current intent files against what was installed and proposes changes. The framework's `install/update-notes.md` provides context about what changed and why.

---

## Ejecting a Skill

If you need to customize a framework skill, replace the thin wrapper with a full skill file:

1. Read the framework logic file (e.g., `core/skills/maintain.md`)
2. Copy its content into your project's `.claude/skills/maintain/SKILL.md`
3. Add YAML frontmatter at the top
4. Customize as needed

Unlike traditional frameworks, ejecting doesn't mean forking. Because `/update` communicates intent — not diffs — the LLM can still propose how framework improvements apply to your customized implementation. You get full control AND intent-level updates. See "The Wrapper Spectrum" in [design-rationale.md](reference/design-rationale.md) for the full picture.

---

## Distributing as a Plugin

Once your NLA is working, you can export it as a plugin for Claude Code or Cowork:

```bash
cd ../my-project
claude

# Then:
/export
```

`/export` converts the NLA project into a self-contained plugin directory. It resolves all framework dependencies (flattening thin wrappers into full skills), bundles shared context, and generates a foundation skill that replaces CLAUDE.md. The result is a plugin anyone can install — no framework clone, no sibling directory, no git.

Think of it as compiling: the NLA project is your source code, the plugin is the artifact you ship. To improve the plugin, improve the NLA and re-export.

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

- **The Cardinal Rule** — The human decides. Humans bear consequences, so humans hold authority.
- **Judgment Over Rules** — Explain *why*, not just *what*. Purpose enables edge-case handling.
- **The Hybrid Model** — Humans provide flexibility, the LLM adds structure, traditional code handles determinism.
- **Iterate Through Documentation** — The system improves by improving documentation, formalized through the friction log and maintenance cycle.

---

## Extension Examples

The framework provides the universal improvement pipeline (`/friction-log` + `/maintain`). Domain projects can extend it. For example, a content-transformation NLA might add a `/learning-feedback` skill for structured correction analysis — comparing human edits against NLA output to capture rich "before/after" learnings. The framework's pipeline handles the general case; extensions handle domain-specific patterns.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on proposing changes to the framework.
