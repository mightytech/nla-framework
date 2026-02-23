# Update Installed Packages

You are updating this NLA — pulling remote changes, applying package intents, or both. The install log tells you what's installed; the package's current intent files tell you what should exist now. Your job is to get everything current.

**This is transformative work.** Updates may modify content that was previously synthesized, and pulls change the state of local repositories. Propose carefully — the user needs to understand what's changing and why.

---

## Input

The user may provide a target as `$ARGUMENTS`:

- **Specific package** (e.g., `nla-penny-post` or `../nla-penny-post/`) — update only that package (pull its remote if ahead, then apply intent changes)
- **The NLA itself** (by name, or "my project," "this project") — pull the NLA's own remote only
- **No argument** — check everything. If only one thing needs updating, proceed with it (after confirming). If multiple things need updating, ask: "These have updates available: [list]. Which do you want to update? (Or all?)"

When the scope includes a package, the update covers both tiers: pulling the package's remote (if ahead and fast-forward) and applying its intent changes to the NLA. When the scope is the NLA itself, only the remote pull applies.

If nothing needs updating: "Everything is up to date."

---

## Phase 0: Safety Checks

Before making any changes:

### Check for Uncommitted Changes

Run `git status` on the NLA project. If there are uncommitted changes, warn the user:

"You have uncommitted changes. The rollback branch preserves your committed state, but uncommitted changes won't be included. I recommend committing or stashing first. Continue anyway?"

If the user says yes, proceed but note it in the summary.

### Create Rollback Branch

Create a branch named `pre-update-YYYY-MM-DD` from the NLA's current HEAD. If that name already exists, append `-2`, `-3`, etc. This branch covers the entire update session — one rollback point for all operations.

Tell the user: "Created rollback branch `pre-update-YYYY-MM-DD`. If anything goes wrong, you can return to this state."

**If the NLA has no git repository:** Skip the rollback branch. Warn: "This project isn't in a git repo, so I can't create a rollback branch. Changes will need to be reverted manually if needed. Proceed?"

---

## Phase 1: Pull Remote Changes

Pull the latest from remotes for the NLA and each package in scope. All pulls are independent — order doesn't matter. This phase is entirely mechanical (no judgment, no synthesis).

### For the NLA's Own Remote (if in scope)

1. Check if the NLA has a remote configured. If not: "No remote configured for this NLA — skipping remote check."
2. Run `git fetch`. If network failure: note it and continue with packages. "Couldn't reach the remote for this NLA. I'll still check local package changes."
3. Compare local HEAD to the remote:
   - **Up to date** — note it, move on.
   - **Fast-forward available** — perform `git merge --ff-only`. Report what was pulled.
   - **Not fast-forward (diverged)** — refuse. "Your NLA's local branch has diverged from the remote. This needs manual resolution — resolve with `git pull` or `git rebase` in this project, then re-run `/update`." Skip the NLA pull but continue with package updates if they're in scope.

### For Each Package in Scope

1. Locate the package using the source path from the install log.
2. Check if the package directory has a remote configured. If not: "Package [name] has no remote — I'll check local changes only."
3. Run `git fetch` in the package directory. If network failure: note it and continue. "Couldn't reach the remote for [name]. I'll check local changes only."
4. Compare local HEAD to the remote:
   - **Up to date** — note it.
   - **Fast-forward available** — perform `git merge --ff-only` in the package directory. Report what was pulled.
   - **Not fast-forward (diverged)** — refuse. "Package [name] has diverged from its remote. This needs attention in the package's own context — resolve the divergence in `[package path]`, then re-run `/update`." Skip this package's remote pull but still check its local-vs-installed state in Phase 2.

### Why Fast-Forward Only

Mechanical operations can cross context boundaries; judgment operations cannot. A fast-forward merge is pointer movement — no conflicts, no decisions. A non-fast-forward merge requires understanding both sides of the divergence, which means being in that project's development context. This NLA's context doesn't include the package's development reasoning. See `reference/design-rationale.md` ("Context Determines Competence") for the full principle.

### After All Pulls

Summarize: "Pulled latest for [list]. [Package X] was already up to date. [Package Y] had new changes. [Package Z] couldn't be reached / has diverged."

If no packages had local-vs-installed changes after the pulls, and no intent changes are pending: "Everything is current. No changes to apply." Stop here.

---

## Phase 2: Apply Intent Changes

This phase runs on whatever local state exists after Phase 1. If a package's remote pull was skipped (diverged or unreachable), Phase 2 still checks its local-vs-installed state — the local copy may have changes from a previous manual pull.

### 1. Read the Install Log

Read `reference/installed-packages.md` to determine what's installed.

**If no install log exists** — enter bootstrap mode (see below).

**If the log exists but is empty** — tell the user: "No packages are recorded as installed. Use `/install` to add packages, or I can bootstrap from what's already here."

### 2. Determine Scope

- If the user specified a package, find it in the install log. If not found: "I don't see [package] in the install log. Use `/install` to add it, or I can bootstrap it."
- If no argument, process all installed packages.

### 3. Detect Changes

For each package in scope:

1. **Locate the package's `install/` directory** using the source path from the install log
2. **Check for changes** since the logged state:
   - If git is available in the package repo: compare the logged commit hash against the current HEAD for `install/`
   - If no git or no commit hash: re-read all intent files and compare against what the log says was done
3. **Categorize changes:**
   - **Changed intents** — an existing intent file has been modified
   - **New intents** — intent files that didn't exist when the package was installed
   - **Removed intents** — intent files that no longer exist (rare; inform user but don't undo previous work)
   - **No changes** — package install directory is unchanged

If nothing changed: "Package [name] is up to date (no changes to install intents since [date])."

### 3b. Read Update Notes

Check if the package has an `install/update-notes.md` file. If it does, read it and
find entries between the project's last-known commit hash and the package's current
HEAD. These notes provide maintainer context about what changed and why — use them
alongside the intent diffs when proposing changes in step 4.

Notes may cover both intent-file changes (which you act on) and core-file changes
(which propagate automatically via the framework). For core-file changes, surface
the note as context for the project maintainer without proposing edits.

If no update notes file exists, or no entries fall in the relevant range, proceed
without them — notes are supplementary context, not a requirement. If the project's
last-known commit is old enough that relevant notes may have been archived, check
`install/update-notes-archive.md` too.

### 4. Apply Changes

**For changed intents:**
1. Read the current intent file
2. Read the install log entry for what was previously done
3. Examine the NLA's current state at the integration point
4. Identify the delta — what the updated intent wants that differs from what's there
5. Propose the change to the user, explaining what's different and why — incorporate
   any relevant update notes as additional context for the proposal
6. Wait for approval, then synthesize

**For new intents:**
- Treat as a fresh install — same process as `/install` step 3

**For removed intents:**
- Don't undo previous work. Inform the user: "The package no longer includes [intent file]. The changes it previously made are still in your NLA. Remove them manually if you want."
- Check update notes for context about why the intent was removed and what replaces it. Surface this to the user alongside the removal notification — it helps them decide whether and how to clean up.
- **Search for stale references.** Grep the project for mentions of the removed item — skill names, file paths, descriptions. Check beyond the known integration points: overview.md, system-status.md, README.md, and any other files that reference project structure or capabilities. Include stale references in your proposal so they can be cleaned up in the same pass.

**Respect ejected wrappers.** If a skill wrapper has been customized (ejected), don't overwrite it. Inform the user of upstream changes and let them decide how to integrate.

### 5. Update the Install Log

Append an update record to the package's section. Don't replace the original install entry — preserve history.

**Update log format:**

```markdown
### Updated [date]

**Package state:** [new commit hash or "snapshot on [date]"]

| Intent File | What Changed | Changes Made |
|-------------|-------------|--------------|
| [file] | [what's different in the intent] | [what was done to the NLA] |

**Notes:** [decisions, skipped items, issues]
```

### 6. Summary and Verification

Report what was updated:
- Which packages had remote changes pulled (Phase 1)
- Which packages had intent changes applied (Phase 2)
- What capabilities were added or modified
- Any manual steps remaining

**Check downstream targets.** After applying changes, review these files for consistency:
- **README.md** — hand-maintained directory trees and skill listings drift after structural changes
- **CLAUDE.md** — skill tables and file references
- **`app/overview.md`** — system descriptions and file hierarchies

Propose fixes for any inconsistencies found.

**Run `/validate`** structural check to verify consistency. Updates often have downstream effects that intent-diff analysis doesn't catch — validation is the safety net.

---

## Bootstrap Mode

When there's no install log but the NLA clearly uses the framework (has thin wrappers, references `../nla-framework/`), offer to establish a baseline.

**Bootstrap flow:**

1. Tell the user: "No install log found, but this NLA appears to use the NLA Framework. I can scan the framework's install intents against your current project to establish a baseline. This won't change any files — it just creates the install log so `/update` works going forward. Want me to do that?"

2. If approved:
   - Read `../nla-framework/install/install.md` and each intent file
   - For each intent, examine the NLA's current state and note what's already present
   - Create `reference/installed-packages.md` with a baseline entry:

```markdown
## NLA Framework

**Source:** ../nla-framework/
**Installed:** [date] (baseline — project predates install log)
**Package state:** [current commit hash]

### What was done

| Intent File | Integration Point | Status |
|-------------|------------------|--------|
| [file] | [target] | Present / Partially present / Missing |

### Notes

Baseline entry created by `/update` bootstrap. No files were changed — this records the current state so future updates can detect deltas.
```

3. After baseline is established, check for any deltas between current intents and what's present. If there are gaps, offer to apply them as updates.

4. If the NLA also has extension packages installed (e.g., penny post wrappers exist), offer to scan those too.

---

## Edge Cases

- **Package directory moved or missing** — "Can't find [package] at [path]. Has it moved? Provide the new path."
- **Install log is corrupted or unparseable** — Don't guess. Ask the user: "The install log is hard to parse. Want me to rebuild it from scratch (bootstrap mode)?"
- **User modified installed content** — The install log says one thing, the NLA says another. Don't overwrite user modifications without explicit approval. Show the diff and ask.
- **Multiple updates available** — Process each package in the order they appear in the install log. Present each package's changes separately.
- **Uncommitted changes in the NLA** — Warn before creating the rollback branch. The rollback branch preserves committed state; uncommitted changes need to be committed or stashed.
- **Network failure during fetch** — Degrade to local-only mode. Report what couldn't be reached, then proceed with local change detection for all packages.
- **Package or NLA with no remote configured** — Skip the remote check for that entry. Proceed with local-vs-installed checks.
- **Non-fast-forward on a package or NLA** — Refuse the merge. Direct the user to resolve the divergence in the affected repo's own context, then re-run `/update`.
- **Everything already up to date** — "Everything is up to date — no remote changes to pull and no intent changes to apply."
- **Rollback branch name collision** — Append `-2`, `-3`, etc. to the branch name.

---

## Principles

- **Preserve history.** Append update records; don't replace install records. The log tells the full story.
- **Propose before implementing.** Even more critical than `/install` — updates modify existing content.
- **Don't undo user work.** If the user has changed something that an update would overwrite, flag it. The user decides.
- **Bootstrap gracefully.** Existing projects without install logs are the common case right now. Make baseline creation painless.
- **One package at a time.** Even when updating all, process each package separately so the user can approve or skip individually.
- **Mechanical operations can cross contexts; judgment cannot.** Fast-forward merges on package repos are safe from the NLA's context — no conflicts, no decisions. Non-fast-forward merges require the package's development context. See `reference/design-rationale.md` ("Context Determines Competence").

---

*This skill brings the NLA current — pulling remotes, applying intent changes, or both. For checking what's available without applying changes, use `/check-updates`. For adding new packages, use `/install`.*
