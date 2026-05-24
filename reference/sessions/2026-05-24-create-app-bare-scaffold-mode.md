# Maintenance Session: Bare Scaffold Mode in /create-app

**Date:** 2026-05-24
**Status:** In Progress

## Intent

Resolve the 2026-02-23 friction-log entry "/create-app bare project path: missing guidance and speculative seeds" by giving `/create-app` an explicit handling for users who want a scaffolded NLA they'll author in `/maintain`. Two behavioral shifts:

1. The skill stops grinding through Phase B's content extraction (voice, values, tasks) when the user has signaled they want to defer authoring. The AI recognizes the bare signal during/after Phase A, confirms in prose, and proceeds to mechanical generation.
2. Shared-context files stop carrying invented content from a domain name alone. They're generated as minimal stubs with explicit "unauthored" framing, and a preloaded umbrella friction-log entry surfaces the authoring work in the user's first `/maintain` session — leveraging the existing maintenance queue rather than inventing a new signaling mechanism.

The 2026-02-24 nla-writer follow-up observation (rich-context-but-blank case: good seeds become invisible because they're not bad enough to revisit) is *adjacent* friction and explicitly out of scope here. Recording the boundary in design-rationale prevents future drift back into a single combined fix.

## Changes Made

- **`.claude/skills/create-app/SKILL.md`** — multiple coupled additions:
  - "Between Phase A and Phase B: Recognize the mode" extended to three shapes (Extraction / Collaborative-refinement / Bare scaffold). Bare-scaffold definition leads with posture ("AI's job is not to extract or refine — it's to set up scaffolding and get out of the way"); confirmation prose included; bare-scaffold signals enumerated as a parallel list to collaborative-refinement signals.
  - "Phase B: Targeted Follow-ups" gets a top paragraph: if bare scaffold was recognized, Phase B collapses; confirm name only.
  - "Phase C: Summary and Confirmation" gets a bare-scaffold summary template variant.
  - "Conversation Edge Cases" gets a "User wants a bare scaffold" entry pointing at the recognition beat and the Bare Scaffold Mode subsection.
  - New "Bare Scaffold Mode" subsection in File Generation, between Domain File Structures and Generation Order. Specifies per-category behavior, stub file shapes including the exact unauthored-stub header, the preloaded friction-log entry template (with creation-date placeholder), and the "why two surfaces" framing for the stub+friction-log pairing.
  - "Generation Order" gets a one-line pointer noting which steps differ for bare-scaffold.
  - "Narration" table gets a bare-scaffold row.
  - "Post-Creation" gets a bare-scaffold next-steps variant (step 5 is `/maintain`, not running a task).
  - "Internal Consistency Check" gets bare-mode items 11-17 (no task docs, no domain skills, stubs verified, output-spec absent, preloaded friction entry exists, overview reflects bare state, skills tables clean).
  - "What You Don't Do" gets a "Don't invent content when bare scaffold was confirmed" bullet.
- **`reference/design-rationale.md`** — added "Bare Scaffold Path in /create-app" section before "Adding Decisions." Captures: what was decided, why this shape (reuse existing recognition pattern, two-surface epistemic signal, leverage existing maintenance queue), rejected alternatives (universal Phase B/C broadening; CLI flag), adjacent case explicitly out of scope (2026-02-24 nla-writer rich-context-but-blank inversion), architectural observation (deferred — bare-mode generation is a strong candidate for `lib/` extraction once Python standards exist; cross-references the new 2026-05-24 friction-log entry), blast radius.
- **`reference/friction-log.md`** — added new 2026-05-24 entry "Scaffold-first generation as the unified /create-app mechanism." Captures the architectural reframe surfaced during this session: split `/create-app` into deterministic scaffold generation + AI-applied conversation edits. Pairs with the existing 2026-04-16 cluster (Python standards, prose-vs-code distinction, nla-compiler experiment). Status: pending. Waits on Python standards / nla-compiler availability.
- **`reference/friction-log.md`** — removed the 2026-02-23 entry (moved to archive).
- **`reference/friction-log-archive.md`** — added the 2026-02-23 entry at the top (most recent resolution), with `Status: resolved` and a `Resolved:` line referencing the design-rationale section and naming the explicit out-of-scope boundary.
- **`reference/sessions/2026-05-24-create-app-bare-scaffold-mode.md`** — this session log (internal).

## Decisions Made

- **Extend the existing mode-recognition beat (third value) rather than create a new recognition.** The 2026-05-11 mode-recognition pattern (extraction vs. collaborative-refinement) is fundamentally "what conversation is the user inviting?" — bare is a third answer on the same axis, not a parallel axis. Reuses existing pattern; no new machinery.
- **Two-surface epistemic signaling: stub header *and* preloaded friction-log entry.** Stub headers catch the gap at task-execution time (LLM reads voice.md and sees "unauthored"). Friction-log entry catches it at `/maintain` session start (the maintainer sees authoring work in the queue). Different surfaces for the same signal — covering both is light belt-and-suspenders, not redundancy.
- **Prose recognition with confirmation, not CLI flag.** Per CLAUDE.md's prose-default principle. User talks to an AI, not a Python program. AI confirms: "Sounds like you want a bare scaffold named X — empty stubs you'll author in /maintain. Right?"
- **Phase B collapses to project-name-only in bare mode.** Skip voice/values/tasks/output/audience. The framework needs a name and a place to put things; everything else is deferred.
- **Reject "broaden Phase B/C universally."** Considered making tasks structurally optional throughout the skill (the route the 2026-02-24 addendum hints at). Rejected: bare is a specific user-requested shape, not a general restructuring. Broadening universally would require the AI to improvise at every step rather than having a clear starting signal. The recognition beat *is* the structural signal.
- **2026-02-24 nla-writer case explicitly out of scope.** Different friction shape (rich-context-but-blank vs. thin-context-but-blank). Same generated content, opposite failure modes depending on input richness. Treating both in one fix would conflate them. Recorded as adjacent in design-rationale.

## What Didn't Work

*(To be filled in if applicable.)*

## Friction Log Entries Processed

- **2026-02-23 — /create-app bare project path: missing guidance and speculative seeds** — resolved this session via bare-scaffold mode addition to `.claude/skills/create-app/SKILL.md` + design-rationale entry. Archived.

## Debrief

*(To be captured at session close.)*

## State at Close

*(To be filled in at session close.)*
