# Maintenance Session: Guide Design Rationale

**Date:** 2026-03-05
**Status:** Complete

## Intent
Add design rationale as a source for the /guide skill's maintainer orientation, so
"why" questions about framework architecture get better answers.

## Changes Made
- Added `reference/design-rationale.md` reference to the maintainer section of
  `.claude/skills/guide/SKILL.md`. Newcomer section left unchanged — newcomers ask
  conceptual "why" (answered by nla-foundations.md), not architectural "why."

## Blast Radius
- Framework only. No core skill or intent file changes.

## Decisions Made
- **Maintainers only, not newcomers** — Design rationale answers "why thin wrappers?"
  not "why NLAs?" Different audiences, different sources.
- **Future essay-discussion NLA** — Discussed putting the probe report essay into an
  NLA that could answer questions about it, with the framework code and design rationale
  as supporting context. Not built this session; noted as a future `/create-app` project.

## Debrief
1. **Conversation before implementation.** The actual change was two lines, but the
   conversation about whether/where to include design rationale produced a clearer
   decision than jumping straight to editing.
2. **The essay NLA idea emerged naturally.** Starting from "would my essay help /guide?"
   led to a better idea — a purpose-built NLA for discussing the essays. The framework
   code + design rationale become the evidence layer beneath the essay's arguments.

## State at Close
**What's working:** /guide maintainer section now includes design rationale.

**What's pending:** Same as previous session — 2 pending friction entries, 2 deferred,
1 feedback item. Plus the essay-discussion NLA as a future project idea.
