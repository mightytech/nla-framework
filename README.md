# NLA Framework

A framework for building Natural Language Applications — software where prose
is the application and an LLM is the runtime.

The source code is Markdown. The runtime is an AI. When behavior needs to
change, the fix is better writing, not better code. This framework provides
the shared foundations, skills, and patterns that make that work.

---

## What Is an NLA?

A Natural Language Application is software where the source code is written
in prose and executed by an LLM. The documents aren't documentation *about*
the application — they *are* the application. When behavior needs to change,
you edit the prose. When you want to add a feature, you write one. The LLM
reads it and does what it says.

This isn't prompt engineering. These are systems with persistence, learning
loops, and modularity — where boundaries between modules are prose rather
than function calls. A spam filter becomes "ignore anything that isn't genuine
feedback." An update system becomes a full package manager — with rollback
branches, merge strategies, and dependency resolution — expressed entirely
in prose.

NLAs excel where judgment is the core requirement — editorial decisions,
pattern recognition, tone, classification, synthesis. Traditional code
handles the deterministic parts (API calls, file I/O, validation). The NLA
handles the intelligence. Neither replaces the other.

If that sounds unusual, two paths for the curious:

- **Read about it:**
  [The Documentation Is the Application](https://github.com/mightytech/nla-office-hours/blob/main/content/the-documentation-is-the-application.md)
  — a probe report exploring what software becomes when language is the runtime
- **Talk to one:**
  [NLA Office Hours](https://github.com/mightytech/nla-office-hours) — an NLA
  you can talk to about NLAs

For the full conceptual foundation, see
[core/nla-foundations.md](core/nla-foundations.md).

---

## Built With NLAs

- [Duet](https://github.com/mightytech/duet) — collaborative music
  composition with SuperCollider
- [Copydesk](https://github.com/mightytech/copydesk) — CMS content
  formatting with pluggable voice and platform packages
- [nla-claude-code](https://github.com/mightytech/nla-claude-code) —
  developer tooling that deposits configuration into codebases
- [Penny Post](https://github.com/mightytech/nla-penny-post) — feedback
  conventions and inter-agent communication
- [Email Rewriter](https://github.com/mightytech/email-rewriter) —
  tone-aware email rewriting
- [Process Helpers](https://github.com/mightytech/nla-process-helpers) —
  facilitation techniques (brainstorming, steelmanning, adversarial testing)
- [NLA Writer](https://github.com/mightytech/nla-writer) — writing partner
  (helped produce the probe report)

**Explorations** — white papers on domains not yet built:
[Policy Stakeholder Simulation](https://github.com/mightytech/nla-whitepapers/blob/main/nla-policy-stakeholder-simulation.md) ·
[Tax Filing](https://github.com/mightytech/nla-whitepapers/blob/main/nla-tax-filing-1040ez.md) ·
[Calendar Negotiation](https://github.com/mightytech/nla-whitepapers/blob/main/calendar-negotiation-agent.md) ·
[Medical Intake](https://github.com/mightytech/nla-whitepapers/blob/main/LLM_as_Platform_Medical_Intake.docx)

---

## Getting Started

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)

### 1. Clone the framework

```bash
git clone https://github.com/mightytech/nla-framework.git
```

### 2. Create your project

Start Claude Code in the framework directory and run `/create-app`. A short
conversation about your domain, voice, and tasks — then a working project.

```bash
cd nla-framework
claude
# Then: /create-app
```

### 3. Use it

```bash
cd ../my-project
git init && git add -A && git commit -m "Initial NLA project"
claude
# Then: /startup
```

### See an example first

If you want to explore a working NLA before building your own, run
`/install-app`. It presents a catalog of example projects you can clone
and try immediately.

---

## How It Works

### The thin wrapper pattern

Your project has skill files in `.claude/skills/` that Claude Code discovers.
Framework skills are thin wrappers — they delegate to logic files in the
framework:

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

**Domain skills** (like `/format-article`) are full skill files in your
project — they don't delegate to the framework because they contain your
domain-specific logic.

### Path resolution

The LLM operates from your project's working directory:
- **Your files:** `app/overview.md`, `reference/friction-log.md`
- **Framework files:** `../nla-framework/core/nla-foundations.md`

The framework must be a sibling directory to your project.

---

## What's in the Framework

```
nla-framework/
├── core/
│   ├── nla-foundations.md     # Universal NLA concepts and principles
│   └── skills/               # Skill logic (delegated to by project wrappers)
├── install/                   # Intent files — source of truth for project generation
├── reference/                 # Framework maintenance records
└── .claude/skills/            # Framework-level skill entry points
```

`core/` contains universal NLA concepts — they work with any domain.
`install/` describes what a well-formed NLA needs — the source of truth
that `/create-app` reads when generating projects.

## What's in a Domain Project

```
my-project/
├── CLAUDE.md                  # Runtime identity and configuration
├── app/                       # The application (prose the LLM executes)
│   ├── overview.md            # What this NLA does
│   ├── shared/                # Values, voice, patterns, output spec
│   └── [task docs]            # Domain-specific tasks
├── reference/                 # Maintenance records
├── .claude/skills/            # Skill entry points (wrappers + domain skills)
└── lib/                       # Traditional code (if needed)
```

---

## Upgrading

```bash
cd nla-framework
git pull
```

Thin wrappers point to framework files, so updated logic takes effect
immediately. For structural changes (new skills, changed expectations),
run `/update` in your project — it compares current intent against what
was installed and proposes changes.

---

## Improving It

NLAs improve through use:

1. Use the application
2. Notice what works and what doesn't
3. Log observations with `/friction-log`
4. Process them with `/maintain`

One material — prose — and one process — read, think, write — at every
level.

---

## Getting Help

Ask the AI. Run `/guide` for a contextual walkthrough, or describe what
you're trying to do — the AI has read the documentation and can orient you.

---

## Learn More

- [The Documentation Is the Application](https://github.com/mightytech/nla-office-hours/blob/main/content/the-documentation-is-the-application.md)
  — a probe report on the NLA paradigm
- [NLA Office Hours](https://github.com/mightytech/nla-office-hours) —
  interactive introduction
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute (it's different
  from what you're used to)
