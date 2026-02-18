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
2. **`scaffold/CLAUDE.md`** — How a domain project's runtime config is structured
3. **`scaffold/app/overview.md`** — How a domain project describes itself

Don't read every scaffold file now. You'll read each one as a structural reference immediately before generating its counterpart.

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

### Two Categories

**1. Copied verbatim from scaffold** (no generation needed):

| File | Notes |
|------|-------|
| `.claude/skills/startup/SKILL.md` | Thin wrapper — identical for all projects |
| `.claude/skills/maintain/SKILL.md` | Thin wrapper |
| `.claude/skills/friction-log/SKILL.md` | Thin wrapper |
| `.claude/skills/plan/SKILL.md` | Thin wrapper |
| `.claude/skills/preferences/SKILL.md` | Thin wrapper |
| `.claude/skills/validate/SKILL.md` | Thin wrapper — identical for all projects |
| `reference/friction-log-archive.md` | Empty archive structure |
| `reference/feedback-log-archive.md` | Empty archive structure |
| `lib/.gitkeep` | Directory placeholder |
| `reference/sessions/.gitkeep` | Directory placeholder |
| `config/.gitkeep` | Config sub-directory placeholder |
| `.gitignore` | Excludes config.md and config/ from git |

**2. Generated from conversation** (read scaffold file as structural reference, then generate new content):

| Generated file | Read this scaffold file first | What to customize |
|---|---|---|
| `CLAUDE.md` | `scaffold/CLAUDE.md` | Skills table, project identity, environment section |
| `app/overview.md` | `scaffold/app/overview.md` | Task descriptions, diagrams, skills table, document hierarchy |
| `app/shared/voice-and-values.md` | `scaffold/app/shared/voice-and-values.md` | Tone, values, editorial standards from conversation |
| `app/shared/common-patterns.md` | `scaffold/app/shared/common-patterns.md` | Domain-specific patterns (start minimal, user iterates) |
| `app/shared/output-spec.md` | `scaffold/app/shared/output-spec.md` | Output format from conversation |
| `app/[task-name].md` | `scaffold/app/format-article.md` | Purpose, steps, judgment calls for the domain task |
| `.claude/skills/[task-name]/SKILL.md` | `scaffold/.claude/skills/format-article/SKILL.md` | Skill entry point for domain task |
| `reference/design-rationale.md` | `scaffold/reference/design-rationale.md` | Starter rationale with creation decisions |
| `reference/system-status.md` | `scaffold/reference/system-status.md` | Actual tasks and skills |
| `reference/friction-log.md` | `scaffold/reference/friction-log.md` | Keep format and guidance, remove sample entry |
| `reference/feedback-log.md` | `scaffold/reference/feedback-log.md` | Keep format and guidance |
| `README.md` | `scaffold/README.md` | Project name, tasks, skills, getting started |
| `app/config-spec.md` | `scaffold/app/config-spec.md` | Configurable behaviors, defaults, constraints from conversation |
| `config.md` | `scaffold/config.md` | Starter config with defaults from config-spec |

### Generation Order

Follow this order — later files reference earlier ones:

1. **Directory structure** — Create all directories with `mkdir -p`
2. **Copied files** — Thin wrapper skills, .gitkeep files, friction-log-archive
3. **Shared context** — voice-and-values.md, common-patterns.md, output-spec.md
4. **Task docs and skills** — Task-specific files for each task
5. **Integration files** — overview.md, CLAUDE.md, README.md (generated last because they reference everything above)
6. **Reference files** — design-rationale.md, system-status.md, friction-log.md
7. **Config files** — config-spec.md, config.md, .gitignore

### How to Generate Each File

For each file in category 2:

1. **Read the scaffold reference** listed in the table above
2. **Use it as structural guidance** — match the section organization, level of detail, and relationship patterns
3. **Generate new content** based on the conversation — don't copy the scaffold's sample content
4. **Keep framework references intact** — paths like `../nla-framework/core/` must be preserved exactly

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
| **Validation** | `/validate` checks that your system's internal references are consistent, and can trace through docs to debug when output doesn't match expectations. |

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

**Tip for first-time users:** If they seem unsure or want to see a working example first, mention `/create-sample-app` — it installs a complete sample NLA they can explore before building their own.

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
- **Don't copy scaffold prose** — Read scaffold for structure, generate fresh content for the domain. The sample article-formatter language shouldn't leak into a ticket-classification project.
