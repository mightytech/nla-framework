# Maintenance Session: Feedback Triage — Five Letters

**Date:** 2026-09-09
**Status:** Complete

## Intent

Triage five open GitHub Issues that accumulated over roughly three months while the prior two sessions worked from the friction log. Two intake sources, five letters:

- **Issue #28** (2026-05-23, nla-office-hours) — end-user update affordance + missing post-bulk-edit verification step
- **Issue #29** (2026-06-05, nla-claude-code) — `/update` phase order doesn't surface dormancy as the primary signal
- **Issue #30** (2026-06-05, nla-claude-code) — `/session-checkpoint` shipped with no update-notes entry
- **Issue #31** (2026-07-15, facebook-moderation) — foundations principle: understanding over deliverables
- **Issue #32** (2026-07-29, facebook-moderation) — AI "be-done" bias at review/verify/wrap gates

Nothing in the system changed behaviorally this session. The output is a triaged queue and one structural finding, and the finding is the more important half.

**The finding:** three independent sources are describing the same shape — the verify/close/deliberate step gets underweighted or skipped. More decisively, the framework has already shipped two mitigations in exactly this territory (`close.md` Step 3's anti-front-run language, 2026-05-23; the Session-Bracketing rhythm's plans-not-runbooks note, written preventively), and Issue #31 documents both being violated *after* they shipped. That reframes the response: "add a standing note where the framework handles gates" is approximately what was already done, twice, and it didn't fire. Whatever the cluster `/think` concludes, it has to answer why this class of guidance doesn't transfer — not place another instance of it.

The consequence for the queue: six accepted items sort into three `/think` bundles plus four small fixes, rather than six independent workstreams.

## Changes Made

Records only — no operative content was edited.

- **`reference/feedback-log.md`** — six new entries (below), plus a reciprocal `Bundled with` pointer added to the existing 2026-05-22 reliability-vs-determinism entry so the #31 pairing is visible from both sides. Pending count 4 → 10.
- **`reference/friction-log-archive.md`** — added a positive entry for Issue #29 item 1 (`/update` protocol holds under 3.5 months of dormancy). Filed directly to the archive rather than the active log: it is resolved-on-arrival with nothing to implement, and parking it in the active log would have left a resolved entry for the next session start to flag as pending archival. Active friction log unchanged at 8 pending / 2 deferred.
- **Issues #28–#32** — triage summary comments posted, all five closed.

### Verdicts

| Item | Verdict | Lands in |
|------|---------|----------|
| #31 understanding over deliverables | Accept-with-`/think`, bundled with #27 | `core/nla-foundations.md` (channel undecided) |
| #32 be-done bias at gates | Accept-with-`/think` — cluster primary | Multiple; shape deliberately open |
| #28 Item 2 bulk-edit verification | Accept | `core/skills/maintain.md` Bulk Edits |
| #29 items 2–3 dormancy signal | Accept, light shape only | `core/skills/update.md` Phase 1 |
| #30 update-notes backstop | Accept, three pieces in sequence | `install/update-notes.md`, `core/skills/README.md`, `update.md` Phase 2 |
| #28 Item 1 end-user update | Adapt | Docs + AI awareness; script optional |

## Decisions Made

- **Verify every checkable claim before writing a verdict.** Roughly ten minutes of grepping materially changed three of six verdicts (see What Didn't Work for what this caught). Chosen over triaging from the letters alone, which would have produced fluent verdicts that were wrong in specific ways.

- **#28 Item 1 adapted rather than accepted.** The letter's proposed script wraps `git submodule update --init --recursive`; `install/update-notes.md:755` documents the opposite convention (flat dependencies, not `--recursive`). Also reconsidered whether a script is the right shape at all — the gap is *awareness* ("bring this application up to date" → these two commands and the maintainer/end-user split), not the absence of a two-line wrapper. Docs-plus-awareness is cheaper, ships no code artifact, and avoids depending on the pending `lib/` Python-standards entry. Rejected: accepting the script as proposed, which would have committed the framework to contradicting its own documented convention.

- **#29 accepted at the light shape only.** Verification found that `update.md:76` already gates the early stop on local-vs-installed state, so the protocol wouldn't actually terminate wrongly on a dormant project — the defect is in the *reported* signal, not the control flow. That's a smaller bug than the letter's Phase 1 output suggests. Rejected: the medium reorder (`commits-since-install` check before fetching) and the heavier dormancy branch, both deferred with an explicit trigger — a second dormant-project update reporting the same friction. The submitter's own confidence note ("moderate, one data point") pointed the same direction.

- **#30 accepted in both halves, with the author-time fix landing more precisely than proposed.** The letter framed the gap as "author-time convention needed." The convention already has a home — `core/skills/README.md`'s "Adding a New Skill" checklist — and the update-notes step simply isn't among its seven. Separately, `maintain.md`'s Shippability rule already covers this case in general terms and didn't fire. An author-time convention that has demonstrably failed once is the argument for pairing it with the defensive backstop rather than choosing between them.

- **#31 split into two payloads, routed separately.** The principle goes to a foundations-language `/think` bundled with #27. The post-fix recurrence evidence goes to the gate/verification cluster, where it is the decisive input. Rejected: treating the letter as a single item, which would have buried the recurrence evidence inside a placement discussion where it does no work.

- **#29 item 1 recorded as positive evidence rather than discarded.** Nothing to implement, but the three mechanisms the submitter names (proposal-per-item cadence forcing re-justification, sequential dependency chain, commit-per-item rollback targets) are worth having when the update pipeline next comes up for design work.

- **Issue #33 deferred rather than triaged.** It arrived mid-session, after the discovery scan. Argument for triaging immediately: cluster context was loaded, and its Item 1 ("explanation-shaped text is retrievable; verified claims are not") may be a fourth capture of the same centroid theory. Argument for deferring, which won: it is a four-item letter with a demonstrated failure attached and deserves real attention, and the mis-landing risk is cheaply mitigated by recording the connection here. Appending it would have been momentum, not need.

- **Closing #31 despite its author framing it as a briefing for continuation.** Closing is the triage convention; the comment says so explicitly and commits to returning with questions rather than guessing at intent.

## What Didn't Work

- **Reading verdicts off the letters would have failed in three places.** Not a wrong turn taken, but the counterfactual is worth recording because it is the session's most transferable lesson. Without verification: #28 Item 1 would have been accepted with a `--recursive` script contradicting documented convention; #29 would have gotten the medium reorder on a defect that turned out to be narrower than reported; #30's fix would have been "add a convention" rather than "fill the empty slot in the existing checklist." Letters are *reports about* artifacts, so foundations principle #2 — the account is hypothesis, the artifacts are ground truth — applies to inbound feedback, not only to an AI's self-report.

## Feedback Log Entries Processed

Five issues triaged, six entries created, none resolved. Implementation is queued for later `/maintain` sessions; follow-up comments on the issues are owed when accepted items land.

## Friction Log Entries Processed

None resolved. One positive entry created and archived immediately (Issue #29 item 1).

## Debrief

Brief observations captured directly; no explicit `/debrief` conversation.

1. **Verification changed half the verdicts.** Detailed under What Didn't Work. The generalization worth carrying: the hypothesis-vs-evidence discipline the framework applies to AI self-accounts applies equally to inbound letters.

2. **The central finding was only visible across letters.** "Two mitigations shipped and then failed to fire" appears in none of the five submissions. Issue #31 knew it was quoting `close.md`; it could not know that line shipped ten weeks earlier in response to its own project's previous letter, as a fix for that exact failure. Assembling it required three letters plus repo history plus the 2026-05-23 session log. The uncomfortable corollary: triaging each letter promptly on arrival — the obviously correct hygiene — would likely have missed it. The lesson isn't "batch intake" (#28 sat over three months, which has its own costs, including a submitter waiting). It's that cross-letter reading is a distinct analytical move that should happen deliberately, even when triage is prompt.

3. **Lower confidence in the #31/#27 bundle than the entry's tone conveys.** The May scan-pattern/memory-mining precedent was fresh in the required reading, which made bundling *available* as a move. But those two items shared a mechanism (consult the corpus at decision-time); #31 and #27 share a shape (foundations-language item, placement open, maintainer judgment invited). "Optimize for reliability over determinism" and "understanding over deliverables" might be one principle seen from two sides or two unrelated principles that each need a placement decision. Cardinality is flagged as an open question inside the entry, which is the right hedge — but the `/think` session should not inherit false confidence from the framing.

4. **This session is weak evidence that the framework handles the be-done bias.** Asked whether it was safe to close, I reasoned to a stopping criterion rather than asserting done — but that was easy, having read #32 twenty minutes earlier. The disposition it describes operates precisely when the letter *isn't* in context. What happened here was an ambient mitigation, not a structural one, and shouldn't be counted as the pattern being managed. If anything it is a small data point for the cluster: the guidance works when freshly loaded, which is the same conditional that made Section 2.6 and the runbook note insufficient.

## State at Close

### Context for next time

- Feedback log at **10 pending** (4 existing + 6 new). Friction log unchanged at **8 pending / 2 deferred**.
- Intake channel is clear except **Issue #33** (see below). Issues #28–#32 closed with triage comments; follow-up comments are owed on each when accepted items are implemented.
- This session changed no operative content. Commits are `reference/`-only — internal by the Shippability rule, so no update-notes entry and no tag.

### Decisions awaiting implementation

Four small fixes, none blocking, none urgent:

- **#28 Item 2** — verification clause in `core/skills/maintain.md` Bulk Edits (drafted text in the letter). Genuinely standalone; the only one not part of a grouping.
- **#29** — one clarifying sentence in `core/skills/update.md` Phase 1.
- **#30 pieces 1–2** — backfill the `/session-checkpoint` update-note; add the missing update-notes step to `core/skills/README.md`'s "Adding a New Skill" checklist.
- **#30 piece 3** — skill-time backstop in `update.md` Phase 2. More machinery; sequenced after 1–2.

`#28 Item 1`, `#29`, and `#30` share the update-pipeline surface and are noted in their entries as plausibly one session's work. Implementing #29's one-line fix in isolation would fragment that grouping.

Also unrecorded and owed: the **third deferral trigger** from the 2026-05-23 debrief ("if future authoring shows *I knew about it but didn't apply it* instances, revisit the deferred `/maintain` posture preamble") was decided but never written into `reference/design-rationale.md`, which still lists only two. Issue #31 has now fired it. Recording it is a prerequisite step for the cluster `/think`, and is captured inside that feedback-log entry.

### Where to pick up

Three `/think` bundles, in rough priority order:

1. **Gate/verification cluster** — #32 primary, plus #31's recurrence evidence, #28 Item 3, the 2026-05-23 pre-emption-hazard friction entry (whose "second instance" trigger #31 satisfies), and the `/maintain` preamble reassessment. Must sequence against the pending #24 `/close` enhancement, since that item modifies `/close`'s step structure and one of #31's instances is a `/close` Step 3 failure. Constraint carried from the letter: the AI's tidy-rule fix *was the bias operating*, so "add a rule to the gate skills" is suspect as a response shape.
2. **Foundations language** — #31 principle + #27 reliability-vs-determinism. Open: one principle or two; which of three channels (`core/nla-foundations.md`, `install/CLAUDE-intent.md`, framework's own `CLAUDE.md`); how hard to state the contestable claims in a doc read across many fields. See debrief observation 3 on bundle confidence.
3. **Corpus consultation** — scan-pattern + memory-mining, unchanged from prior sessions.

**Issue #33** (2026-07-30, facebook-moderation) is open and untriaged: four items on the writing standards — the frame/persona distinction as load-bearing and unwritten, §1.2 as the same inversion, a proposed generator behind both, and a concrete gap in the author-time loading table with a demonstrated failure and cold-agent confirmation attached. Triage it **against the gate cluster, not standalone** — its Item 1 ("explanation-shaped text is retrievable; verified claims are not") looks like a fourth capture of the centroid theory running through #31 and #32.

Also still open from 2026-05-24: the **bare-scaffold fresh-context test**. If that run happened, its signal is worth capturing before it fades.
