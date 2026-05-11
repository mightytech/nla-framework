# Session: nla-archetypes creation and create-app friction capture

**Date:** 2026-05-10 to 2026-05-11
**Status:** Complete

## Intent

Use the framework's `/create-app` to generate a new domain project — `nla-archetypes` — for extracting structural archetypes from portraits and interviews like the ones in Studs Terkel's *Working*. The output is meant to be runtime context for downstream NLAs (focus-group simulations, character-construction tools) where the goal is perspectives that *surprise* rather than flatten into AI-generated centroids.

This was framework-side work to the extent that it exercised `/create-app` and surfaced friction observations about it. The actual domain project lives at `../nla-archetypes/` (sibling git repo) and isn't tracked from here.

## Changes Made (framework side)

- **`reference/friction-log.md`** — two pending entries added:
  - **2026-05-10 — AskUserQuestion overreach despite user-private memory note.** I invoked `AskUserQuestion` twice for "yes-but"/"yes-and" shaped design questions where prose was the right format; the user redirected both times. A user-private memory note saying don't-do-this didn't prevent the lapse. Argues for framework-level guidance in `install/CLAUDE-intent.md` and `core/skills/create-app.md`.
  - **2026-05-11 — /create-app's structured Q&A misses the collaborative-refinement mode.** The most consequential design decision in nla-archetypes (the "true like fiction" Guernica value) emerged from user-invited collaboration, not from Phase A/B questions. The skill assumes extraction; when the user arrives with rich conceptual work, the right mode is translation through collaborative refinement. Proposes a mode-recognition step between Phase A and Phase B.

## Domain project created (sibling repo, not framework changes)

At `../nla-archetypes/`:

- Fresh git repo with framework as submodule at `packages/nla-framework/`, pinned to v0.0.8 (HEAD was already at the latest tag — no pin choice needed).
- Full NLA scaffold: 14 framework thin-wrapper skills + 1 domain skill (`/extract-archetype`); CLAUDE.md, README.md, overview.md with a "Where Things Live" structure record.
- Three values in `app/shared/values.md`: ground every claim in the text; resist demographic smoothing; true-like-fiction-not-like-a-transcript (Guernica anchor).
- Voice optimized for downstream NLA consumption (per `reference/standards/nla-writing.md`), not human reading.
- Custom directories beyond the framework default: `sources/` (gitignored portrait files), `archetypes/` (tracked output corpus). Recorded in the project's structure record.
- Lens system (multiple framings of the same subject) deliberately deferred — filename convention leaves room for `[subject]-[variant].md` later without restructuring.

## Debrief

Refined observations from this session's explicit `/debrief`:

- **The Guernica value emerged from invited collaboration, not Phase B Q&A.** Load-bearing observation, captured as the 2026-05-11 friction entry. `/create-app`'s structured-extraction mode underperforms when the user arrives with rich conceptual work; translation-through-collaborative-refinement should be a recognized mode within the skill, not an accident of the user's explicit invitation.

- **"Barebones" required real-time calibration the skill doesn't anchor.** The user said barebones; I still had to decide what scaffolding to skip (output-spec.md, lens system, multiple voice files) vs. what to add (the two custom directories). A retrospective calibration anchor would help: *the smallest project that runs the user's actual workflow once*. Not captured as a separate friction entry — could fold into the 2026-05-11 entry's `/maintain` pass, or surface fresh if it recurs.

- **AskUserQuestion friction (captured as 2026-05-10 entry).** Two rejections cost a turn each; the structured-tool default fired despite an existing memory note. Memory-only mitigation proved insufficient — argues for framework-level guidance that loads into every session.

- **Generation order worked smoothly — worth preserving.** The 7-step order (settings → mechanical files → shared context → task → integration → reference → config) avoided dependency issues where integration files (overview, CLAUDE.md) reference task docs that don't yet exist. Positive signal; no change recommended.

## State at Close

**Context for next time:**

- `nla-archetypes` is fully scaffolded at `../nla-archetypes/`. The initial commit there hasn't been made yet — that's a step inside the new project, not framework work.
- Framework HEAD remains at v0.0.8; no consumer-facing changes this session (the two friction entries are internal content per Shippability classification).
- The two new friction entries target overlapping files (`core/skills/create-app.md` primarily, `install/CLAUDE-intent.md` secondarily), so a future `/maintain` could address them together.

**Decisions awaiting implementation:**

- **2026-05-10 friction entry** — framework-level guidance about defaulting to prose for follow-up questions (vs. AskUserQuestion's structured affordance). Touch points: `install/CLAUDE-intent.md`, `core/skills/create-app.md`.
- **2026-05-11 friction entry** — `/create-app` mode-recognition step between Phase A and Phase B (extraction vs. collaborative refinement) + Conversation Edge Cases entry for "user arrives with rich conceptual work." Touch point: `core/skills/create-app.md`; possibly `install/CLAUDE-intent.md` for the broader mode-recognition posture.

**Where to pick up:**

- Process the two friction entries together in a `/maintain` session — both touch `core/skills/create-app.md` and they're conceptually adjacent (both about how the AI should hold the conversation in design-sensitive moments).
- For domain work: `cd ../nla-archetypes`, commit the initial scaffold, then `/startup` and try `/extract-archetype` with a real portrait in `sources/`. The first real extractions will surface what's next — likely the lens system, or refinements to the voice and patterns docs.
