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

---

## process helpers

**Source:** `../nla-process-helpers/`
**Installed:** 2026-02-22
**Package state:** commit `6c893ea`

### What was done

| Intent File | Integration Point | Changes Made |
|-------------|------------------|--------------|
| `CLAUDE-intent.md` | `CLAUDE.md` | Added `/unpack` to Available Skills table. Key files reference for `../nla-process-helpers/` was already present. |
| `skills-intent.md` | `.claude/skills/unpack/` | Created thin wrapper delegating to `../nla-process-helpers/app/unpack.md` |

### Notes

- This is the framework itself, not a domain project. The `/unpack` skill was previously a core framework skill; it was moved to the process helpers package as facilitation is a preference, not infrastructure. This install brings it back as a package-provided capability.

### Updated 2026-02-24

**Package state:** commit `e2a4a2f`

| Intent File | What Changed | Changes Made |
|-------------|-------------|--------------|
| `CLAUDE-intent.md` | Added awareness of 3 new techniques: brainstorm-cluster, steelman, devils-advocate | Added `/brainstorm-cluster`, `/steelman`, `/devils-advocate` to Available Skills table in `CLAUDE.md` |
| `skills-intent.md` | Added wrapper definitions for 3 new skills | Created thin wrappers: `.claude/skills/brainstorm-cluster/SKILL.md`, `.claude/skills/steelman/SKILL.md`, `.claude/skills/devils-advocate/SKILL.md` — all delegating to `../nla-process-helpers/app/[name].md` |

**Notes:** Straightforward addition of three new facilitation techniques. No conflicts with existing skills or content.
