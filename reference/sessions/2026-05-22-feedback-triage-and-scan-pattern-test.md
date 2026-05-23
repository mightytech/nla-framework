# Maintenance Session: Feedback Triage + Scan-Pattern Test

**Date:** 2026-05-22
**Status:** Complete

## Intent

Triage two new GitHub Issues from facebook-moderation (the framework's most active feedback source over the past ~4 days):

- **Issue #27** (2026-05-22) — Reliability vs determinism as load-bearing distinction for NLA design
- **Issue #26** (2026-05-20, with 2026-05-21 recurrence comment) — Mechanics-without-spirit failure pattern + candidate `/scan-pattern` skill

Secondary intent: during triage, the framework maintainer asked the meta-question on Issue #26 Item 2: would the proposed `/scan-pattern` technique have been useful in *this framework's own history*? We tested it as a one-off cold-context scan against the framework's own corpus during triage. The test was a real-time instance of the technique it was evaluating.

## Changes Made

- **`reference/feedback-log.md`** — added three new pending entries (newest first):
  - 2026-05-22 — Reliability vs determinism (Accept-with-/think)
  - 2026-05-22 — Mechanics-without-spirit framing-transfer fix (Accept-with-/think)
  - 2026-05-22 — Scan-pattern technique (Accept-with-/think, bundled with memory-mining beat)
- **`reference/feedback-log.md`** — added `**Bundled with:**` cross-reference line to the existing 2026-05-18 memory-mining entry, pointing at the new scan-pattern entry. The /think session is shared.
- **GitHub Issue #27** — triage comment posted, issue closed.
- **GitHub Issue #26** — triage comment posted (covering both items + 2026-05-21 recurrence comment), issue closed.

## Decisions Made

- **All three items accepted, all three with /think prerequisite.** The verdicts converge on the same shape because each item has a sound principle but a non-trivial design step before implementation can be specified. This is the "Accept-with-/think" verdict shape (per the 2026-05-20 friction-log entry on verdict prominence).
- **#27's /think is about placement and channel,** not whether to add the framing. The letter mis-located the existing aphorism (it's in `install/CLAUDE-intent.md` + framework `CLAUDE.md`, not `core/nla-foundations.md`). So the design question is multi-channel coverage and placement-within-foundations, not "expand the existing line."
- **#26 Item 1's /think is about response shape,** not whether the failure pattern is real. The diagnosis has implications beyond the recommended fix; multiple valid responses exist (writing-standards section, /validate mode, conditional→unconditional refactors, /maintain posture preamble). The /think folds in the adjacent 2026-04-16 Fallingwater-preamble friction entry.
- **#26 Item 2 verdict shifted from Defer to Accept-with-/think after the framework-side scan.** Initial verdict was Defer (N=1). The maintainer asked whether the technique would have been useful in framework history; we ran it as a one-off. The scan produced 4 clean misses, 4 counter-evidence cases, and a 7-capture map. Evidence picture shifted from N=1 to N≥2.
- **#26 Item 2 bundled with the pending 2026-05-18 memory-mining beat for a shared /think.** The scan surfaced a structural adjacency that wouldn't have been visible warm-context: both items are about "consult the corpus proactively at decision-time." Running two separate /think sessions would risk producing two adjacent features that should have been one.

## What Didn't Work

Nothing that didn't work, but one observation worth recording (see Debrief #2 below): the framework's existing skill-listing convention ("Defer / Accept / Adapt / Decline" as primary verdicts with "Accept-with-prerequisite" as a parenthetical) influenced my initial verdict on #26 Item 2. I proposed Defer first; only after the scan changed the evidence picture did I revise. The 2026-05-20 friction-log entry on verdict prominence anticipates this exact drift.

## Friction Log Entries Processed

None directly. The 2026-05-20 entry on Accept-with-/think verdict prominence is adjacent (this session is more evidence the verdict needs more visible placement in check-feedback Step 4), but I didn't apply the fix this session — it can ride along with the next penny-post-side maintenance work.

## Debrief

(To be captured at session close via `/close`, or as brief observations here if no explicit debrief happens.)

**Brief observations from execution:**

1. **The scan worked as advertised.** The technique surfaced findings I wouldn't have produced warm-context alone — particularly the 7-capture map and the structural adjacency between scan-pattern and memory-mining. The meta-recursive test (running the technique on the question of whether the technique would have been useful) produced clean directional evidence for the verdict shift, and the same run generated framework-side support for the mechanics-without-spirit pattern's generality.

2. **My initial verdict reflected the four-primary-verdicts pull the 2026-05-20 entry anticipates.** I proposed Defer on Item 2 first, with "we could adapt" as a parenthetical alternative. The scan-induced revision wasn't a verdict-shape issue (Accept-with-/think was always available); it was a confidence-on-the-evidence issue. But the parenthetical-alternative shape of my initial framing tracks the same drift the friction log names. Worth noting.

3. **Trust-but-verify on subagent output landed cleanly.** I spot-checked two of the agent's four clean candidates (Candidate 1's 2026-05-07 session log quote, Candidate 4's 2026-05-06 friction archive entry). Both citations were accurate. This was N=2 verification for ~50% of the load-bearing claims — adequate for this stakes level. If implementing from the scan output directly, more verification would be warranted.

4. **The framework's feedback intake from facebook-moderation is dense.** Three letters in ~4 days (Issue #25 on 2026-05-18 triaged previous session; #26 on 2026-05-20; #27 today). All Accept-with-/think. All touching foundational consumer-facing prose or skill design. The framework should be deliberate about not over-anchoring on one source's perspective — the letters' arguments stand on their own merits, but the source concentration is worth noticing.

## State at Close

**What's working:**

- Three new pending feedback log items recorded. Cross-reference between scan-pattern and memory-mining captured. Two GitHub issues closed with triage summaries. Session log written.
- The framework now has framework-side evidence for the scan-pattern technique's utility (4 clean misses in own corpus) and for the mechanics-without-spirit pattern's generality (the 7-capture map shows the awareness-keeps-being-captured-but-gap-persists pattern that #26 Item 1 names).
- One /think session now covers two pending items (scan-pattern + memory-mining), which is more efficient than processing them separately.

**What's pending:**

The feedback log now has **5 pending Accept-with-/think items**:

- 2026-05-22 — Reliability vs determinism (Issue #27)
- 2026-05-22 — Mechanics-without-spirit framing-transfer fix (Issue #26 Item 1)
- 2026-05-22 — Scan-pattern technique (Issue #26 Item 2) — bundled with memory-mining /think
- 2026-05-18 — /close enhancement: plan-shaped artifact detection + handoff integration
- 2026-05-18 — Memory-mining beat in lifecycle — bundled with scan-pattern /think

That's 4 distinct /think sessions queued (since two items share a session). Each /think session can be picked up independently. Recommended ordering by leverage:

1. **#26 Item 1 (mechanics-without-spirit)** — highest leverage; targets writing standards which are upstream of all future framework prose. Folds in 2026-04-16 Fallingwater-preamble friction entry.
2. **Scan-pattern + memory-mining (shared /think)** — high leverage; touches the corpus-consultation problem at framework lifecycle level. Has the strongest just-collected evidence base.
3. **#27 (reliability vs determinism)** — medium leverage; sharpens existing foundational language. Smaller blast radius than #26 Item 1.
4. **2026-05-18 /close enhancement** — already in queue from last session; touches most-frequently-run skill but requires the most design care.

The friction log retains 7 pending entries (unchanged from session start; none processed this session). The 2026-05-20 Accept-with-/think verdict prominence entry remains pending and is implicitly relevant given that this session produced three more Accept-with-/think items in immediate succession.

**Commits this session:** None yet. Work is in a state where /close can wrap up commit + tag + push when invoked. Consumer-facing content touched: `reference/feedback-log.md` is internal (reference/), `reference/sessions/` is internal. No consumer-facing content changed — this commit is framework-internal only (no tag needed, no update-notes entry).

**Where to pick up:**

Any of the four /think sessions above. The mechanics-without-spirit /think has the strongest evidence-and-implications profile right now and is the natural next move if continuing in this work strand.

---

## Scan Output

This is the raw output from the cold-context pattern-scan subagent run during triage. Preserved here as evidence for the eventual scan-pattern + memory-mining /think session.

**Scan question:** "Are there moments in framework maintenance history where the maintainer (or AI) was working on something and would have benefited from a cross-corpus pattern scan that didn't happen?"

**Sources scanned:** `reference/sessions/*.md`, `friction-log.md` + archive, `feedback-log.md` + archive, `design-rationale.md`.

**Discipline:** err inclusive at candidate boundary; file:line cites + brief excerpt; counter-evidence as valuable as candidates; no synthesized conclusion.

### Clean candidates (4)

**Candidate 1: 2026-05-07 "validation-arc methodology" miscalibration — self-reported pattern-scan failure**

`reference/sessions/2026-05-07-structure-decisions-protocol.md` lines 261-274:

> "I miscalibrated initially ('wait until methodology matures') because I only had the framework's two reports in mind. User pointed at three more experiment reports in facebook-moderation... reading them satisfied the generalizability threshold easily. **The miscalibration was a real-time instance of the very memory entry I had just captured a few exchanges earlier** (`feedback_read_artifacts_before_think`) — description-level knowledge of sibling experiments, not artifact-level. The user's implicit test was 'will you apply the lesson?'; I didn't until pointed."

Strongest possible direct evidence. The AI captured a memory about reading sibling artifacts, then in the same session committed the exact failure that memory was about. A cold-context subagent doing a corpus scan for "experiment reports in sibling NLAs" would have surfaced the three facebook-moderation reports the AI hadn't loaded. Author explicitly names this as a missed pattern application.

**Candidate 2: 2026-04-17 standards-subfolder broadening — friction-log evidence sat unweighted**

`reference/sessions/2026-04-17-feedback-triage-and-shippability.md` lines 137-146:

> "**User pushback on framing twice produced broader-and-better outcomes.** My initial framings were too narrow in both cases... The friction log had signals I hadn't weighted properly (four 2026-04-16 entries anticipating multiple standards types) — the subfolder decision was there in the data; I just didn't connect it until pushback forced the re-read. Worth being more suspicious of my own 'start small' reflex."

Directly addresses the orchestrator's training example #1 (the 4-16 cluster). The four entries were already in the friction log; a precedent scan against "standards / standards types / Python / Fallingwater" would have surfaced them and the subfolder decision would have been native rather than corrected. Author explicitly names "friction log as design-signal, not just backlog" as the lesson. Also memorialized in MEMORY.md.

**Candidate 3: 2026-05-22 AskUserQuestion near-miss despite landed guidance**

`reference/sessions/2026-05-22-session-bracketing-rhythm-and-handoff-template.md` lines 135-140:

> "**AskUserQuestion reach was a near-miss.** The AI started to call AskUserQuestion for the framing/placement/naming bundle. User interrupted; AI reverted to prose. The relevant memory exists ('Prose over enum for decisions'); the reach happened anyway in the first multi-decision moment of the session. Worth noting for future sessions — the memory's pull weakens in flow."

Even after the 2026-05-11 CLAUDE.md placement of the prose-default principle landed (strongest possible "always in active prompt" channel), the AI still reached. A cold-context pattern scan at decision-prep time ("look for prior AskUserQuestion/enum issues") would have surfaced six prior corpus references — making the precedent overwhelming in a way passive prompt-loading evidently isn't.

**Candidate 4: 2026-05-06 /think rediscovered findings already in Issue #24**

`reference/friction-log-archive.md` lines 766-792:

> "This session ran /think on the skill-invocation doctrine question and converged on several findings independently — only to discover that GitHub Issue #24 (a feedback letter from facebook-moderation) had captured most of those findings and several more. Reading the issue *after* /think meant the plan needed substantive rework to incorporate findings that were already documented."

Pre-existing self-aware capture of exactly the gap the scan-pattern technique would address. Resolution added a single sentence to /think's Prior Art section — minimal mechanism, leans on the AI to remember to do it.

### Borderline candidates (4)

- **B1: 2026-02-22 "Adding a New Skill" checklist not consulted during creation** (`friction-log-archive.md` 1168-1188) — checklist consultation failure, not precedent recognition. Including because failure mode rhymes.
- **B2: 2026-02-19 README directory-tree drift "keeps showing up"** (`friction-log-archive.md` 1545-1547) — recurrence noticed, but the fix is procedural (mirrors check in /close), not scan-driven.
- **B3: 2026-02-22 Voice/values bundled when conceptually distinct** (`friction-log-archive.md` 1317-1335) — conflation persisted whole framework history; no earlier facet-captures existed to scan for. Including for completeness; alternative framing is "this is exactly what scanning *would not* catch."
- **B4: 2026-05-08 single-commit-cross-reference "held up again"** (`reference/sessions/2026-05-08-close-reorder-and-tagging.md` 91-99) — recurrence caught and named in close debrief, but came at close not at decision-time. Pattern-scan at moment of designing the close-step shape might have folded the lesson in cleaner.

### Counter-evidence (4)

- **Counter 1: 2026-05-14 `reference/plans/` already exists** (`reference/sessions/2026-05-14-inquiry-flow-and-principle-2-recalibration.md` line 170) — structural-change discipline surfaced precedent at the right moment via `core/structure.md` consultation. Argues pattern-scan competes with always-loaded structural records; where the framework has built per-decision recording artifacts loaded at session start, it catches precedent natively.
- **Counter 2: 2026-04-15 packages/submodules /think** (lines 14-17) — most consequential design move in the corpus emerged from in-the-room lateral thinking during triage, not from a precedent scan.
- **Counter 3: 2026-05-22 session — design-rationale entry "modeled on Structure Decisions Protocol"** (lines 90-94) — AI located the right precedent and noted what neighboring rhythms had/didn't have, without a scan-pattern subagent. Corpus small enough for warm-context reasoning over design-rationale TOC.
- **Counter 4: 2026-04-17 friction-log read at session start surfaced four pending 4-16 entries naturally** (lines 70-74) — the 4-16 entries WERE loaded (per /maintain session-start friction-log scan); the failure was *weighing* them as design-signal, not surfacing them. Pattern-scan does *recall*; failure here was *judgment about loaded material*. Suggests scan-pattern may be solving the wrong layer for cases like this.

### Existing partial captures (7)

1. **/think's Prior Art section** (`core/skills/think.md` 72-85) — intent-shaped capture; warm-context judgment rather than dedicated subagent.
2. **/maintain Session Start surfacing** (`core/skills/maintain.md` 25-39) — counts and recent-session-log read; doesn't trace patterns across them. Open GitHub Issues not loaded.
3. **The Inquiry Flow rhythm** (`core/nla-foundations.md` 359-378) — hypothesis → verification → human-decides explicitly anticipates the warm-orchestrator/cold-verifier pattern.
4. **The Session-Bracketing Discipline's cold-context check mechanisms** — "Simulation catches execution stumbling blocks; question catches concept-layer conflations." A third mechanism — "scan catches missed-precedent" — would be a natural sibling.
5. **Pending feedback-log item: Memory-mining beat in lifecycle** — conceptual sibling, possibly bundlable. (This session does the bundling.)
6. **MEMORY.md "Friction log as design-signal, not just backlog"** (2026-04-17) — orchestrator-side discipline that scan-pattern's output-consumer role would systematize. Demonstrably doesn't always fire.
7. **feedback-memory "Read artifacts before /think"** (referenced as `feedback_read_artifacts_before_think.md`) — memory-level capture of precedent-scan principle. Captured 2026-05-06; demonstrably didn't prevent the 2026-05-07 lapse (Candidate 1).

### Agent's summary of signal

> "The signal pattern: the framework keeps re-noticing this gap, captures it in proportionally larger surfaces each time (memory → /think Prior Art → CLAUDE.md prose-default), and the gap keeps recurring even after capture. That's consistent either with 'the technique is right but invocation-discipline matters more than capture' or with 'the awareness-level captures are sufficient and the residual is irreducible.' Distinguishing those is the framework maintainer's call — both readings are defensible from this corpus."

This framing is the right input for the scan-pattern + memory-mining /think session.
