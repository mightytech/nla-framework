# Maintenance Session: Friction Log Communication Path

**Date:** 2026-02-23
**Status:** Complete

## Intent
Enable non-maintainer NLA users to get friction log entries to the project's
maintainer. The friction log captures observations from anyone, but the "now
what?" assumes the observer is the maintainer. When users and maintainers are
different people, entries need a communication path.

## Design Decisions
- **Friction-log skill stays unchanged for capture.** Fast, unobtrusive, log-and-
  move-on. No interruption to suggest sending.
- **Framework owns awareness, penny post owns mechanism.** Startup surfaces pending
  entries with generic "process or share" language. Write-letter (penny post) gains
  friction-entry compilation as a capability. Neither side dictates the other.
- **No penny post coupling in framework.** The framework says "share with your
  maintainer." The AI mentions /write-letter if available, suggests sharing the
  file directly if not. Intent-level guidance, not mechanism-level.
- **Session-end awareness in friction-log skill.** Brief nudge at session boundaries,
  not a workflow step. Menu bar, not wizard.
- **Friction log git storage logged as open question.** Working logs may belong
  outside git (like config.md). Archives may stay committed. Design session needed.

## Changes Made
- `core/skills/startup.md`: Added friction entry check to "After Loading" section —
  surface pending count in startup summary, note sharing option for non-maintainers
- `core/skills/friction-log.md`: Added "Session Awareness" section — AI surfaces
  pending entries at session boundaries
- `reference/friction-log.md`: Logged "should friction logs be gitignored?" as
  pending design question
- `install/update-notes.md`: Added entry for domain projects
- Penny post letter: notified penny post about write-letter enhancement

## Blast Radius
- `core/skills/startup.md`: all domain projects (new behavior at startup)
- `core/skills/friction-log.md`: all domain projects (new session awareness)
- Penny post changes (write-letter enhancement): separate project, separate session

## Post-Validate Fixes
- Converted framework's ejected `.claude/skills/friction-log/SKILL.md` to annotated
  wrapper delegating to `core/skills/friction-log.md` with blast radius addendum.
  Eliminates accumulated drift (missing diagnostic richness, mid-task capture,
  patterns-to-watch check, and session awareness sections).
- Checked preferences skill — ejection justified (real path differences: `config-spec.md`
  vs `app/config-spec.md`, different conflict detection targets).
- Fixed double separator in `reference/friction-log.md`
- Softened "non-maintainer" wording in startup — removed role detection condition,
  now always mentions both processing and sharing options

## State at Close
All framework changes implemented. Startup surfaces pending friction entries.
Friction-log skill has session awareness guidance. Friction log gitignore
question logged as pending design work. Update note written for domain projects.
Penny post letter delivered to `boxes/penny-post/` describing the write-letter
enhancement — that work happens in penny post's context in a separate session.

Pre-existing structural findings from validation (not from our changes):
- Missing /check-updates in create-app Category 1 table
- install/README.md doesn't mention package-intent.md
- README.md tree omits LICENSE, VERSION, config/
- Broader ejection drift in preferences wrapper (justified, not converting)
