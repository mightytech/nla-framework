# Session Checkpoint

A mid-session save point. Like `/startup` loads context at the beginning of a session,
`/session-checkpoint` preserves and refreshes context at a transition point within a
session — between work phases, after completing a block of work, before reasoning from
files read earlier.

**The problem it solves:** Long sessions accumulate context that thins as the
conversation grows. Decisions made early in the session — file contents, design choices,
spec interpretations — may be compressed by the time they're needed later. A checkpoint
saves what matters and re-reads what's needed for the next phase.

---

## When to Use

Invoke explicitly (`/session-checkpoint`) or suggest at natural transitions:

- **Between work phases** — after finishing one block of work, before starting another
  that draws on different inputs
- **Before reasoning from files read long ago** — when you're about to make decisions
  based on documents read earlier in the session that may have been compressed
- **After evaluation, before diagnostics** — evaluation results are fresh; earlier
  context may be thin
- **When you notice needing to re-read** — if you're unsure about something you read
  earlier, that's the signal

**The timing insight:** Checkpoint before you're about to *reason from* files you read
a long time ago, not before you're about to *produce output* from recent conversation.
The natural instinct is to checkpoint when you feel tired or when a task ends. The
productive moment is when the *context* needs it most — when the next phase depends on
inputs that may have thinned.

Don't checkpoint after trivial work or between rapid-fire small tasks — the overhead
isn't justified.

---

## What to Do

Three steps, kept lightweight (~2-3 minutes):

### 1. Save state

Update the session log with current progress — what's been done, what's decided, what's
next. If no session log exists yet, create one. This is the "save your game" step — if
the session ends unexpectedly or context degrades, the session log has the state.

Check whether any observations from the current work phase should be saved to memory.
Most won't — but if you learned something about the user's preferences, the project's
state, or the process that future sessions should know, save it now while context is
fresh.

### 2. Identify and re-read key files

Based on what the *next* phase of work needs, identify 3-5 files to re-read. The goal
is to have the most important inputs fresh in context for the upcoming work, not to
re-read everything.

Examples:
- Before applying feedback: re-read the foundations doc + the relevant feedback items
- Before diagnostics: re-read the spec + evaluation results
- Before a new maintenance task: re-read the friction log + relevant app docs

Re-read these files. Don't summarize them — the point is having the actual content in
context.

### 3. Brief status anchor

Output a brief status summary (3-5 lines) so the conversation has a clear anchor point.
What just happened, what's next, any decisions that carry forward. This helps both you
and the human orient after the checkpoint.

---

## What Not to Do

- Don't re-read every file from `/startup` — that's a full context load, not a checkpoint
- Don't create new session logs or memory entries unless there's genuinely new state to capture
- Don't turn this into a planning session — save state, refresh context, move on
- Don't checkpoint between every step — only at real transitions where context matters

---

*A checkpoint is two minutes that saves twenty minutes of degraded reasoning. The best
time to checkpoint is before you need to — when the next phase depends on context that
might have thinned.*
