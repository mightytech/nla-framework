---
name: guide
description: Context-aware help — understand how the NLA works, what to do next, and how the pieces connect. Adapts to your familiarity level.
disable-model-invocation: true
---

# Framework Context

This is the NLA Framework itself — shared infrastructure that domain projects depend on.
There is no `app/overview.md` here. Adapt your guidance to the user's familiarity:

## New to NLAs or the framework

If the user seems unfamiliar with NLAs — they're asking what this is, how it works, or
what they can do — orient them in this order:

1. **What NLAs are.** Read `core/nla-foundations.md` — the concept, why NLAs exist, what
   they're good at. Explain conversationally, not by reciting the doc.
2. **What the framework does.** It's the shared foundation for building NLAs. You describe
   what you want to build; the framework generates a working project. The "code" is
   documentation; the runtime is an LLM.
3. **What they can do from here.** `/create-app` builds a new project through a short
   conversation. `/install-app` lets them browse and install example projects to see what
   NLAs look like before building their own. Or they can keep asking questions — `/guide`
   stays active.

Start with what's immediately relevant to their question. Don't dump all three sections
at once — offer to go deeper. The goal is for someone who knows nothing about NLAs to
leave the conversation understanding the concept and feeling ready to build.

## Framework maintainer

If the user is already working in the framework (in `/maintain`, navigating confidently,
using framework terminology), orient them to framework internals:

- **Architecture** — `core/` (foundations + skill logic, affects all projects), `install/`
  (intent files, affects project generation), `reference/` (maintenance records, local).
- **Skill catalog** — the skills table in `CLAUDE.md` and what each skill does.
- **Working rhythms** — from the Working Rhythms section of `core/nla-foundations.md`.
- **What's pending** — friction log and feedback log status.

Read and follow `core/skills/guide.md`.
