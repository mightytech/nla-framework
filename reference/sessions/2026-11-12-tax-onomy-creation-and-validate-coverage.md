# Maintenance Session: tax-onomy Creation and /validate Coverage Gaps

**Date:** 2026-09-09 → 2026-11-12 (long-running; closed 2026-11-12)
**Status:** Complete

## Intent

The session began as project creation, not maintenance: generate a bare-scaffold
NLA for categorizing personal tax documents. The framework work was a byproduct
— generating a project exercised `/create-app` and the package intent files
against real conditions, and three defects fell out of that exercise. The
session's lasting contribution is the diagnosis of *why* those defects reached a
generated project: `/validate`'s structural check cannot see the surfaces they
live on.

## Changes Made

**Outside this repo** — `../tax-onomy/` created via `/create-app` in
bare-scaffold mode. 44 files, 20 skill wrappers, framework pinned to v0.0.12,
penny post and process helpers at HEAD. Recorded here because the creation
exercised framework surfaces; the project's own history lives in its repo, which
has since run its own maintenance sessions.

**In this repo** (commit `0e61e34`):

- `core/structure.md` — removed a `lib/.gitkeep` row claiming a file that
  doesn't exist. `lib/` holds `export.py` and needs no placeholder. The
  attribution stays accurate for new projects, where
  `install/structure-intent.md` still specifies the placeholder.
- `.claude/skills/validate/SKILL.md` — Structural Addenda #3 now excludes
  dispatcher mode files. The six `validate-*.md` files are modes of
  `validate.md`, not skills, and were reported as missing from
  `install/skills-intent.md` on every run. Six false positives per run trains
  the reader to skim the section where real findings appear. Re-verified clean
  at 14 vs 14.
- `reference/friction-log.md` — eight pending entries (below).

## Decisions Made

| Decision | Reasoning |
|----------|-----------|
| Used `packages/` paths for the six package skill wrappers, not the `../` sibling paths the package intents specify | Sibling paths resolve to nothing under the submodule model. Deviation logged in tax-onomy's `installed-packages.md`. The framework does **not** edit the packages — the 2026-03-04 precedent establishes that packages adopt conventions through their own `/update` channel. |
| Generated 14 framework wrappers, not the 13 in `/create-app`'s table | `install/skills-intent.md` documents `/session-checkpoint`; intent files are the declared source of truth. |
| Kept `disable-model-invocation: true` on all generated wrappers | The framework has adopted model-invokable wrappers in its own house, but `reference/plans/skills-doctrine-publication.md` gates publication on verification sessions. Generating the unpublished convention would diverge from the propagation path. Recorded in tax-onomy's design rationale so nobody hand-fixes it. |
| `core/structure.md` treated as internal for shippability | It records the framework's own directories; consumers keep theirs in `app/overview.md`. The path-shaped rule says `core/` is consumer-facing, so this is the rule's spirit against its letter — logged as its own entry. |
| Skipped the optional `/install` scenario trace | The coverage finding had already established the severity; the trace would have confirmed what was known. |

## Blast Radius

Both edits are internal — framework maintainers and framework maintenance
behavior. No `core/` consumer content, no intent files, no update-notes entry,
no tag. Of the eight logged entries, five propose changes with wider radius
(`core/skills/validate*.md`, `core/skills/maintain.md`,
`.claude/skills/create-app/SKILL.md`); none of those are implemented yet.

## Debrief

An explicit `/debrief` ran. Refined conclusions:

1. **Running `/validate` as a known-answer test was the session's highest-value
   move, and it is undocumented.** The structural check was invoked specifically
   to see whether it would catch two defects already known and logged. It caught
   neither, and that miss outranked both originals — it covered a class rather
   than an instance. Nothing in `/validate` suggests this use; every mode
   description frames the system as the object of inspection. Logged, with a
   proposed note for `validate-structural.md`. The friction log turns out to be a
   corpus of test cases, not just a work queue — a use it doesn't advertise.

2. **`/validate` recommends a disposition it is forbidden to execute.** "Fix now"
   sits in the dispositions list; Scope says "You don't: Edit any files." The
   drift the same section warns about then happened in this session: two
   approved fix-now findings existed only in conversation until a `/maintain`
   pass was requested at close. Logged. The gap is invisible from inside
   `/validate` — it surfaced only by debriefing a validation session.

3. **Five approval gates produced five approvals and zero edits.** Three were
   `/friction-log` draft gates, which mandate showing the full entry before
   writing. The gate earns its keep in the case where a draft is wrong; the cost
   here was five round trips for no corrections. Batching the final three into
   one gate helped and is the adjustment worth keeping. Separately, the AI ended
   several turns with two or three bundled questions; the maintainer answered one
   part and moved on both times. Recommend-and-proceed is the better default.

4. **The bare-scaffold double surface worked as designed.** Stub headers catch
   the unauthored gap at task-execution time; the preloaded friction entry
   catches it at `/maintain`-session start. tax-onomy's first maintain session
   authored `values.md` and added the first task — the entry was waiting where it
   was meant to be. Reads as redundancy until the timing difference is noticed.

5. **Generation experience confirms the pending 2026-05-24 scaffold-first
   entry.** Writing 44 files was mechanical; the judgment was the conversation,
   the inbox-vs-archive decision, catching the package path breakage, and the
   17-check verification. The verification held the value and is the part a
   script does better. Worth appending as a data point to that entry rather than
   opening a new one.

## State at Close

### Context for next time

- tax-onomy is live and has run its own sessions since creation. It has one
  authored task (`/categorize`), a designed ledger, a half-built `lib/`, and its
  own pending queue. Framework-side work should not reach into it; changes flow
  through `/update`.
- Nothing consumer-facing has landed since v0.0.12. Four commits sit past the
  tag, all internal.
- The two `/validate` fixes are verified, not merely applied — Addenda #3
  re-runs clean and `lib/export.py` is the only remaining `lib/` claim.

### Decisions awaiting implementation

None. Both fixes decided this session were applied and committed before close.

### Pending — eight friction entries

Three cluster on `/validate` and would likely be one `/maintain` arc rather than
three:

| Entry | Severity |
|-------|----------|
| `/validate`'s structural check can't see `/create-app` or package intents | major |
| `/validate` recommends "fix now" but cannot execute it | minor |
| Running `/validate` as a known-answer test is undocumented | positive |

The rest:

| Entry | Severity |
|-------|----------|
| Package intent files still specify pre-submodule sibling paths | major |
| `/session-checkpoint` missing from `/create-app`'s file tables | minor |
| Framework has no `/startup` wrapper; intent file says it should | minor — needs a ruling |
| `installed-packages.md` uses display names, not directory names | minor |
| `core/structure.md` is internal content inside a consumer-facing path | minor |

### Where to pick up

Start with the `/validate` cluster — the coverage entry is the one with teeth,
and resolving it closes the class that produced two of the others. Read it
alongside the pending 2026-05-24 scaffold-first entry: if `/create-app` moves to
deriving its skill list from `install/skills-intent.md`, that overlaps the
scaffold-generation proposal and the `/session-checkpoint` fix becomes
unnecessary rather than necessary.

Two items need the maintainer rather than the AI: the `/startup` wrapper ruling
(deliberate exception or oversight?), and whether the package sibling-path fix
travels by penny post letter to each package.
