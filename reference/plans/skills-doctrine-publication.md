# Plan: Skills Convention Publication

**Drafted:** 2026-05-06 (warm-context, drafted in the same session as
the framework-side adoption work)
**Drafted for:** A future maintenance session
**Status:** Cold-context review complete (findings appended below);
awaiting framework-side adoption (Commit A, this session) and one
or more verification sessions before execution

---

## What this is

This plan publishes a refinement to the framework's skill-invocation
convention. The original convention (`disable-model-invocation: true` on
all skills) was adopted 2026-02-18 to prevent spontaneous invocation by
removing skills from the AI's active prompt. This plan refines that
convention: skills become model-invokable, but their descriptions carry
explicit invocation discipline ("AI: suggest as an option; only invoke
on user assent or explicit `/skill-name`"). A CLAUDE.md backstop rule
covers ambiguous cases.

This plan executes the consumer-facing publication: updating intent
files, adding an update-notes entry, updating the design-rationale to
record the refinement, generating the convention into new projects,
and tagging a release. The framework's own house adoption (the prior
arc that motivates this publication) happens in the session that drafts
this plan, not at execution time.

This is a plan, not a runbook. Each step expects human input. The AI
executing this plan should surface options at decision points and pause
for human direction rather than proceeding mechanically. Per the
framework's cardinal rule, the human decides.

The maintainer is the active session-manager. The AI's role is to
surface options, execute decisions, and capture context — not to manage
the session unilaterally.

## What this refines

The framework's design rationale (lines 711–742, "Skill Invocation:
disable-model-invocation on All Skills") documents the original
convention and the reasoning behind it. The original concern: invitation-
style description language (e.g., "Run periodically," "Best used at end
of sessions") in the active prompt invites spontaneous AI invocation.
The original solution: remove all skills from the active prompt via the
flag.

The new convention addresses the same concern via a different
mechanism. Empirical validation (from the session that drafts this plan)
showed that descriptions carrying *constraint-bearing* language —
"AI: suggest, do not invoke without explicit user assent" — discipline
invocation behavior in cold-context tests. The constraint language
counters the active-prompt nudge that the original convention removed
structurally.

The trade-off being made:

- **Original (structural):** Skills not in active prompt. AI must read
  CLAUDE.md's skills table to know skills exist. No invitation risk
  because nothing nudges. Cost: AI under-suggests skills it should
  surface (e.g., `/debrief` rarely fires at task transitions because
  CLAUDE.md's compressed table doesn't trigger as a behavioral cue).
- **Refinement (behavioral):** Skills in active prompt. AI sees skill
  descriptions as part of its toolkit. Constraint-bearing description
  language disciplines invocation behavior. Trade-off: relies on
  description prose to prevent the failure mode the original convention
  prevented structurally.

This is a real architectural shift, not a cosmetic convention update.
The plan acknowledges this explicitly. Step 5 below updates the
design-rationale entry to record the refinement, the new evidence, and
the residual concerns.

The refinement does not invalidate the original concern. Skills with
external action (e.g., `/write-letter` posting GitHub Issues) and skills
the original convention specifically discussed warrant especially
careful constraint language; a tier may emerge here at execution time
or post-rollout.

## Why this exists

The validation work that grounds this plan was captured in the session
log produced at the close of the drafting session
(`reference/sessions/2026-05-06-skills-awareness.md` or similar — the
exact filename will be set at session close). That session demonstrated:

- Per-description constraints reliably produce suggest-vs-invoke
  behavior in cold-context tests
- A CLAUDE.md backstop rule helps with ambiguous cases but cannot
  override a clear description trigger
- The pattern `[what] + Relevant when [trigger] + [why] + AI:
  [discipline]` produces well-calibrated agent behavior

The framework's own wrappers were migrated to this pattern in the
drafting session as the first adopter. By execution time, the
convention will have been exercised in at least one substantive
maintenance session (per pre-requisite #1 below).

Issue #24 (a feedback letter from facebook-moderation about handoff
discipline) is referenced as substrate for the *plan's structure* — the
four-section template (substance + procedural-edge + judgment-defaults
+ confidence band). The letter's *recommendations* about framework-wide
changes are NOT implemented by this plan; they are deliberately
deferred for separate triage. See "What this plan deliberately defers"
below.

## Pre-requisites for execution

Before starting, verify all the following. If any pre-requisite is
unmet, surface it to the maintainer and pause.

1. **Framework wrappers have been migrated to the new pattern.** Verify:
   pick three framework wrappers (e.g., `/debrief`, `/maintain`,
   `/friction-log`) and check their frontmatter. They should not carry
   `disable-model-invocation: true`, and their descriptions should
   follow the `[what + relevant when + why + AI: discipline]` pattern.
   If any sampled wrapper still has the old shape, the framework-side
   adoption work didn't land — defer publication.

2. **Convention has been used in at least one substantive maintenance
   session.** Specifically: a session of meaningful length where the
   AI's suggest-vs-invoke behavior could be observed. Check the most
   recent session log for any notes about whether skills were suggested
   at appropriate moments and whether any auto-invocation occurred.

3. **No regressions surfaced.** Read recent friction-log entries since
   the framework-side adoption. If any flag the AI auto-invoking
   inappropriately, regressing on user-decides framing, or breaking
   prior workflows, address those before publishing.

4. **Latest tag is known.** Run `git tag --sort=-creatordate | head -3`
   to confirm starting point.

5. **No uncommitted changes that aren't part of this publication arc.**
   If there are, decide: commit now, stash, or include in this arc.

## Goals (and non-goals)

**Goals:**

- Domain projects can adopt the new convention via `/update` (or via
  manual migration following update-notes guidance)
- `install/skills-intent.md` reference content reflects the new pattern
- New domain projects from `/create-app` start with the new convention
- The CLAUDE.md backstop rule is generated for new projects by default
- The design-rationale entry is updated to record the refinement, the
  new evidence, and the trade-off being made
- A tagged release marks the publication

**Non-goals (deferred):**

- Implementing a `/handoff` skill (Issue #24 recommendation E)
- Auditing other framework skills for runbook framing (Issue #24
  recommendation C)
- Documenting session-bracketing workflow shape in foundations (Issue
  #24 recommendation F)
- Extending verify-don't-trust to agent self-reports across the
  framework (Issue #24 recommendation D)
- Formalizing the four-section handoff template as framework-wide
  guidance (Issue #24 recommendation B; this plan *uses* the template
  but doesn't document it as universal guidance)
- `/close` integration of plan-shape detection (Issue #24
  recommendation A)
- Triage of Issue #24 itself

The drafting session consumed Issue #24's findings about handoff
*structure* (used to draft this plan) but did not perform formal
triage of the issue. Triage will happen in a separate session before
or alongside this publication. This is a deliberate sequencing
decision — drafting the plan with the letter's findings was time-
sensitive (warm-context capture); formal triage of the broader
recommendations is not.

## Substance — the steps

### Step 1: Update `install/skills-intent.md`

**Intent.** Become the canonical source for the new wrapper pattern.
Domain projects' `/update` proposals reference this file's structure
to suggest migrations.

**Actions.**

1. Read `install/skills-intent.md` end-to-end to understand current
   structure. Note: this file contains both a top-level reference
   wrapper *template* AND per-skill example wrappers (one per framework
   skill). Both need updating to stay internally consistent.
2. Update the top-level reference wrapper template:
   - Remove `disable-model-invocation: true` from frontmatter (defaults
     to false / model-invokable).
   - Replace the description with the new pattern.
3. Update each per-skill example wrapper to match the pattern. For each:
   - Read the corresponding core skill file to understand the skill's
     purpose and natural triggers.
   - Audit the core skill body for invitation-style language (see "On
     auditing for invitation-style language" below) — this happens
     during distillation; it shapes the description we write.
   - Write a description following `[what] + Relevant when [trigger] +
     [why] + AI: [discipline]`.
4. Add prose to the document explaining:
   - The suggest-vs-invoke convention
   - Why descriptions carry constraint language
   - The relationship to the design-rationale entry being refined
   - Reference to the audit guidance (see Step 4 / update-notes)

**On auditing for invitation-style language.** When distilling each
skill's description, the audit isn't a checklist of forbidden phrases.
The intent: the active prompt biases the AI's reasoning about what to
do next. Anything in a description that reads as direction-toward-
action ("run this," "use periodically") rather than relevance-signal
("relevant when X happens, available as an option") risks the
spontaneous-invocation failure mode the original convention prevented.

Use judgment. Different skills have different natural language — an
action tool reads differently than a phase skill. What you're
protecting is the user's authority over when the AI acts. If a skill's
existing body language reads as inviting the AI to fire on its own
rhythm, the distillation should reframe it; if the body's language
itself is load-bearing for that pattern (e.g., the skill genuinely is
about a periodic capture rhythm), flag it and decide whether to revise
the body too.

Two anchor examples (not exhaustive):
- "Run this periodically" → directive toward the AI; reframe
- "Relevant when the maintainer notices something worth recording" →
  relevance signal with user-as-actor; keep

**Verification.** Reference template and all per-skill examples follow
the new pattern. No remaining `disable-model-invocation: true` flags.
No invitation-style language in descriptions.

### Step 2: Check `install/structure-intent.md`

**Intent.** Sync if the file mentions skill-invocation conventions; do
nothing if it doesn't.

**Actions.**

1. Read `install/structure-intent.md` looking for any references to
   skill loading, invocation, or model-invocation conventions.
2. If found: update guidance to align with the new convention.
3. If absent: skip this step. Don't manufacture content.

**Verification.** Search confirms no stale references after edit (if
any edit was made).

### Step 3: Update `install/CLAUDE-intent.md` for backstop rule

**Intent.** New domain projects generated via `/create-app` should
include the CLAUDE.md backstop rule by default. Existing projects
acquire it via the update-notes entry (Step 4).

**Actions.**

1. Read `install/CLAUDE-intent.md` end-to-end. This file describes the
   intended structure of generated CLAUDE.md files; it doesn't carry
   literal text destined for those files.
2. Identify where prescriptive guidance about generated CLAUDE.md
   "Available Skills" section lives — likely in the Reference Structure
   section. The backstop rule belongs as part of this prescription, so
   that `/create-app`'s synthesizer renders it into new projects.
3. Add prescription language for a backstop rule. Sample text:

   > Generated CLAUDE.md should include a section near "Available
   > Skills" instructing the AI: when project skills appear in the tool
   > listing, prefer suggesting them conversationally over invoking
   > directly; only invoke on explicit user assent or `/skill-name`;
   > when uncertain, ask before invoking.

   The exact wording is a drafter judgment call — what matters is that
   `/create-app` generates a CLAUDE.md with the rule.
4. Verify generation behavior: read `.claude/skills/create-app/SKILL.md`
   to confirm it instructs the synthesizer to include CLAUDE-intent's
   Available Skills prescription faithfully. If `create-app` has its
   own CLAUDE.md generation logic that bypasses CLAUDE-intent, sync
   that too.

**Verification.** A sample generation (read the create-app
instructions) confirms the rule would land in new project CLAUDE.mds.

### Step 4: Add update-notes entry

**Intent.** Tell domain projects what changed, why, and how to migrate.
This is the consumer-facing change-log entry that runs through
`/update`.

**Actions.**

1. Read `install/update-notes.md` to confirm entry format.
2. Draft the entry. Include:
   - **Title:** Skill awareness convention — wrappers become
     model-invokable
   - **Affects:** `install/skills-intent.md`,
     `install/CLAUDE-intent.md`, `reference/design-rationale.md`,
     downstream domain wrappers
   - **What changed:** Convention shift on wrappers (toggle flip,
     description pattern, CLAUDE.md backstop rule). Reference the
     design-rationale entry to indicate this is a refinement, not a
     bug fix.
   - **Why:** Empirical validation showed descriptions can discipline
     invocation when constraint-bearing. Original concern (spontaneous
     invocation) is still addressed, via different mechanism.
   - **How to migrate:** Specific per-wrapper steps for domain
     maintainers, including the same audit guidance from Step 1's
     "On auditing for invitation-style language."
   - **Migration scope:** Optional. Existing projects continue to work
     with the old convention; the new convention is for projects that
     want richer AI awareness of their skills.
   - **Risk acknowledgement:** For skills with external action
     (e.g., `/write-letter`, `/check-feedback`), constraint language
     warrants extra care; the original convention specifically called
     these out.

**Verification.** Entry follows the file's format conventions. Migration
steps are concrete enough that a domain maintainer can execute without
further questions. The audit guidance is intent-based, not a checklist.

### Step 5: Update `reference/design-rationale.md`

**Intent.** Record the refinement in the design-rationale entry it
modifies. The framework's pattern for changes like this is the inline
"Superseded" or "Refined" marker (see line 707 for an example).

**Actions.**

1. Read the existing entry at lines 711–742.
2. Add an inline marker noting the refinement. Format follows the
   line 707 example:

   > **Refined 2026-MM-DD.** [One-paragraph summary: descriptions can
   > carry constraint-bearing language that disciplines invocation;
   > validation evidence from session log [path]; trade-off summary;
   > residual concerns about external-action skills.] See "Skill
   > Awareness Convention Refinement" below.

3. Add a new entry at the end of the file (or near the original) with
   the full refinement reasoning:
   - What the refinement is
   - Empirical evidence (link to validation session log)
   - The architectural shift from structural to behavioral discipline
   - The trade-off being made
   - Residual concerns (external-action skills, multi-skill ecosystem
     interactions, post-rollout calibration)
   - What's still true from the original convention (the concern was
     real; the original mechanism worked)

**Verification.** Both entries are internally consistent. A reader
arriving at the original entry sees the refinement marker and is
directed to the new entry. A reader arriving at the new entry
understands its relationship to the original.

### Step 6: Run `/validate`

**Intent.** Verify internal consistency before tagging.

**Actions.**

1. Run `/validate` structural mode. Address findings.
2. Run `/validate standards` against the modified files. Doc-type
   classification:
   - `install/skills-intent.md`, `install/CLAUDE-intent.md`,
     `install/update-notes.md`: operative docs (Section 8.3) — they
     instruct `/create-app`, `/install`, `/update` what to synthesize
     or describe. Run with sections 2 + 8.3.
   - `reference/design-rationale.md`: design doc (Section 8.4). Run
     with sections 2 + 8.4.
   - Scope: just the modified files; no need to re-validate the whole
     framework.
3. Address findings before proceeding to tagging.

**Verification.** Validate runs clean (or surfaces only findings the
maintainer accepts as deferred).

### Step 7: Tag and push

**Intent.** Mark the consumer-facing arc as a release.

**Actions.**

1. Determine the version bump. Two questions to resolve:
   - **What's the bump from?** Latest tag is v0.0.6 (or whatever
     `git tag --sort=-creatordate | head -1` returns at execution time).
   - **Are there unreleased consumer-facing commits between v0.0.6 and
     this publication?** Check `git log --oneline v0.0.6..HEAD`. Per
     the framework's shippability convention, prior consumer-facing
     work should have been tagged at session-end. If there are
     unreleased consumer-facing commits, those should ideally have
     been tagged separately. Two paths:
     - **Tag this publication as v0.0.7 covering everything since
       v0.0.6.** Update-notes entry should mention bundled changes.
     - **Tag prior consumer-facing work first as v0.0.7, then this
       publication as v0.0.8.** Cleaner separation but more bookkeeping.
   - The maintainer decides which path. Surface both with a
     recommendation.
2. Verify all commits in the publication arc are on `main` and pushed.
3. Create the tag: `git tag vX.Y.Z` at the latest commit on main.
4. Push the tag: `git push origin vX.Y.Z`.

**Verification.**

- Tag is visible on origin
- Tag points at the expected commit
- Update-notes entry's wording matches what the tag covers

### Step 8: Close the loop on Issue #24

**Intent.** Per penny-post conventions, post a follow-up comment on the
source issue summarizing what was implemented.

**Actions.**

1. Compose a comment that:
   - Names what was published (the skill awareness convention
     refinement)
   - Acknowledges the issue's structural contribution to the plan
     (drafted using the four-section handoff template described in
     items 3-5)
   - Notes that the awareness work is partially aligned with the
     letter's broader theme but is not a direct address of any single
     lettered recommendation A-F
   - Lists what's deliberately deferred for separate triage (the
     non-goals list)
2. Post via `gh issue comment 24 --repo mightytech/nla-framework`.
3. Do NOT close the issue. Full triage is a separate session.

**Verification.** Comment visible on Issue #24.

## Procedural edge-cases

### What if pre-requisites are unmet?

Surface to the maintainer with specifics about which pre-requisite
failed. Default: defer publication. Don't proceed without explicit
acknowledgment of unmet pre-requisites.

### What if `/validate` surfaces structural inconsistencies?

Address findings before tagging. If findings can't be resolved in this
session, don't tag — defer publication. Common cases:
- **Missed file:** update it now.
- **Inconsistent wording:** sync to the latest pattern.
- **Cross-reference broken:** fix the reference; if the referenced
  thing doesn't exist, decide whether to create it or remove the
  reference.

### What if the version-bump path is unclear?

Surface both paths from Step 7.1 with the implications and let the
maintainer decide. Don't choose unilaterally.

### What if `install/structure-intent.md` doesn't mention any skill-invocation conventions?

Step 2 result: skip. Don't manufacture content.

### What if `/create-app` generation logic has its own copy of CLAUDE.md skills section that needs syncing?

Possible. Step 3.4 includes verifying generation behavior. If
`create-app/SKILL.md` has its own logic that bypasses CLAUDE-intent,
treat that as part of Step 3 — the intent is "new projects get the
rule by default," and the implementation may need touching multiple
files.

### What if domain projects already have wrappers without `disable-model-invocation: true`?

Possible — domain projects may have ejected or manually customized
wrappers. The update-notes entry should be clear that the convention
applies where the project hasn't already diverged. Don't auto-migrate
diverged wrappers.

### What if a skill body's invitation-style language is load-bearing?

The audit during Step 1 may surface skills whose body language is
inviting the AI to fire on its own rhythm, and where that rhythm is
genuinely the skill's purpose. Don't automatically revise — surface
to the maintainer. May warrant extra-strong constraint language in
the description, or may warrant deferring the skill from this
publication, or may warrant an actual body revision. The maintainer
decides per-skill.

### What if `gh` CLI auth fails when posting the Issue #24 comment?

Step 8 may fail. The publication isn't blocked by this — it's a
courtesy. If posting fails, note it; the maintainer can post manually.

### What if the design-rationale update from Step 5 surfaces the original convention's reasoning we hadn't accounted for?

Possible — the entry was written with intent the cold drafter may not
fully recover. If reading it surfaces concerns the plan doesn't
address (e.g., the entry's specific worry about an external-action
skill), pause and surface. Don't bulldoze the existing rationale; the
refinement should integrate with it, not erase it.

## Judgment defaults

These are pre-decided answers to questions where the rule space is open
and the executor would otherwise improvise.

### Substance vs. brevity in the update-notes entry

**Lean: substance.** Domain maintainers will read this once when
migrating. Length is fine.

### Backstop rule in CLAUDE-intent vs. only in update-notes guidance

**Lean: both.** Add to CLAUDE-intent so new projects start with it;
existing projects pick up via update-notes guidance.

### Phased rollout vs. all-at-once for domain wrappers

**Lean: framework publishes once; domain maintainers choose pace.** The
intent file change applies the new pattern to all reference content.
Domain maintainers can choose to migrate skill-by-skill or all-at-once.

### Aggressive vs. conservative version bump

**Lean: conservative.** Patch increment (v0.0.X+1), not minor or major.
This is an additive convention refinement, not a breaking change.

### Tag scope (this arc only vs. covering prior unreleased work)

**Lean: surface to maintainer.** Don't pre-decide. The shippability
convention says session-end tagging; if prior sessions skipped tagging,
that's an inherited bookkeeping question the maintainer should resolve.

### Wait for multiple verification sessions or one

**Lean: one substantive session is enough.** Multiple = belt-and-
suspenders that costs more than the small risk it mitigates. Maintainer
can override.

### Specific wording for new descriptions vs. reference template only

**Lean: update both the reference template AND each per-skill example
wrapper in `skills-intent.md`.** Stale per-skill examples create
confusion for `/update`'s diff detection and for human readers.

### How to handle skills with external action (`/write-letter`,
`/check-feedback`)

**Lean: extra-strong constraint language in description, but include in
this publication.** Don't tier separately unless audit (Step 1) or
verification surfaces a specific failure. The original convention's
concern about these skills is real; the constraint language addresses
it; the rollout will reveal whether constraint language alone is
sufficient.

### When the design-rationale update conflicts with our publication framing

**Lean: trust the existing rationale's reasoning.** If the entry
surfaces a concern the plan doesn't address, that's a finding worth
honoring, not a hurdle to skip.

## Confidence band

Where the executor should expect to push back at the maintainer:

### Pre-requisite verification

Don't assume the framework-side adoption work was completed just
because time has passed. Sample wrapper frontmatter; check at least
one substantive maintenance session occurred since adoption.

### Update-notes wording

The maintainer should review the update-notes draft *before*
publication. Domain projects act on this entry. Wording matters. Don't
push past the maintainer's review.

### Design-rationale wording

Same — the maintainer should review the design-rationale entry before
publication. The refinement framing matters: this is a refinement of an
existing decision, not a contradiction. Get the framing right.

### Whether to extend scope mid-execution

If during execution the maintainer wants to add scope ("while we're at
it, let's also do X"), push back: extending scope mid-session
compromises the plan's coherence. Defer the new work to a separate
session.

### Cold-context review of *this plan* before execution

Two cold-context reviews of this plan happened in the drafting session
(findings appended below). If those findings haven't been addressed in
the plan as it stands at execution time, that's a signal the plan was
published before review was integrated. Flag to the maintainer.

### Tagging timing

Don't tag mid-execution. Tag only when all steps complete and validate
runs clean.

### Specific steps' framing

If a step seems to require mechanical pattern-matching, pause and check
whether the file state matches what the plan assumed. The artifact may
have evolved between drafting and execution.

### When auditing skill bodies, intent-based judgment is required

The audit isn't a checklist. If you find yourself just searching for
specific phrases, you're likely missing edge cases. Use judgment about
what reads as direction-toward-action vs. relevance-signal. Surface
borderline cases to the maintainer rather than deciding unilaterally.

## Open questions for the maintainer

1. **Does `/update` actually auto-propose the wrapper changes in domain
   projects?** Verify by reading `core/skills/update.md`. If `/update`
   doesn't propagate wrapper-level edits (the plan's working assumption
   may be wrong), the update-notes entry must include manual migration
   steps as primary. If it does, the entry can lean on `/update`'s
   behavior.

2. **Should publication wait for verification across multiple
   sessions?** Default is one (per judgment default above). Maintainer
   may want more conservative verification.

3. **Should we triage Issue #24 before or as part of this publication
   session?** The drafting session deferred triage. The maintainer may
   want triage to happen first (so the broader recommendations are
   processed alongside the convention publication) or separately
   (clean separation of concerns).

4. **What scope does the v0.0.7 (or v0.0.8) tag cover?** Per Step 7.1,
   two paths exist. The maintainer's call.

5. **Are there skills where the audit surfaces invitation-style body
   language that should be revised in addition to the description?**
   Step 1's audit may surface these. Each is a per-skill maintainer
   judgment call.

## Verification (whole-plan)

How to know the publication worked:

- Domain project running `/update` after the publication tag sees the
  convention shift and can adopt it (test in at least one domain
  project if available)
- New domain project from `/create-app` starts with the new pattern
  and the CLAUDE.md backstop rule
- `reference/design-rationale.md` carries the refinement marker on the
  original entry and a new entry recording the refinement
- Issue #24 has a follow-up comment summarizing what was published
- Tag is visible on origin
- No regressions in subsequent maintenance sessions

## What this plan deliberately defers

Per Issue #24's other recommendations (each warrants its own session
and feedback triage):

- **Recommendation A:** `/close` detects plan-shaped artifacts, offers
  simulation
- **Recommendation B:** Document four-section handoff template formally
- **Recommendation C:** Audit framework skills for runbook framing
- **Recommendation D:** Extend verify-don't-trust to agent self-reports
- **Recommendation E:** `/handoff` skill or fold into `/close`
- **Recommendation F:** Document session-bracketing workflow shape in
  foundations

Triage of Issue #24 itself is also deferred. This plan consumes the
letter's findings about handoff structure but doesn't dispose of the
issue.

---

## Cold-context review findings

*Two cold-context reviews ran in the drafting session: a simulation
pass (Pass 1) and a conceptual-frame pass (Pass 2). Findings below were
synthesized from both, with notes on which were patched into this plan
and which remain as caveats for the executor.*

*Reviewer notes for execution-session AI: when reading this plan to
execute it, the findings below show what the plan was missing during
drafting and how it was patched. Some findings are inherently
unpatchable (state mismatches between drafting time and execution time
that can only be resolved by execution-time verification). Where you
see "verify at execution," that's a finding patched into a verification
step rather than into pre-decided content.*

### Pass 1: Simulation review

The simulation pass identified specification gaps and state
mismatches. Synthesized findings:

- **Validation session log doesn't exist on disk at drafting time** →
  Patched: prose updated to clarify the session log will exist by
  execution time (created at this drafting session's close); pre-
  requisite #1 verifies this.
- **Framework wrappers haven't been migrated** → Patched: pre-requisite
  #1 explicitly verifies this with a sampling procedure. The drafting
  session migrates them (Commit A from this session).
- **Step 3 backstop rule location ambiguous** → Patched: Step 3.2-3.3
  now specifies "Reference Structure section" with sample text and a
  verification step.
- **Step 5 validate doc-type classification wrong** (originally said
  intent files are specs, Section 8.7) → Patched: Step 6 now
  classifies intent files as operative docs (8.3) and design-rationale
  as design doc (8.4).
- **Step 1 ambiguity about per-skill wrappers** → Patched: Step 1 now
  explicitly directs updating both the reference template AND each
  per-skill example. Judgment default reinforces.
- **Tag arithmetic conflicts with shippability convention given
  unreleased consumer-facing commits since v0.0.6** → Patched: Step 7
  surfaces both paths to the maintainer rather than pre-deciding.
- **Step 7 (now Step 8) comment template too vague** → Patched: Step
  8.1 now specifies the four items the comment should cover.
- **Recursive review reference loop** → Patched: confidence band entry
  on cold-context review specifies "flag to the maintainer; default-
  defer."
- **Pre-requisite #4 may false-flag drafts left from drafting session**
  → Pre-requisite #5 added to clarify expectations.

### Pass 2: Conceptual-frame review

The frame pass identified the most consequential gap: the plan
proposed reversing a documented design decision without acknowledging
it. Synthesized findings:

- **Design-rationale entry on `disable-model-invocation` exists and was
  never consulted during drafting** → Patched substantively: new "What
  this refines" section frames the relationship; new Step 5 updates
  the design-rationale entry; the plan no longer presents itself as
  publishing a "doctrine" without reference to existing reasoning.
- **Plan conflates structural discipline (toggle flag) with behavioral
  discipline (description prose)** → Patched: "What this refines"
  section now explicitly names the architectural shift and the
  trade-off being made.
- **Validation session and framework wrapper state were "fictional" at
  drafting time** → Same finding as Pass 1's first two; same patches.
- **Terminology drift (doctrine/convention/pattern)** → Patched:
  standardized to "convention" throughout. Title updated to "Skills
  Convention Publication."
- **Pre-triage consumption of Issue #24** → Patched: "Why this exists"
  and goals/non-goals now explicitly note that the letter's findings
  about plan structure are consumed (warm-context capture); broader
  recommendations are deferred for triage; this is a deliberate
  sequencing decision, not an oversight.
- **Intent files classified as specs (8.7) when they're operative docs
  (8.3)** → Same finding as Pass 1 #4; same patch.
- **`/update` propagation behavior assumed without verification** →
  Open question #1 surfaced as the load-bearing one; the answer
  affects whether the update-notes entry's "how to migrate" section
  leans on automated propagation or specifies manual steps as
  primary.
- **External-action skill concerns (`/write-letter`, `/check-feedback`)
  not specifically addressed** → Patched: "What this refines" section
  notes these warrant especially careful constraint language;
  judgment default for handling these added; design-rationale update
  (Step 5) preserves the original concern.

### What both passes worked well to surface (process reflection)

Both reviewers noted:
- The four-section template (substance + procedural-edge + judgment-
  defaults + confidence band) is structurally well-shaped and pays
  off; reviewers found their concerns pre-addressed in several places.
- Goals/Non-goals up front prevented scope creep at review time.
- Open questions surfaced rather than pre-decided was helpful — Pass
  2's question #1 about `/update` was exactly the right load-bearing
  question.
- Pre-requisites with explicit verification steps was useful.

Pass 1 noted: **the plan should distinguish between "specified-by-
reference" (legitimate) and "specified-by-handwave" (illegitimate).**
This patch round tightened several handwaves into either concrete
specifications or explicit verification steps.

Pass 2 noted: **the plan's polish made the frame easier to accept
uncritically. The diagnostic move that exposed the frame issue was
checking whether the cited substrate actually existed.** A pre-flight
"verify cited artifacts exist" check is worth adopting as a drafting
discipline going forward — friction-log territory at session close.

Both passes' debrief-style reflections converge on a single
suggestion: **drafters should self-ask "what design-rationale entry
would a skeptical reader cite to refuse this plan?" before publishing
the plan for review.** If the answer is non-empty and the plan
doesn't address it, frame work isn't done.

---

*This plan was drafted from warm context, reviewed by two parallel
cold-context agents, and revised to incorporate findings. The plan
is now ready for execution pending pre-requisite verification.*
