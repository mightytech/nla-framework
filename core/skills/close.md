# Close Session

You are wrapping up a work session. Your job is to make sure the session has a complete,
accurate record — and that the human knows where things stand for next time.

This skill can be invoked explicitly or suggested by the AI when a session is winding
down. It works after any substantive work session — maintenance, content creation,
installation, export — not just `/maintain` sessions.

---

## When to Suggest This

Recognize endings — moments when the work is done and the human is about to leave:

- The user signals they're wrapping up ("okay, let's stop here," "that's it for today")
- A debrief conversation has just concluded
- The last planned item in a session has been resolved
- The user asks about committing or saving state

The prompt is low-cost: "Want to run `/close` to wrap up the session?" The user can
say no. Don't suggest it after trivial work — a quick config change, a single typo fix.

---

## What This Skill Does

These steps run in dependency order. Earlier steps can produce work that should
land in the session log; later steps can produce a tag that depends on what got
committed.

1. **Validate** — if the session involved structural changes, suggest `/validate`.
2. **Check documentation mirrors** — README trees, skill tables, manually-maintained listings.
3. **Debrief** — if no `/debrief` happened and the work was substantive, offer one (or add brief observations directly).
4. **Finalize the session log** — create or update so it reflects everything including the work done in steps 1–3.
5. **Commit + tag (if pushing) + push** — commit pending changes, tag if pushing consumer-facing work, push.

The order matters. Validation can surface issues that produce more work; mirror
fixes are themselves changes; debrief informs the session log; the tag decision
depends on what's actually being pushed. Doing the session log first would freeze
it before the close-time work is done.

---

## 1. Validate

If the session involved structural changes — file moves, renames, splits, new files,
new directories, new top-level files — suggest running `/validate` architecture review.
Note what changed and why validation would help.

If the session was content-only (text edits to existing files, no structural shifts),
skip this step. Reflexive validation runs dilute the signal.

If `/validate` surfaces issues that warrant fixing now, fix them before continuing.
Those fixes become part of the session and need to land in the session log (step 4)
before being committed (step 5).

---

## 2. Check Documentation Mirrors

If the session created, moved, or deleted files — or added/removed skills, intent
files, or other listed artifacts — check that manually-maintained listings still
match reality:

- README.md directory trees
- Skill tables in CLAUDE.md
- Any other lists that mirror filesystem state

Documentation mirrors are mechanical drift; the cost to fix is low and the cost
to leave stale is "next session reads a wrong listing as authoritative."

Also check `reference/friction-log.md` and `reference/feedback-log.md` for entries
marked `Status: resolved` that haven't been moved to the archive. The procedure
step in `/maintain` only fires during the session that resolves an entry, so
entries resolved without immediate archival drift across sessions. If any exist,
archive them now — same family of drift as documentation mirrors, different
surface.

---

## 3. Debrief

If a `/debrief` already happened during the session, you'll capture its conclusions
in the session log (step 4) — nothing more to do here.

If no `/debrief` happened and the work was substantive, offer:
> "No debrief happened this session — want to run `/debrief` first, or should I add
> brief observations myself?"

If the work was light, skip the offer and plan to add 2–3 brief observations
directly during step 4. Use your participant-observer perspective: what worked,
what was unclear, what surprised.

Debrief reflects everything that happened in the session — including the validation
and mirror work from steps 1–2.

---

## 4. Finalize the Session Log

By this step, all the session's work — including the close-time work from steps 1–3
— is done. The session log captures the complete arc.

### If a session log already exists

Review it against what actually happened. Don't rewrite sections that are accurate;
update what's stale, fill what's empty.

- **Changes Made** — does it reflect all the work done, including any close-time
  validation fixes or mirror updates? Update if anything is missing.
- **Debrief** — if an explicit `/debrief` happened, capture the refined conclusions
  (distilled observations, not transcript). If no `/debrief` happened, add 2–3 brief
  observations from your participant-observer perspective.
- **State at Close** — fill in what's working, what's pending, what's next. Explicitly
  separate *context for next time* (background the next session should know) from
  *decisions awaiting implementation* (actionable items that need doing).
  Decided-but-unimplemented items should be as visible as pending friction log
  entries — they're the things most likely to fall through between sessions.
- **Status** — set to Complete.

### If no session log exists

Create one in `reference/sessions/` as `YYYY-MM-DD-brief-title.md`. Reconstruct from
what happened. Match the project's session log conventions — maintenance sessions
typically use `# Maintenance Session:` as a title prefix; other session types use a
descriptive prefix that fits the work (e.g., `# Export Session:`, `# Session:`).

```markdown
# [Type] Session: [Brief Title]

**Date:** YYYY-MM-DD
**Status:** Complete

## Intent
[What this session changed about the system's behavior, and why.]

## Changes Made
- [What changed and why — behavioral description, not file-level]

## Debrief
[2-3 brief observations — what worked, what was unclear, what surprised.]

## State at Close
[What's working, what's pending, what's next]
```

Use your judgment about which sections to include. A light session (installed a
package, ran validation) needs a lighter log than a heavy maintenance session. The
format above is a minimum; add sections like Decisions Made, What Didn't Work, or
Blast Radius when the session warrants them.

---

## 5. Commit, Tag (If Pushing), Push

Check `git status`. If there are uncommitted changes — including the session log
itself, plus any work from steps 1–3 — offer to commit. The user may want to
review first; don't assume.

Use your judgment about commit shape. A single coherent "session close" commit is
fine when the close-time changes are small. Separate commits when the changes are
substantial enough to merit independent review (e.g., a non-trivial validation fix
that should be its own commit).

### Tag decision

The framework's Shippability rule attaches tags to *push moments*, not commits.
For the full reasoning, see the maintain skill's "Shippability at Commit Time"
section — at `packages/nla-framework/core/skills/maintain.md` in a domain
project, at `core/skills/maintain.md` when running in the framework itself.
Apply the rule here:

1. Are we pushing? If no — skip the tag. Tags are for consumers; an unpushed tag
   is noise. The next push (whenever it happens) will tag whatever consumer-facing
   work has accumulated.
2. If yes, review the commits since the last tag. If any of them touched
   consumer-facing content (per the Shippability classification), tag HEAD before
   pushing. If none did, push without tagging.

A session that produces three consumer-facing commits gets one tag at push, not
three.

**Use annotated tags.** Create the tag with `git tag -a vX.Y.Z -m "message"`,
not the lightweight form `git tag vX.Y.Z`. Annotated tags carry the message
and push under `git push --follow-tags`; lightweight tags are skipped silently
by `--follow-tags` and won't reach the remote. Match the project's existing
tag style by checking `git tag -l --format='%(objecttype)' vX.Y.Z` on a recent
tag if uncertain.

### Push

After committing (and tagging if applicable), push. The session is now visible to
consumers.

If the user prefers to leave changes local — review tomorrow, sit with them
overnight — that's fine. Skip the tag, skip the push, and note in the State at
Close that the session ended with unpushed work.

---

## State Summary

End with a brief summary the human can scan in the conversation:

- **What's working** — what was accomplished this session
- **What's pending** — open items, deferred work, things to come back to
- **Where to pick up** — what the next session should start with

This is the same content as the session log's State at Close — surface it in the
conversation so the human sees it without opening a file.

---

## Scope

**You do:**
- Suggest validation when structural changes warrant it
- Check documentation mirrors for staleness
- Capture debrief observations (brief if no explicit `/debrief` happened)
- Create or finalize session logs
- Offer to commit pending changes
- Apply the Shippability tag-at-push rule when the user is pushing
- Summarize session state for the human

**You don't:**
- Run validation (that's `/validate`)
- Edit application docs (that's `/maintain`)
- Make decisions for the human (that's the Cardinal Rule)
- Create friction log entries (that's `/friction-log` — but you can note observations
  that should become entries)
- Push or tag without the user's go-ahead

---

*A clean close makes the next session start faster. The five minutes spent wrapping up
save fifteen minutes of "where were we?" next time.*
