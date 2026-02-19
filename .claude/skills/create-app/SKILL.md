---
name: create-app
description: Create a new NLA project through guided conversation. Asks about your domain, voice, and tasks, then generates a tailored project.
disable-model-invocation: true
---

# Create NLA Application

You are helping someone build a new Natural Language Application. This is often their first interaction with the NLA framework — make it a good one.

**Your job:** Have a short conversation to understand what they want to build, then generate a complete, working NLA project tailored to their domain. The result should be ready to `git init` and start using immediately.

**Philosophy:** The first experience of an NLA framework should itself be an NLA interaction — flexible interface on top (conversation), structure underneath (generated project). Don't make the user fill out a form. Talk to them.

---

## Before You Begin

Read these to understand what a well-formed NLA project looks like:

1. **`core/nla-foundations.md`** — What NLAs are, key principles
2. **`install/CLAUDE-intent.md`** — What an NLA's runtime identity should establish
3. **`install/structure-intent.md`** — What directory structure and reference files an NLA needs
4. **`install/skills-intent.md`** — What skill wrappers an NLA should have

These intent files are your primary source for structural guidance. They describe WHAT each file should contain and WHY; you generate content that fits the user's domain.

---

## Conversation Flow

Guide an adaptive conversation. Core principle: **parse what the user provides, fill in what you can, ask about what's missing.** Never force Q&A when the user already gave you the answer.

### Information Targets

Gather these through conversation (not as a checklist):

1. **Project name** — used as directory name (lowercase, hyphens)
2. **What the NLA does** — domain description in a sentence or two
3. **Primary task(s)** — name and what the LLM should do for each
4. **Voice/tone** — how output should sound
5. **Output format** — Markdown, HTML, JSON, plain text, etc.
6. **Audience** — who reads the output
7. **Configuration** — what behaviors should users be able to customize?

### Phase A: Opening

Welcome the user. Briefly explain what `/create-app` does:

> I'll ask a few questions about what you want to build, then generate a complete NLA project for you. The whole thing takes a few minutes.

Then ask an open question: **What are you building?** Accept anything from a one-liner to a full paragraph. Parse whatever they provide — if they mention voice, tasks, and audience in one message, don't ask again.

### Phase B: Targeted Follow-ups

Based on what's missing after Phase A, ask focused follow-up questions. Group related items together. Max 2-3 questions at a time.

**Groupings that work well:**
- Voice + audience (they inform each other)
- Output format + task description (what the LLM produces shapes how it works)
- Multiple tasks (if hinted at — "Do you need separate tasks for X and Y, or is that one task?")
- Configuration (what should users be able to customize?)

**Configuration guidance:** Ask what behaviors the app developer wants users to be able to customize. Examples: "Should users be able to adjust the tone? Change output length? Modify specific task behaviors?" Some developers want tight control ("only output format"); others want maximum flexibility ("let them change anything — it's an LLM"). If the developer isn't sure, suggest starting with common settings (voice adjustments, output preferences) and note that `/maintain` can expand the config-spec later.

**Provide examples and suggestions** to help users who aren't sure:
- Voice: "Formal and authoritative? Warm and conversational? Technical and precise?"
- Output format: "Clean Markdown is the most common. Some projects use HTML, JSON, or structured plain text."
- Task naming: "Task names become skill names. Short, verb-based: `format-article`, `classify-ticket`, `draft-response`."

### Phase C: Summary and Confirmation

Present a summary of what will be created:

```
Project: [name]
Location: ../[name]/ (sibling to nla-framework)

What it does: [one-sentence description]
Voice: [tone summary]
Output: [format]

Tasks:
  - /[task-name]: [what it does]

Files to generate: [count]
```

**Wait for explicit confirmation before creating any files.** This is the last chance to catch misunderstandings.

### Conversation Edge Cases

- **User provides everything upfront** — Skip to Phase C. Don't ask questions you already have answers to.
- **Multiple tasks** — Generate a task doc and skill for each. All integration files (overview, CLAUDE.md) reflect all tasks.
- **User changes mind** — The confirmation step exists for this. Adjust and re-summarize.
- **Vague voice description** ("professional" or "friendly") — Generate a reasonable starter voice doc. Note to the user that `/maintain` can refine it later.

---

## File Generation

### Three Categories

**Category 1 — Generated from intent files (mechanical):**

These files have the same structure in every NLA. Read reference implementations from
`install/skills-intent.md` and templates from `install/structure-intent.md`.

| File | Source |
|------|--------|
| `.claude/skills/startup/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `.claude/skills/maintain/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `.claude/skills/friction-log/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `.claude/skills/plan/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `.claude/skills/preferences/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `.claude/skills/validate/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `.claude/skills/install/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `.claude/skills/update/SKILL.md` | Reference wrapper in `install/skills-intent.md` |
| `reference/friction-log-archive.md` | Structure in `install/structure-intent.md` |
| `reference/feedback-log-archive.md` | Structure in `install/structure-intent.md` |
| `lib/.gitkeep` | Empty file |
| `reference/sessions/.gitkeep` | Empty file |
| `config/.gitkeep` | Empty file |
| `.gitignore` | Template in `install/structure-intent.md` |

**Category 2 — Generated from intent files + conversation (structured framework files):**

These files follow framework-defined structures but are customized with conversation
content. Read reference structures from intent files, then generate content that fits
the user's domain.

| File | Structural source | What to customize |
|------|-------------------|-------------------|
| `CLAUDE.md` | `install/CLAUDE-intent.md` reference structure | Project identity, skills table, modes, environment |
| `reference/design-rationale.md` | `install/structure-intent.md` | Starter rationale with creation decisions for this domain |
| `reference/system-status.md` | `install/structure-intent.md` | Actual tasks and skills from the conversation |
| `reference/friction-log.md` | `install/structure-intent.md` | Keep format and guidance, seed patterns for this domain |
| `reference/feedback-log.md` | `install/structure-intent.md` | Keep format and guidance |
| `reference/installed-packages.md` | `install/structure-intent.md` | Add framework as first entry with date and commit hash |
| `README.md` | `install/structure-intent.md` | Project name, tasks, skills, getting started |
| `app/config-spec.md` | `install/structure-intent.md` | Configurable behaviors from the conversation |
| `config.md` | `install/structure-intent.md` | Starter config with defaults from config-spec |
| `config/maintenance.md` | Always-active maintenance preferences | Propose before editing, summarize plans |

**Category 3 — Generated from conversation (domain-specific):**

These files are unique to the user's domain. No framework-level structural source exists
because they vary completely by project. The structural guidance below is all you need.

| File | Structure guidance |
|------|-------------------|
| `app/overview.md` | See "Domain File Structures" below |
| `app/shared/voice-and-values.md` | See "Domain File Structures" below |
| `app/shared/common-patterns.md` | See "Domain File Structures" below |
| `app/shared/output-spec.md` | See "Domain File Structures" below |
| `app/[task-name].md` | See "Domain File Structures" below (one per task) |
| `.claude/skills/[task-name]/SKILL.md` | Domain skill pattern in `install/skills-intent.md` (one per task) |

### Domain File Structures

**`app/overview.md`** — How the NLA's pieces connect:
- What this NLA does (1-2 paragraphs)
- Tasks table: Task name, what it does, source file
- How it connects (brief description or diagram of the workflow)
- Skills table: all skills with purpose
- The improvement pipeline (friction-log → maintain cycle)
- For humans: key workflow patterns (change behavior, debug, add tasks)
- Document hierarchy: tree of all `app/` files with descriptions
- Document index: links to all docs
- Getting started: first-time setup

**`app/shared/voice-and-values.md`** — Tone, personality, editorial standards:
- Who we are (brief identity)
- Voice: 3-5 tone principles, each with a clear/not pattern (e.g., "Clear, not clever")
- The test: one question to check if output matches the voice
- Values: 2-4 editorial values with explanations
- Editorial standards: domain-relevant rules (attribution, links, structure, etc.)

**`app/shared/common-patterns.md`** — Recurring patterns the LLM should recognize:
- Start minimal — 2-4 patterns that are clearly relevant to the domain
- Each pattern: what to look for, what to do, when NOT to apply
- Note that patterns grow through `/friction-log` + `/maintain` iteration

**`app/shared/output-spec.md`** — Output format specification:
- Format: what format and why
- Structure: general template showing the shape of typical output
- Flexibility: what varies, what's consistent
- What stays raw: what the NLA should NOT transform

**`app/[task-name].md`** — One doc per task (the actual application logic):
- Purpose: what this task does in one sentence
- Input: what it receives
- Output: what it produces
- Prerequisites: which docs to read first (voice, patterns, output spec)
- Processing steps: numbered steps with enough detail for the LLM to follow
- Judgment calls: when to flag uncertainty, domain-specific edge cases

### Generation Order

Follow this order — later files reference earlier ones:

1. **Directory structure** — Create all directories with `mkdir -p`
2. **Category 1 files** — Thin wrapper skills, .gitkeep files, archives, .gitignore
3. **Shared context** — voice-and-values.md, common-patterns.md, output-spec.md
4. **Task docs and skills** — Task-specific files for each task
5. **Integration files** — overview.md, CLAUDE.md, README.md (generated last because they reference everything above)
6. **Reference files** — design-rationale.md, system-status.md, friction-log.md, feedback-log.md, installed-packages.md
7. **Config files** — config-spec.md, config.md, config/maintenance.md

### How to Generate Each File

**Category 1 (mechanical):**
Read the reference implementation from the intent file and reproduce it. These are
identical across all projects.

**Category 2 (intent + conversation):**
1. Read the reference structure from the relevant intent file
2. Use it as structural guidance — match the section organization and purpose
3. Generate content based on the conversation — don't use sample domain content
4. Keep framework references intact — paths like `../nla-framework/core/` must be preserved exactly

**Category 3 (conversation only):**
1. Read the structural guidance in "Domain File Structures" above
2. Generate content entirely from the conversation
3. Match the voice and domain the user described
4. Start minimal — especially common-patterns.md. Better to add through `/friction-log` + `/maintain` than to guess

**Critical path details:**
- Framework references: `../nla-framework/core/nla-foundations.md`, `../nla-framework/core/skills/`
- Domain references: `app/`, `reference/`, `.claude/skills/` (project-relative)
- Thin wrappers point to: `../nla-framework/core/skills/[skill].md`

---

## Narration

As you create files, narrate by concept — not file-by-file. A sentence or two per concept, teaching as you go.

| Concept | What to say |
|---------|-------------|
| **Two channels** | `app/` is what the LLM reads and executes. `reference/` is for maintainers. They stay separate on purpose. |
| **Voice file** | This is the most important file — it shapes every decision the LLM makes about your content. |
| **Thin wrappers** | These delegate to the framework. When you `git pull` the framework, they pick up improvements automatically. |
| **Task doc** | This IS the application. Edit this file to change what the LLM does. |
| **Common patterns** | Starting minimal — as you use the system and run `/friction-log`, patterns will emerge and you'll add them here. |
| **Friction log** | Your learning journal. `/friction-log` captures observations, `/maintain` turns them into improvements. |
| **Config** | Config lets users personalize the NLA without editing the application. Their preferences live in `config.md`, separate from the app. `/preferences` creates and edits it. |
| **Validation** | `/validate` checks internal consistency, reviews architecture after restructuring, traces scenarios through docs, and debugs when output doesn't match expectations. |
| **Package management** | `/install` adds new capabilities from extension packages. `/update` keeps them current. Your install log tracks what's installed. |

Don't narrate every file. Group the thin wrappers, group the reference files. Focus on what helps the user understand the system.

---

## Post-Creation

After all files are created, provide:

```
Project created at ../[project-name]/

Next steps:
1. cd ../[project-name]
2. git init && git add -A && git commit -m "Initial NLA project"
3. Start Claude Code
4. Run /startup to load foundational context
5. Try /[task-name] with some sample content
```

**Tip for first-time users:** If they seem unsure or want to see a working example first, mention `/install-app` — it can install example NLA projects they can explore.

---

## Internal Consistency Check

Before reporting completion, verify:

1. **Skills table in CLAUDE.md** lists every skill in `.claude/skills/` (and no extras)
2. **Skills table in overview.md** matches CLAUDE.md
3. **Document index in overview.md** lists every file that exists
4. **system-status.md** tasks and skills match what was actually created
5. **Thin wrappers** all point to `../nla-framework/core/skills/[skill].md` with correct names
6. **README.md** references correct skill names
7. **config-spec.md** reflects configuration choices from the conversation
8. **config.md** has sensible defaults matching the config-spec
9. **.gitignore** excludes config.md and config/

If anything doesn't match, fix it before reporting done.

---

## What You Don't Do

- **Don't run `git init`** — The user handles post-creation setup
- **Don't create `.env` or credentials** — Note in CLAUDE.md if the project will need them
- **Don't over-generate** — Common patterns should start minimal. Better to add through `/friction-log` + `/maintain` than to guess
- **Don't use sample domain content** — Generate fresh content for the user's domain. Article-formatter language shouldn't leak into a ticket-classification project.
