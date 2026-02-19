# Update Installed Packages

You are updating packages that have already been installed in this NLA. The install log tells you what's installed; the package's current intent files tell you what should exist now. Your job is to find the delta and apply it.

**This is transformative work.** Unlike `/install` (purely additive), updates may modify content that was previously synthesized. Propose carefully — the user needs to understand what's changing and why.

---

## Input

The user may provide a package name or path as `$ARGUMENTS`:

- **Specific package** (e.g., `nla-penny-post` or `../nla-penny-post/`) — update only that package
- **No argument** — update all installed packages

---

## Processing Flow

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

### 6. Summary

Report what was updated:
- Which packages had changes
- What capabilities were added or modified
- Any manual steps remaining
- Suggest running `/validate` to check consistency

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

---

## Principles

- **Preserve history.** Append update records; don't replace install records. The log tells the full story.
- **Propose before implementing.** Even more critical than `/install` — updates modify existing content.
- **Don't undo user work.** If the user has changed something that an update would overwrite, flag it. The user decides.
- **Bootstrap gracefully.** Existing projects without install logs are the common case right now. Make baseline creation painless.
- **One package at a time.** Even when updating all, process each package separately so the user can approve or skip individually.

---

*This skill brings existing NLAs current with package changes. For adding new packages, use `/install`.*
