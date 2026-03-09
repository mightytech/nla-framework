# Maintenance Session: Foundations Principles and Coherence Validation

**Date:** 2026-03-08
**Status:** Complete

## Intent
Add two principles to nla-foundations.md that were implicit but operationally
important, and create a coherence validation mode to catch whole-document quality
issues after edits.

## Changes Made
- **"Imperfection Is Assumed" principle** added to nla-foundations.md (#1). Names the
  assumption underlying the improvement loop, friction log, and human oversight.
  Removed "Iterate Through Documentation" (#7) which became redundant — its content
  was covered by the new principle + the Improvement Loop rhythm.
- **"Principles and Procedures" principle** added to nla-foundations.md (#3). Captures
  the distinction between prose that shapes judgment (principles) and prose that
  produces specific behaviors (procedures). Originally inline in #2, promoted to its
  own principle after coherence review showed weight imbalance.
- **Coherence review validation mode** added as fifth `/validate` mode. Re-reads
  startup files checking internal redundancy, flow, and whole-document coherence.
  Complements architecture review (between-document consistency) with within-document
  consistency.
- **Post-edit coherence step** added to both core and framework maintain skills.
  After structural changes to foundational files, re-read the full document for
  coherence.
- **"Bug tracker" echo** resolved between CLAUDE.md and nla-foundations — removed
  redundant metaphor from nla-foundations, kept in CLAUDE.md where it fits naturally.
- **Friction log entry** added for `/startup` `disable-model-invocation` question —
  deferred to a future `/think` session.

## Blast Radius
- nla-foundations.md changes affect all domain projects (loaded at startup)
- validate and maintain skill changes affect all domain projects (via thin wrappers)
- README, framework wrapper, friction log changes affect framework only

## Decisions Made
- **"Imperfection Is Assumed" included; "machines speaking human" excluded** — The
  operational test: does naming this explicitly change runtime behavior? Imperfection
  changes how the AI holds its instructions (flag friction proactively). The
  philosophical motivation doesn't change what the AI does.
- **"Iterate Through Documentation" removed** — Adding #1 created a three-way echo
  (#1, old #7, Improvement Loop). Removing #7 tightened the document; the idea lives
  in two places (principle + rhythm) instead of three.
- **Principles/procedures promoted from inline to standalone** — Coherence review
  showed weight imbalance when attached to #2. The topic (how to write effective NLA
  prose) is distinct enough from "the fix is in the docs" to earn its own number.
- **Coherence review in validate + procedure in maintain** — Discussed three options
  for catching post-edit coherence issues: maintain step, validate mode, or
  foundations principle. AI self-assessed that a principle alone wouldn't reliably
  produce the behavior. Went with both maintain (routine catch) and validate
  (deliberate review).
- **No framework /startup skill** — Framework doesn't need it; its user-facing paths
  (/create-app, /install-app) load their own context. Domain project /startup
  auto-invocation logged as separate question.

## Debrief
1. **The coherence check proved itself immediately.** Built the mode, ran it, and it
   caught two real issues (weight distribution and cross-document echo) in the same
   session. Fast feedback loop.
2. **The session surfaced a meta-principle about NLA writing.** "Principles shape
   judgment; procedures produce behavior" started as self-assessment, became a
   principle, then immediately demonstrated itself — the coherence step went into
   maintain as a procedure because a principle alone wouldn't work.
3. **Surface area tracking matters.** Caught a missed file (framework maintain
   wrapper) during implementation. Mode additions to existing skills don't have a
   checklist equivalent to "Adding a New Skill."
4. **The "read the whole file" ask caught a real problem.** Without the explicit
   request to re-read nla-foundations as a unit after adding #1, the #7 redundancy
   would have shipped. This directly motivated the coherence validation mode.

## State at Close
**What's working:** nla-foundations has 8 principles including the two new ones.
Coherence validation mode operational. Maintain skill has post-edit coherence step.

**What's pending:** 3 friction log entries pending (startup auto-invocation [new],
bare project path, friction log git storage). 2 deferred (maintain thin wrapper,
context window awareness). 1 feedback item (export hybrid approach).

**Where to pick up:** The startup auto-invocation question is fresh and interesting
but not urgent. The export hybrid approach (feedback #9) is the largest pending item.
