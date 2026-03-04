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

1. **Ensure a session log exists** — check for a session log in `reference/sessions/`.
   If one exists for this session, review and update it. If none exists, create one.
2. **Finalize the session log** — make sure it's complete and accurate.
3. **Check for loose ends** — uncommitted changes, documentation mirrors, validation.
4. **Summarize state** — what's working, what's pending, where to pick up next.

---

## Session Log

### If a session log already exists

Review it against what actually happened in the session:

- **Changes Made** — Does it reflect all the work done? Update if anything is missing
  or stale from mid-session syncs.
- **Debrief** — If an explicit `/debrief` happened, capture the refined conclusions
  (distilled observations, not transcript). If no `/debrief` happened, add 2-3 brief
  observations from your participant-observer perspective — what worked, what was
  unclear, what surprised.
- **State at Close** — Fill in what's working, what's pending, what's next.
- **Status** — Set to Complete.

Don't rewrite sections that are already accurate. Update what's stale, fill what's empty.

### If no session log exists

Create one in `reference/sessions/` as `YYYY-MM-DD-brief-title.md`. Reconstruct from
what happened in the session. Match the project's session log conventions — maintenance
sessions typically use `# Maintenance Session:` as a title prefix; other session types
use a descriptive prefix that fits the work (e.g., `# Export Session:`, `# Session:`).

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

Use your judgment about what sections to include. A light session (installed a package,
ran validation) needs a lighter log than a heavy maintenance session. The format above
is a minimum; add sections like Decisions Made, What Didn't Work, or Blast Radius when
the session warrants them.

---

## Loose Ends

After the session log is settled, check for loose ends:

**Debrief.** If no `/debrief` happened this session and the work was substantive,
offer: "No debrief happened this session — want to run `/debrief` first, or should I
add brief observations myself?" If the work was light, skip the offer and add brief
observations directly.

**Uncommitted changes.** Check `git status`. If there are uncommitted changes, offer
to commit. Don't assume — the user may want to review first.

**Documentation mirrors.** If the session created, moved, or deleted files, check that
README.md's directory tree and any other manually-maintained listings are current.

**Validation.** If the session involved structural changes (file moves, renames, splits,
new files), suggest running `/validate` architecture review. Note what changed and why
validation would help — don't suggest it reflexively for every session.

---

## State Summary

End with a brief summary the human can scan:

- **What's working** — what was accomplished this session
- **What's pending** — open items, deferred work, things to come back to
- **Where to pick up** — what the next session should start with

This goes in the session log's State at Close AND in the conversation — the human
should see it without having to open a file.

---

## Scope

**You do:**
- Create or finalize session logs
- Capture debrief observations (brief if no explicit `/debrief` happened)
- Check for uncommitted changes and offer to commit
- Check documentation mirrors for staleness
- Suggest validation when structural changes warrant it
- Summarize session state for the human

**You don't:**
- Run validation (that's `/validate`)
- Edit application docs (that's `/maintain`)
- Make decisions for the human (that's the Cardinal Rule)
- Create friction log entries (that's `/friction-log` — but you can note observations
  that should become entries)

---

*A clean close makes the next session start faster. The five minutes spent wrapping up
save fifteen minutes of "where were we?" next time.*
