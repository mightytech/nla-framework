# Framework Feedback Log

Accepted items from external feedback, waiting for implementation. Each entry captures
what was accepted, why, and where to find the full context.

The feedback log is the sibling of the friction log:
- **Friction log** — things *you* noticed while working
- **Feedback log** — things *others* noticed that you agreed with

Both feed into `/maintain`. Both are queues of actionable items.

---

## How to Use This Log

**When items are added:**
- After triaging feedback (via `/check-feedback` or any intake mechanism), accepted
  items are deposited here with their verdict rationale and a reference to the source.

**When items are resolved:**
- During `/maintain` sessions, the maintainer reviews pending items and implements them.
  Resolved entries are moved to `feedback-log-archive.md`.

**At session start:**
- `/maintain` checks this log alongside the friction log to surface what's waiting.

---

## Entry Format

```markdown
### [DATE] — [Brief description of the accepted item]

**Source:** [Link to GitHub Issue or intake item]
**Verdict:** [Accept / Adapt — and the reasoning]
**Status:** pending | in-progress | resolved

**What to do:**
[Concrete description of the change needed]

**Why it was accepted:**
[The rationale from triage — why this matters, what it improves]

**Resolved:** [DATE] — [brief description of what was changed and where]
```

Not every entry needs all fields. The essentials are: Source, What to do, Why it was
accepted, Status.

---

## Entries

*Entries are added chronologically, newest first.*

### 2026-04-17 — /install and /update initial-add path should check for tagged releases

**Source:** [Issue #23](https://github.com/mightytech/nla-framework/issues/23) item 1
**Verdict:** Accept
**Status:** pending

**What to do:**
The advance path in `core/skills/update.md` already checks for tagged releases between
current and HEAD and offers the user a choice between the tagged release (stable) and
HEAD (bleeding edge). Extend that same check to the initial-add path:

1. In `core/skills/install.md`, after `git submodule add`, run
   `git -C packages/[name] tag --sort=-creatordate | head -1`. If a tag exists and
   points at a commit other than current HEAD, offer the same stable/HEAD choice the
   advance path offers. Mirror `update.md:65`'s prompt wording for consistency.
2. In `core/skills/update.md`, apply the same check when a migration introduces new
   submodules (the initial-add flow inside `/update`, not only the advance flow).
3. Check `.claude/skills/create-app/` — if it runs `git submodule add` for framework
   during project creation, the same check should apply there too, so new projects
   pin at the framework's tagged release rather than HEAD.

**Why it was accepted:**
The principle (tagged release = stable default) is already in the framework; only the
initial-add path didn't inherit it. High confidence: this was caught during the
process-helpers maintainer's actual packages/ migration. Penny-post's HEAD was one
commit past v0.0.1 (a session-log update, not behavioral), so the project ended up
silently pinned at `main` rather than at the tagged release. Caught during pre-push
review — otherwise the mismatch would have drifted undetected. Small, well-scoped
change; same UX pattern applied to more entry points.

---

### 2026-04-17 — Document settings.local.json drift pattern in structure-intent

**Source:** [Issue #23](https://github.com/mightytech/nla-framework/issues/23) item 2
**Verdict:** Adapt — take only the lightweight doc note; defer the heavier options
**Status:** pending

**What to do:**
Add a short note in `install/structure-intent.md` (alongside or near the
`.claude/settings.local.json` guidance) describing the drift pattern: Claude Code
auto-approves-and-records new Bash patterns when a maintainer runs a tool the project
hasn't pre-declared (e.g., `python3 -m json.tool`). These entries accumulate silently
over time even in a fully-migrated packages/ project. This isn't framework behavior
and isn't a bug — but maintainers should know to recognize it and periodically prune
if the file grows, rather than mistake it for a framework-introduced problem.

Deferred from this item (not implementing now): a `/close` or `/maintain` drift nudge
comparing actual settings against a declared baseline, and a `/validate` mode doing
the same check. Both require more design work (what's the authoritative baseline?
what's the diff strategy?) and solve a problem that's now narrow after the packages/
migration closed out the big accumulation vectors (#6, #7, #12). Revisit if drift
actually accumulates meaningfully across a few projects, or if a third data point
comes in.

**Why it was accepted:**
The submitter explicitly flagged no strong recommendation and moderate confidence on
best mitigation. The positive signal — packages/ migration closed out the primary
permission-drift concerns — means this residual is genuinely narrow. A doc note meets
the submitter's primary ask (help maintainers recognize and not misattribute the
pattern) with minimal surface area. Heavier interventions can wait for more evidence.

---

### 2026-04-15 — Rewrite principle #4: intent over rules, with identity-description pattern

**Source:** [Issue #14](https://github.com/mightytech/nla-framework/issues/14), [Issue #17](https://github.com/mightytech/nla-framework/issues/17) item 1
**Verdict:** Accept (#14) + Adapt (#17.1 folded in)
**Status:** resolved

**What to do:**
Rewrite nla-foundations.md principle #4 (Judgment Over Rules). Lead with intent over rules
as the primary guidance: for judgment tasks, describe intent with rationale rather than
enumerating rules. Incorporate the identity-description pattern for classification/moderation
tasks ("describe the space, not the boundaries"). Add the boundary: rules are appropriate
only for pure preferences where consistency is the sole goal. Current "explain the why"
content stays as supporting material within the stronger framing.

**Why it was accepted:**
Empirically validated across three domains (moderation policy: 97% vs 93%, implementation
standards, quality evaluation). The strongest finding from the facebook-moderation project.
With public release approaching, this is the single most important thing newcomers need
to understand about writing NLA documents — the instinct to write precise rules produces
worse results than writing intent with rationale.

**Resolved:** 2026-04-15 — Rewrote principle #4 in nla-foundations.md as "Intent Over Rules" with identity-description pattern, examples, and rules-for-consistency boundary.

---

### 2026-04-15 — Promote session-checkpoint to core skill

**Source:** [Issue #17](https://github.com/mightytech/nla-framework/issues/17) item 2, plus facebook-moderation's `app/session-checkpoint.md`
**Verdict:** Accept — replaces the narrower "session splitting" proposal
**Status:** resolved

**What to do:**
Add `core/skills/session-checkpoint.md` adapted from facebook-moderation's version.
Add reference wrapper in `install/skills-intent.md`. Fold in the timing insight from
the compiler: "checkpoint before reasoning from files read long ago, not before producing
output from recent conversation." Drop the "experimental" status.

**Why it was accepted:**
Validated in practice. Addresses context thinning in long sessions — a universal problem
for persistent NLAs. The checkpoint skill was tested live during this triage session
and demonstrably improved quality of reasoning by refreshing key context.

**Resolved:** 2026-04-15 — Created `core/skills/session-checkpoint.md` adapted from facebook-moderation, with timing insight folded in. Added reference wrapper to `install/skills-intent.md`, framework wrapper to `.claude/skills/session-checkpoint/SKILL.md`, and entry to CLAUDE.md skills table.

---

### 2026-04-15 — Strengthen /think posture: frame-questioning and unexpected connections

**Source:** [Issue #17](https://github.com/mightytech/nla-framework/issues/17) item 3
**Verdict:** Accept — as /think skill enrichment, not general guidance
**Status:** resolved

**What to do:**
Add two posture bullets to `core/skills/think.md`: (1) "Question the frame" — before
converging, consider whether the problem as stated is the right problem; (2) "Bring
unexpected connections" — ideas from outside the immediate problem space, analogies,
other domains. These are aspirational — the AI may not achieve true lateral thinking,
but the aspiration produces better exploratory posture as a side effect.

**Why it was accepted:**
The AI's default is incremental thinking within the current frame. The packages/submodules
idea (this session) came from the human, not the AI — the AI was optimizing within the
permission model rather than questioning whether the model was the right approach.
Aspirational goals produce better side effects even when not fully achieved.

**Resolved:** 2026-04-15 — Added "Question the frame" and "Bring unexpected connections" posture bullets to core/skills/think.md.

---

### 2026-04-15 — Diagnostic step in the improvement loop

**Source:** [Issue #18](https://github.com/mightytech/nla-framework/issues/18) item 1
**Verdict:** Accept
**Status:** resolved

**What to do:**
Two changes. (1) Add a diagnostic beat to the improvement loop in nla-foundations.md
Working Rhythms: between "capture" and "fix," ask "why did this happen?" from the
artifacts, not from the AI's narrative. (2) Add to principle #2 (The Documentation Is
the Application): the AI's self-report and the actual artifacts can disagree — diagnose
from the artifacts, not the explanation.

**Why it was accepted:**
Empirical data: 6 of 19 diagnostic items traced to spec gaps, not actual bugs. 2 of 6
findings reclassified by diagnostic agent vs. orchestrator analysis. The AI's account of
what it did is a hypothesis, not evidence. The diagnostic step is low-cost (~80 seconds
per batch) and catches root causes that fixing alone misses.

**Resolved:** 2026-04-15 — Added diagnostic paragraph to principle #2 in nla-foundations.md and diagnostic beat to the improvement loop in Working Rhythms.

---

### 2026-04-15 — Strengthen friction log guidance: diagnosis as important as the fix

**Source:** [Issue #18](https://github.com/mightytech/nla-framework/issues/18) item 2
**Verdict:** Adapt — from "no-whisper extends to fixes" to friction log entry format guidance
**Status:** resolved

**What to do:**
Strengthen the friction log entry format guidance (in `reference/friction-log.md` and
`install/structure-intent.md`) to emphasize that recording *why* something went wrong
is as important as recording the fix. The "Confirmed reason" field exists but the
guidance should make clear that reasoning about root cause belongs in a persistent
document, not in ephemeral conversation.

**Why it was accepted:**
The no-whisper principle (answers go in docs, not conversation) extends naturally to
diagnosis. A whispered fix (edit directly, tell the AI "you missed this") produces a
working artifact but doesn't improve the inputs. The same gap will reappear.

**Resolved:** 2026-04-15 — Strengthened "Confirmed reason" field guidance in reference/friction-log.md entry format to emphasize diagnosis from artifacts and recording root cause.

---

### 2026-04-15 — Enrich the Cardinal Rule: consequences, perspective, capability

**Source:** [Issue #18](https://github.com/mightytech/nla-framework/issues/18) item 3
**Verdict:** Accept — as enrichment of principle #6, not a new principle
**Status:** resolved

**What to do:**
Rewrite nla-foundations.md principle #6 (The Cardinal Rule) with a three-beat structure:
(1) **Consequences** — humans bear them, authority follows accountability (existing, stays
the floor). (2) **Perspective** — the human brings context, experience, and frames the
AI doesn't have, including their gaps and limitations. Limitations are an asset — a
non-standard background produces lenses the AI's training can't. The AI should draw out
the human's perspective, not normalize it. (3) **Capability** — staying engaged builds
the human's judgment. Checkpoints on easy decisions build understanding for hard ones.
The goal isn't just good output — it's a human who's better at their work.

**Why it was accepted:**
The Cardinal Rule currently frames human involvement as accountability ("humans bear
consequences"). This is true but incomplete — it makes human involvement sound like a
constraint rather than a design advantage. The enrichment names what the framework
already produces: humans who stay engaged develop judgment, and their non-standard
perspectives make the work substantively better.

**Resolved:** 2026-04-15 — Rewrote principle #6 in nla-foundations.md with three-beat structure: consequences, perspective (limitations as asset), capability (engagement builds judgment).

---

### 2026-04-15 — /close convention: separate context from actionable decisions

**Source:** [Issue #19](https://github.com/mightytech/nla-framework/issues/19), [Issue #18](https://github.com/mightytech/nla-framework/issues/18) item 5
**Verdict:** Accept
**Status:** resolved

**What to do:**
Add guidance to the /close skill (and the maintain skill's session lifecycle section):
in State at Close, explicitly separate *context for next time* (background) from
*decisions awaiting implementation* (actionable). The next session's `/maintain` reads
State at Close — decided-but-unimplemented items should be as visible as pending friction
log entries. Convention, not machinery — no new files or scanning.

**Why it was accepted:**
Observed in facebook-moderation: a style guide mechanism was decided during /think,
recorded in the session log, then forgotten for two compilations. The human caught it;
the AI didn't. Session logs record decisions in prose but nothing distinguishes "context"
from "things that need doing." The fix is making the existing structure carry this
distinction.

**Resolved:** 2026-04-15 — Added guidance to State at Close section in core/skills/close.md: explicitly separate context from decisions awaiting implementation.

---

### 2026-04-15 — Bring NLA writing standards into the framework

**Source:** [Issue #21](https://github.com/mightytech/nla-framework/issues/21)
**Verdict:** Accept
**Status:** pending

**What to do:**
1. **Bring the standards in.** Copy the NLA writing standards from facebook-moderation
   (`reference/specs/implementation-standards/nla-writing.md`) into the framework,
   likely at `reference/nla-writing-standards.md`. The file is 479 lines, 33 standards
   across 9 sections.
2. **Review framework docs against them.** Use the two-pass structure from #21:
   Pass 1 (behavioral gaps) focuses on standards 2.3 (produces what it contains),
   2.4 (emphasis shapes character), 8.3 (operative docs). Pass 2 (craft refinements)
   focuses on 4.2 (naming consistency), 4.4 (cross-references), 3.5 (positive
   instruction). The review surfaces which standards find real gaps.
3. **Standards that find gaps earn active status.** Don't curate by editorial
   judgment — curate by what produces findings. Standards with no findings can be
   noted as "validated, no current gaps."
4. **Integrate.** The active standards inform `/validate` (as a review mode or check)
   and `/maintain` (as writing guidance when editing operative docs). The standards
   are quality criteria the AI applies when writing and reviewing NLA documents.

**Why it was accepted:**
33 empirically-grounded standards for writing NLA documents — the prose artifacts an LLM
reads as its runtime. Key findings: "the document produces what it contains" (the AI
won't fill gaps from general knowledge), "emphasis shapes character" (what you emphasize
is what you get), and the core reframe that NLA documents are source code, not
documentation. Validated through 28+ compilations, confirmed to apply to prose artifacts
(not just code), and used as a diagnostic tool that found gaps in 2 of 12 operative docs.

---

---

*This log is populated by `/check-feedback` (or any external feedback tool) and consumed
by `/maintain`. Resolved entries are moved to `feedback-log-archive.md`.*
