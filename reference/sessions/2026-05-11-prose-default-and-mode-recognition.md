# Maintenance Session: Prose-default principle and create-app mode-recognition

**Date:** 2026-05-11
**Status:** In Progress

## Intent

Resolve two related friction entries from the 2026-05-10/11 nla-archetypes
creation session, both about how the AI should hold the conversation in
design-sensitive moments.

- **2026-05-10 (AskUserQuestion overreach):** establish a framework-level
  prose-default principle that loads into every session's prompt. The
  prior session's lapse happened despite a user-private memory note;
  memory-only mitigation was insufficient. Move the guidance to a channel
  with more weight — CLAUDE.md, which loads at session start.
- **2026-05-11 (mode-recognition):** make `/create-app` recognize when
  the user is inviting collaborative refinement rather than structured
  extraction, so the most consequential design decisions (the Guernica
  value in nla-archetypes' case) emerge through collaborative
  articulation rather than mechanical Q&A.

The two entries pull in the same direction but address different layers:
tool-choice (5/10) vs. whole-mode-recognition (5/11). Both got addressed
in this session.

## Changes Made

- **Framework's own `CLAUDE.md`** — added a "Default to prose for design
  conversations" bullet to Grounding Principles. Covers framework
  sessions: `/create-app`, `/maintain`, `/think`, any conversation-heavy
  skill run from the framework. The bullet closes with a sentence
  connecting the principle to `core/nla-foundations.md` principle #2
  ("the LLM bridges human flexibility and computational rigidity") —
  naming the foundational truth that makes enum-for-design-questions a
  category error rather than a preference.

- **`install/CLAUDE-intent.md`** — added the same prose-default bullet
  to Execution Principles (alongside "the cardinal rule" and "flag
  uncertainty"). Propagates to every domain project's CLAUDE.md via
  `/create-app` (for new NLAs) and `/update` (for existing ones).

- **`.claude/skills/create-app/SKILL.md`** — two additions:
  - A "Between Phase A and Phase B: Recognize the mode" transition
    section that distinguishes extraction from collaborative refinement
    and names four signals for the latter (working prompt or sample
    artifact, length about *why*, explicit invitation of AI perspective,
    user-named-but-unresolved tensions).
  - A "User arrives with rich conceptual work" entry in Conversation
    Edge Cases, as a sibling to "User provides everything upfront."

- **`install/update-notes.md`** — entry for the `install/CLAUDE-intent.md`
  change, so existing NLAs running `/update` see why their CLAUDE.md is
  getting a new Execution Principle.

## Decisions Made

- **Awareness-level placement, not config-directive** — the user
  proposed a lateral option of making this a default config directive
  users could change. Rejected: config is for user-facing preferences
  (voice, output length), and AskUserQuestion behavior is a craft-level
  decision about how the AI uses its own tools. Making it configurable
  would dilute the principle ("configurable" reads as "negotiable") and
  put a micro-choice in front of the user that they shouldn't have to
  think about. The asymmetry is also load-bearing: when AskUserQuestion
  is right, prose still works; when prose is right, AskUserQuestion
  fails. Prose-as-default is safer in either case.

- **Universal NLA truth, not personal preference** — discussed whether
  this was a quirk of how this user works or a universal NLA principle.
  Landed on universal, with reasoning: the LLM's value proposition is
  handling nuance (foundations principle #2). Using enums for design
  questions surrenders that value — a category error in how the
  affordance is used. Also contradicts intent-over-rules (principle #4):
  enums *are* rules. Same logic applies to standard Claude Code use, not
  just NLA framework use — the surface area is just smaller there
  (operational questions dominate).

- **Bullet in Grounding Principles, not new Execution Principles
  section** — for framework CLAUDE.md, considered creating a parallel
  Execution Principles section to match consumer NLAs' structure. About
  3-4 bullets would migrate. Skipped: scope creep for the friction
  entries at hand. The structural symmetry isn't urgent, and the mix of
  posture/practice bullets already in Grounding Principles absorbs the
  new one cleanly. Captured the reorganization possibility implicitly in
  this session log — could surface as a friction entry if it feels worth
  it later.

- **Awareness-level only, no skill-level reinforcement in
  `core/skills/maintain.md` or `core/skills/think.md`** — the 2026-05-10
  friction entry's Notes argued for in-skill reminders at the
  lapse-prone moments. Deferred: the awareness-level placement loads
  into every session's prompt via CLAUDE.md, which is exactly the
  structural change the entry argued was needed (memory-only mitigation
  had failed). If recurrence shows up despite this, trigger-level
  reinforcements can be added then. Pre-emptive layering wasn't
  warranted. `core/skills/maintain.md` already has scoped guidance
  ("when using plan mode"); broadening it can wait for evidence.

- **5/11 entry resolved through skill-level work only, not parallel
  install/CLAUDE-intent.md addition** — collaborative refinement *is*
  prose by definition, so the broader prose-default principle from the
  5/10 work already covers the mode-recognition behavior at the
  awareness level. The skill-specific transition section + edge case
  covers the trigger level for `/create-app` specifically. No need for
  a separate "recognize the mode" principle in `install/CLAUDE-intent.md`
  — it would be a generalization the friction evidence doesn't support
  (the lapse was specific to `/create-app`'s extraction-shaped Phase B).

## What Didn't Work

- **Initial proposal missed the framework-side coverage entirely** —
  first draft only addressed `install/CLAUDE-intent.md` (consumer side).
  The user caught it: "but it has to be executed somewhere — downstream
  but also here in the framework (it's causing issues during maintenance
  sessions)." The framework's own CLAUDE.md is hand-written, not
  synthesized from `install/CLAUDE-intent.md`, so the intent-file
  channel alone covers only consumer NLAs. Revised proposal added
  framework's CLAUDE.md as a parallel placement. Useful reminder: when
  framework changes propagate via the intent files, the framework
  itself is a separate consumer that needs its own coverage if the
  guidance applies to framework sessions too. Worth a friction log entry
  if this conflation happens again.

## Friction Log Entries Processed

- **2026-05-11 — /create-app's structured Q&A misses the
  collaborative-refinement mode** — resolved. Skill-level placement in
  `.claude/skills/create-app/SKILL.md`. Archived.
- **2026-05-10 — AskUserQuestion overreach despite user-private memory
  note** — resolved. Awareness-level placement in framework `CLAUDE.md`
  + `install/CLAUDE-intent.md`. Update-notes entry. Archived.

## Debrief

[To be added at session close via `/debrief` or in `/close`.]

## State at Close

[To be finalized at session close.]
