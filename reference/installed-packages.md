# Installed Packages

Record of NLA packages installed in this project. Each entry tracks what was installed,
from which package, and what changes were made. This log enables future updates and
uninstalls.

---

## penny post

**Package:** `../nla-penny-post/`
**Installed:** 2026-02-17
**Install directory state:** Current as of 2026-02-17

### Changes made

**From `CLAUDE-intent.md`:**
- Added `/check-feedback` and `/write-letter` to the Available Skills table in `CLAUDE.md`
- Added `reference/feedback-log.md` and `../nla-penny-post/` to the Key Files table in `CLAUDE.md`
- Note: feedback log files (`reference/feedback-log.md`, `reference/feedback-log-archive.md`) were already created during the same session as part of implementing the feedback log as a framework-level concept (Issue #2). The penny post CLAUDE intent reinforces their role.

**From `skills-intent.md`:**
- Created `.claude/skills/check-feedback/SKILL.md` — thin wrapper delegating to `../nla-penny-post/app/check-feedback.md`
- Created `.claude/skills/write-letter/SKILL.md` — thin wrapper delegating to `../nla-penny-post/app/write-letter.md`
