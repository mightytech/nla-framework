# Check for Available Updates

You are scanning this NLA and its installed packages for available updates. This is a read-only operation — you report what's available and recommend actions, but you don't apply changes.

---

## Input

The user may provide a target as `$ARGUMENTS`:

- **Specific package** (e.g., `nla-penny-post`) — check only that package
- **No argument** — check everything: the NLA's own remote and all installed packages

---

## Processing Flow

### 1. Read the Install Log

Read `reference/installed-packages.md` to determine what's installed.

**If no install log exists:** "No packages are recorded as installed. Use `/install` to add packages, or `/update` in bootstrap mode to establish a baseline."

### 2. Check the NLA's Own Remote

1. Check if the NLA has a git remote configured. If not: "No remote configured for this NLA — nothing to check."
2. Run `git fetch` (fetch only — do not merge). If network failure: "Couldn't reach the remote for this NLA." Note it and continue.
3. Compare local HEAD to the remote tracking branch:
   - **Up to date** — "Your NLA is current with the remote."
   - **Fast-forward available** — "Your NLA is behind the remote by N commits. `/update` can handle this."
   - **Diverged** — "Your NLA has diverged from the remote. This needs manual resolution before updating — resolve with `git pull` or `git rebase`."

### 3. Check Each Installed Package

For each package in the install log (or the specific package requested):

**Tier 1 — Remote to Local:** Has the package author pushed changes you haven't pulled?

1. Locate the package using the source path from the install log.
2. Check if the package directory has a git remote. If not: "No remote for [name] — skipping remote check."
3. Run `git fetch` in the package directory. If network failure: note it, continue.
4. Compare local HEAD to the remote:
   - **Up to date** — note it.
   - **Fast-forward available** — "Package [name] is behind its remote by N commits. `/update` can handle this."
   - **Diverged** — "Package [name] has diverged from its remote. Resolve in `[path]` before updating."

**Tier 2 — Local to Installed:** Has the local package changed since the NLA last installed or updated?

1. Compare the install log's recorded commit hash (or date) against the package's current local HEAD.
2. If different: "Package [name] has local changes since your last update on [date]."
3. If the same: "Package [name] is current with what's installed."

### 4. Summary Report

Present a consolidated view:

```
Source             Remote → Local            Local → Installed       Action
─────────────────  ────────────────────────  ──────────────────────  ──────────────
NLA (this project) 2 commits behind          —                       /update
NLA Framework      up to date                3 commits ahead         /update nla-framework
Penny Post         up to date                up to date              current
Process Helpers    5 commits behind           up to date              /update nla-process-helpers
```

**Recommendation patterns:**

| Remote → Local | Local → Installed | Recommendation |
|---------------|-------------------|----------------|
| Fast-forward available | Changes pending | Run `/update [name]` — pulls remote and applies intent changes |
| Fast-forward available | Up to date | Run `/update [name]` — pulls latest from remote |
| Up to date | Changes pending | Run `/update [name]` — applies local intent changes |
| Diverged | Any | Resolve divergence in `[path]` first, then `/update` |
| Up to date | Up to date | Current — nothing to do |
| Network failure | Any | Couldn't check remote — try again later, or run `/update [name]` for local changes only |

If everything is up to date: "All packages and the NLA are current. No updates available."

---

## Edge Cases

- **No install log** — Direct to `/install` or `/update` bootstrap mode.
- **No packages have remotes** — Tier 1 is skipped for all packages. Still useful for Tier 2 (local vs. installed).
- **All up to date** — Report it clearly. Nothing else needed.
- **Network failures** — Report what couldn't be checked. Still report local-vs-installed for all packages (no network needed).
- **Package directory moved or missing** — "Can't find [package] at [path]. Has it moved?"

---

## Principles

- **Read-only.** Don't modify anything. Fetch (to compare), but don't merge.
- **Report, don't prescribe.** Show what's available and recommend actions. The user decides what to update and when.
- **Degrade gracefully.** Network failures, missing remotes, missing install logs — handle each without aborting the entire check. Report what you could check and what you couldn't.

---

*This skill reports what's available. To apply updates, use `/update`. To add new packages, use `/install`.*
