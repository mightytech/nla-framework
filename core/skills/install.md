# Install Package

You are installing an NLA package into the current project. Packages ship `install/` directories with intent files describing what an NLA should have. Your job is to read those intents and synthesize them into this NLA — matching its voice, structure, and conventions.

**This is additive work.** You're adding new capabilities, not replacing existing ones. The NLA's identity, voice, and domain-specific content are not yours to change.

---

## Input

The user provides a package reference as `$ARGUMENTS`:

- **Local path** (e.g., `../nla-penny-post/`) — verify it exists
- **GitHub URL** (e.g., `https://github.com/org/nla-penny-post`) — clone to `../repo-name/` as a sibling directory first
- **No argument** — ask the user what package to install

If cloning from a URL, confirm with the user before cloning: "I'll clone this to `../repo-name/`. OK?"

---

## Processing Flow

### 1. Read the Package Manifest

Read `[package-path]/install/install.md`. This tells you:
- What the package is
- What prerequisites it requires
- What intent files exist and what they target

If `install/install.md` doesn't exist, stop: "This doesn't look like an installable NLA package — no `install/install.md` found."

### 2. Pre-flight Checks

**Check prerequisites.** The manifest lists what the package requires (e.g., "NLA Framework installed," "GitHub CLI authenticated"). Verify what you can; flag what you can't.

**Check the install log.** Read `reference/installed-packages.md` (if it exists) to see if this package is already installed.

- If already installed, tell the user: "This package is already installed (logged on [date]). Did you mean `/update`?"
- If the user wants to proceed anyway, continue — but note it in the install log as a reinstall.

**If no install log exists,** that's fine — you'll create one after installation.

### 3. Process Each Intent File

For each intent file listed in the manifest:

1. **Read the intent file** — understand what the package wants the NLA to have
2. **Examine the NLA's current state** at that integration point (e.g., read `CLAUDE.md` if the intent targets it)
3. **Identify the delta** — what's already present vs. what's missing
4. **Propose changes** to the user, showing:
   - What file(s) will be modified or created
   - What will change (in behavioral terms, not just text diffs)
   - Why (what capability this adds)
5. **Wait for approval** before making changes
6. **Synthesize** — integrate the intent into the NLA's existing files

**Synthesis, not pasting.** Intent files describe what should exist, not literal text to copy. Match the NLA's voice, structure, and conventions. A formal NLA and a casual NLA should both get the same capability, expressed differently.

**Respect ejected wrappers.** If a skill wrapper has been customized beyond the thin wrapper pattern (ejected), don't overwrite it. Inform the user: "The `/[skill]` wrapper has been customized. The package wants [intent]. You can integrate this yourself, or I can add it — your call."

### 4. Update the Install Log

After all changes are made, update `reference/installed-packages.md`. Create the file if it doesn't exist.

**Log format:**

```markdown
## [Package Name]

**Source:** [path or URL]
**Installed:** [date]
**Package state:** [git commit hash if available, otherwise "snapshot on [date]"]

### What was done

| Intent File | Integration Point | Changes Made |
|-------------|------------------|--------------|
| [file] | [target] | [what changed, briefly] |

### Notes

[Any decisions made, things skipped, or issues encountered]
```

### 5. Post-install

Summarize what was installed:
- What capabilities the NLA now has
- Any manual steps remaining (if prerequisites couldn't be verified)
- Suggest running `/validate` to check consistency

---

## Edge Cases

- **Package has no intent files** — The manifest exists but lists nothing. Tell the user; there's nothing to install.
- **NLA already has everything** — Every intent is already satisfied. Log it as "verified current" rather than making no-op changes.
- **Conflicting content** — An intent wants something that contradicts what the NLA already has. Flag it. Don't silently resolve conflicts — the user decides.
- **Multiple packages in one session** — Each gets its own install log entry. Process them sequentially.

---

## Principles

- **Propose before implementing.** Show the user what you plan to change before changing it.
- **Match the NLA's voice.** Intent files describe what should exist. How it's expressed is up to the NLA.
- **Be additive.** Don't remove or replace existing NLA content. Framework and extension capabilities sit alongside domain content.
- **Log everything.** The install log is how `/update` knows what happened. Be thorough.
- **One intent at a time.** Process and get approval for each intent file individually. Don't batch all changes into one proposal.

---

*This skill is the standard entry point for adding new packages to an NLA. For updating already-installed packages, use `/update`.*
