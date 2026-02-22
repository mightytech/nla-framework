# Maintenance Session: Package Intent File

**Date:** 2026-02-22
**Status:** Complete

## Intent
Document implicit package creation conventions explicitly, resolving the friction log
entry about pattern-matching against existing packages.

## Changes Made
- Created `install/package-intent.md` describing package conventions as a diff from
  domain project intent files — only what's different, inheriting the rest
- Archived two friction log entries (package conventions resolved, positive baseline)
- Updated README directory tree to include new file

## Blast Radius
- `install/package-intent.md`: future package creators only (no existing projects affected)
- README: documentation only

## Observations (from debrief)

**1. "Diff from baseline" as an intent file pattern.** The friction log entry assumed
three options (full intent file, documentation, or wait). The user's instinct to write
package-intent.md as a diff from existing intent files was a fourth option that emerged
from conversation — lighter than a parallel document, more discoverable than
documentation, and avoids dual maintenance. This pattern applies whenever a new category
(packages, plugins, etc.) shares most conventions with an existing one.

**2. Test-and-delete as a validation technique for intent files.** Creating a throwaway
package from the intent file, comparing it against the two real packages, then deleting
it — fast, confidence-building, and distinct from `/validate`. Worth remembering for
any intent file that describes what should be generated.

**3. Proportional effort throughout.** Minor friction log entry, minor solution, minor
validation. No over-engineering or unnecessary ceremony. The positive-entry archive was
a 30-second operation, which is the right size for "this doesn't need action."

## State at Close
Package intent file is committed and verified. Friction log has one remaining entry
(context window awareness, deferred). No pending work.
