# Plan/Handoff Template

A scaffold for writing plans that cross a session boundary — typically
from a drafting session's warm context to a future session's cold
context. The template gives the drafter a shape to fill so the cold
executor inherits what the warm drafter knew. Used during the
plan-while-hot beat of The Session-Bracketing Discipline
(`core/nla-foundations.md`).

The template scaffolds — it doesn't enforce. Sections can be dropped when
the work doesn't warrant them. The drafter answers each section from
warm context (cheap) what the cold executor would otherwise improvise
(lossy).

---

## When to use this template

When a plan will be executed by a cold-context agent — a future session,
a different operator, a fresh-context AI. The template is handoff
scaffolding answering "what does the cold executor need from the warm
drafter?"

Plans that don't cross a cold/warm boundary — continuation plans where
the same author resumes within the same session — may carry only a
subset. The template is most valuable where the drafter and executor
have different context.

---

## Sections

### Title + Intent

What the plan does and why it matters. Intent at every layer means: not
just what the plan as a whole does, but what each major step intends.
The cold executor with intent at every step handles deviations that
intent-free instructions can't.

### Substance

What to do. Steps, decisions, references. The bulk of the document. If
the cold executor follows just this section, they can execute the plan
— the other sections enrich, calibrate, and surface judgment moments.

### Procedural-edge cases

What to do when reality deviates from the plan's assumptions. Items the
warm drafter wouldn't anticipate because they weren't executing — but
can pre-think while context is warm. Examples: what if a prerequisite
isn't met? What if a referenced file has changed since drafting? What
if a tool call fails?

### Judgment defaults

Where to lean when rule space is open. Items where the right answer
depends on context the cold executor doesn't have; the warm drafter
pre-decides them. Format: "Lean: X. Reason: Y." with the option to
deviate if execution-time evidence supports a different choice.

### Confidence band

Where the cold executor should expect to push back at the next
collaborative step. Where the drafter is uncertain; what would change
the answer. Honest acknowledgment of "I'm 60% on this" is more useful
to the cold executor than feigned certainty — it tells them to weigh
fresh evidence rather than defer to the drafter's framing.

### Warm-context next-steps

What other work benefits from the warm context this session produced?
Three sub-parts:

- **Specific candidates** — next-phase plans, spec/standards drafts,
  friction log entries, memory updates — anything where the warm
  context would be lossy to defer
- **Generic open-question** — "anything else?" — for unstructured
  surfacing the specific list won't elicit
- **Calibration** — typical lean: capture-shaped work warm; defer
  execution-shaped work to fresh session

This section is plan-shape that fits even non-handoff plans. It asks
the drafter what *else* warm context could produce, not just what the
current plan covers.

### Block-end checkpoints

At each major block's end, pair specific questions (tied to that
block's decisions) with at least one generic open-question (for
unstructured surfacing). The specific questions verify the block's
intended outputs; the generic question catches what neither drafter nor
executor pre-thought of.

---

## Section dropping

Drop sections when they don't earn their weight:

- **No confidence band** if the plan is high-certainty across the board
- **No procedural-edge cases** if the plan is small enough that "if
  something deviates, surface it" is sufficient
- **No judgment defaults** if no judgment calls remain (rare; most
  plans have some)
- **Truncate warm-context next-steps** to "nothing else surfaces" if
  the session is at a natural end

What earns a section's weight: it saves the cold executor from
improvising under worse context than the drafter had.
