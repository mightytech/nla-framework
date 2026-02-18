# NLA Framework — Install Manifest

This directory describes what an NLA needs to be built on the NLA Framework. An `/install`
or `/update` skill reads these files and applies them to the target NLA.

---

## What This Package Is

The NLA Framework is the foundation for Natural Language Applications — software where
documentation is source code and an LLM is the runtime. It provides grounding principles,
maintenance workflows, configuration infrastructure, and a shared skill library.

This is not an extension (like penny post). It's the base layer. Every NLA built on
this framework should have what these intent files describe.

## Prerequisites

- **Claude Code** — The NLA runs inside Claude Code, which provides skill discovery,
  file access, and the LLM runtime.
- **This repo cloned as a sibling** — `../nla-framework/` relative to the NLA. Thin
  wrapper skills reference this path.

## What's in This Directory

Each file describes the **intent** of what a framework-based NLA should have at a
specific integration point. The installing AI reads these intents and synthesizes them
into the NLA's existing files in whatever way fits that NLA's structure and voice.

| File | Integration Point | Purpose |
|------|------------------|---------|
| `CLAUDE-intent.md` | NLA's CLAUDE.md | Runtime identity, grounding principles, modes, execution rules |
| `skills-intent.md` | NLA's .claude/skills/ | Framework skill wrappers |
| `structure-intent.md` | NLA's directory layout | Required directories and reference files |

## How This Relates to `/create-app`

`/create-app` is the bootstrap — it creates a new NLA from scratch through conversation.
It solves the chicken-and-egg problem: you can't `/install framework` if you don't have
an NLA yet.

These intent files describe what `/create-app` produces. They serve as:

- **Reference for `/create-app`** — what a well-formed NLA should have
- **Specification for `/update`** — what to diff against when the framework evolves
- **Documentation** — a readable description of the framework's expectations

When the framework adds new capabilities (e.g., the feedback log), the intent files are
updated. `/update` can then detect what existing NLAs are missing and create it.

## How Installation Works

For new NLAs, `/create-app` handles everything. For existing NLAs being updated:

1. Read each intent file in this directory.
2. For each one, examine the target NLA's current state at that integration point.
3. Synthesize what's missing into the NLA's existing files — don't paste, integrate.
   Match the NLA's voice, structure, and conventions.
4. Log what was done and why in the NLA's install log (see below).

## The Install Log

After making changes, the installing AI should record what it did in the target NLA.
This log is how future updates know what came from this package.

For each integration point changed, record:
- Which package and intent file prompted the change
- What the intent was (in your own words)
- What concrete changes were made and where
- The state of this install directory at the time (commit hash or date)

The format and location of this log is up to the NLA. A reasonable default:
`reference/installed-packages.md`.

## Updating

When this install directory changes (new intent, revised intent, removed intent),
the NLA's `/update` skill should:

1. Diff this directory against the state recorded in the install log.
2. For changed intents, re-read the intent and re-synthesize. Use the install log
   to understand what was previously done.
3. For new intents, apply them as a fresh install.
4. Update the install log.

---

*This manifest is maintained as part of the NLA Framework. Changes here affect what
every framework-based NLA is expected to have.*
