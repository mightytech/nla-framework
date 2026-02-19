# Architecture Review: NLA Framework

**Date:** 2026-02-19
**Context:** Post-session review following the Duet feedback processing session that broadened language across multiple core files, removed /plan, added NLA Shapes, and designed the update notes system.

## Document Chain

The framework has a dual-audience document chain: one for framework users (building/maintaining NLAs) and one for the framework itself (maintaining the framework).

### Framework user chain (from CLAUDE.md)

```
CLAUDE.md
  → core/nla-foundations.md (loaded by domain projects at startup)
  → install/ intent files (read by /create-app, /install, /update)
     ├── CLAUDE-intent.md
     ├── skills-intent.md
     └── structure-intent.md
  → core/skills/ (delegated to by domain project thin wrappers)
     ├── startup.md
     ├── maintain.md
     ├── friction-log.md
     ├── preferences.md
     ├── validate.md → validate-structural.md
     │               → validate-architecture.md
     │               → validate-scenario.md
     │               → validate-debug.md
     ├── install.md
     └── update.md
  → install/update-notes.md (read by /update as context)
```

### Framework self-maintenance chain

```
CLAUDE.md (framework identity, skills table)
  → config.md → config/maintenance.md
  → .claude/skills/ (full skills, not thin wrappers)
     ├── create-app/SKILL.md (reads install/ intent files)
     ├── install-app/SKILL.md (reads install/example-catalog.md)
     ├── maintain/SKILL.md (reads reference/ files)
     ├── validate/SKILL.md (delegates to core/skills/validate-*.md)
     ├── friction-log/SKILL.md (reads reference/friction-log.md)
     ├── preferences/SKILL.md (reads config-spec.md)
     ├── install/SKILL.md (thin wrapper → core/skills/install.md)
     ├── update/SKILL.md (thin wrapper → core/skills/update.md)
     ├── check-feedback/SKILL.md (thin wrapper → ../nla-penny-post/)
     └── write-letter/SKILL.md (thin wrapper → ../nla-penny-post/)
  → reference/ (design-rationale, friction-log, feedback-log, sessions/)
```

### Conditional branches

- `config.md` → `config/maintenance.md` (only in maintenance mode)
- `install/update-notes-archive.md` (only when project's last-known commit is old)
- `app/startup.md` (only in domain projects, if it exists)
- `app/shared/output-spec.md` (only if it exists)

## Findings

### Fix

1. **`README.md`**: The directory tree is incomplete and outdated. — **Cross-reference integrity**

   The README's "What's in the Framework" tree shows:
   ```
   .claude/skills/
       ├── create-app/
       └── install-app/
   ```
   But the actual `.claude/skills/` directory contains 10 skills: check-feedback, create-app, friction-log, install, install-app, maintain, preferences, update, validate, write-letter. This significantly understates the framework's skill surface. A user reading the README would not know about framework-level maintain, validate, friction-log, preferences, install, update, check-feedback, or write-letter.

   The tree also omits several files and directories that exist:
   - `install/update-notes.md` (listed in the tree, good)
   - `install/README.md` (not listed)
   - `core/skills/README.md` (not listed, but the skills/ directory is)
   - `config-spec.md` (not listed)
   - `config.md` and `config/` (not listed, but these are gitignored so omission is reasonable)
   - `CONTRIBUTING.md` (not listed in the tree, but linked at the bottom)
   - `LICENSE` (not listed)
   - `VERSION` (not listed)
   - `reference/designs/` (not listed)
   - `reference/feedback/` (not listed)
   - `reference/installed-packages.md` (not listed)

2. **`core/skills/validate.md`** (dispatcher): Mode routing table uses domain-project paths that do not resolve from the framework. — **Path resolution**

   The dispatcher's routing table says:
   ```
   | Structural check | `../nla-framework/core/skills/validate-structural.md` |
   | Architecture review | `../nla-framework/core/skills/validate-architecture.md` |
   ```

   These paths are designed for domain projects (where `../nla-framework/` resolves). When running from the framework itself, these paths would resolve to `../../nla-framework/core/skills/...`, which is wrong. The framework's own validate skill wrapper (`.claude/skills/validate/SKILL.md`) correctly routes using `core/skills/validate-*.md` paths in its mode routing table, so in practice the framework workaround is in place. But the core dispatcher file, which domain projects also read, contains paths that only work from domain projects. This is by design for domain projects, but it means the dispatcher itself is not self-consistent when read from the framework context.

   This is a known architectural trade-off (documented in design-rationale under "Framework Self-Maintenance") and the framework's wrapper compensates. However, the dispatcher is the only core skill file that uses `../nla-framework/` paths for internal references to other core files — all other core skill files use relative references (e.g., `reference/friction-log.md`). The validate dispatcher is inconsistent with its siblings.

3. **`core/skills/README.md`**: The "What's Here" table is missing the `/install` and `/update` skills. — **Cross-reference integrity**

   The table lists 11 files (startup, maintain, friction-log, validate dispatcher + 4 modes, preferences) but omits `install.md` and `update.md`. These files exist in `core/skills/` and are referenced by thin wrappers, but anyone reading the README to understand the directory's contents would not know they exist.

### Improve

4. **`core/skills/validate.md`** (dispatcher): Required reading references `app/overview.md` which does not exist in the framework. — **Conditional completeness**

   Line 12: `2. **app/overview.md** — How pieces connect, skill tables, document hierarchy`

   The framework has no `app/` directory. This is the generic dispatcher intended for domain projects, so it correctly references `app/overview.md` for domain project use. But when the framework's validate skill wrapper reads this file, the instruction asks it to read a file that doesn't exist.

   The framework's validate wrapper (`.claude/skills/validate/SKILL.md`) provides its own required reading that replaces this, but the mismatch could cause confusion if the LLM tries to follow both the wrapper's instructions AND the core file's instructions. The wrapper says "read CLAUDE.md and install intent files"; the core file says "read CLAUDE.md and app/overview.md." Both instructions are active in context.

5. **`core/skills/maintain.md`**: Several references assume domain project structure that doesn't exist in the framework. — **Generic/specific alignment**

   The maintain skill references:
   - `app/overview.md` (line 15) — framework has no `app/`
   - `app/shared/common-patterns.md` (line 95) — framework has no shared patterns
   - `app/shared/voice-and-values.md` (line 96) — framework has no voice doc
   - `app/shared/output-spec.md` (line 97) — framework has no output spec
   - "Adding a New Task" section (lines 209-216) references `app/`, `app/overview.md`

   This is the core maintain skill that domain projects delegate to, so these references are correct for domain use. The framework's own maintain wrapper compensates with framework-specific instructions. The issue is that the LLM reads both the wrapper and the core file, and the core file contains references that do not resolve in the framework context.

   The framework wrapper handles the "What You Can Edit" table correctly (substituting `core/`, `install/`, etc. for `app/`) but does not explicitly say "ignore the domain-project-specific sections of the core maintain file." The LLM must use judgment to skip inapplicable sections.

6. **`install/structure-intent.md`**: No mention of `reference/installed-packages.md` in the directory layout tree. — **Cross-reference integrity**

   The directory layout tree (lines 22-36) shows the `reference/` contents but omits `installed-packages.md`. The file IS described later in the document (lines 160-166, under "Reference File Structures"), but someone reading the tree to understand expected directory structure would not see it. Since `/create-app` uses this tree as structural guidance, generated projects might not get a prompt to include the install log in their directory structure (though the file generation table in create-app does include it).

7. **`install/skills-intent.md`**: Missing `/check-feedback` and `/write-letter` from the skills list. — **Cross-reference integrity**

   The skills intent file lists 7 framework skills (startup, maintain, friction-log, validate, preferences, install, update) but the framework's CLAUDE.md skills table lists 11 skills (adding create-app, install-app, check-feedback, write-letter). Two of the missing ones (create-app, install-app) are framework-only skills not intended for domain projects, so their absence is correct. But check-feedback and write-letter are penny post skills that ARE installed in domain projects via a separate package — they should not be listed here since they belong to the penny post install manifest, not the framework's.

   This is actually correct as-is: the skills-intent file describes what the *framework* package installs, and penny post is a separate package. However, the current state creates a gap: the CLAUDE.md skills table includes all 11 skills, but `skills-intent.md` only covers 7. A new maintainer might think the intent file is incomplete. A note clarifying that penny post skills are managed by the penny post package's own install manifest would prevent confusion.

8. **`CLAUDE.md`**: The key files table references `../nla-penny-post/` but doesn't clarify its relationship. — **Prerequisite sufficiency**

   The key files table lists `../nla-penny-post/` with purpose "Penny post extension (feedback conventions and skills)." If this sibling repo doesn't exist (e.g., a new contributor clones only the framework), two skills (check-feedback, write-letter) would have broken delegation paths. The table doesn't note that this is an optional extension.

9. **`config-spec.md`**: References `/plan` implicitly in the maintenance mode "Plan first" option. — **Consistency**

   Line 22: `- **Plan first** — Whether to always enter planning mode before making framework changes, or allow direct editing for small changes.`

   The session log says this was reframed to "reference planning mode generally rather than the removed skill." The current text says "planning mode" which is correct and does not mention `/plan`. However, the session log's addendum says "The config-spec 'Plan first' option is reframed to reference planning mode generally rather than the removed skill," implying a change was made. The current text is clean — this note is for confirmation that the cleanup was completed successfully.

   **Actually clean — no issue.** Keeping as a note for transparency.

10. **`core/skills/startup.md`**: References documents in order but doesn't handle the framework-as-self case. — **Conditional completeness**

    The startup skill says to read `app/overview.md`, `app/shared/voice-and-values.md`, `app/shared/common-patterns.md`, and `app/shared/output-spec.md`. None of these exist in the framework. The framework doesn't have a `/startup` wrapper (it's not in `.claude/skills/`), which means this file is only read by domain projects — so its domain-project references are correct.

    But `skills-intent.md` lists startup as a framework skill that should be installed in domain projects. The framework itself doesn't use startup, which is appropriate — the framework's CLAUDE.md serves as its own initialization. No issue here; noting for completeness.

11. **`install/structure-intent.md`**: The `installed-packages.md` description is in the "Reference File Structures" section but not in the directory tree. — **Consistency**

    Same as finding #6 but from the consistency angle: the document describes the file in one section but omits it from the canonical directory listing. Two parts of the same document disagree on what the reference directory contains.

12. **`reference/design-rationale.md`**: The "Validate Dispatcher + Mode Files" section says Copydesk proposed `/code-review` which became "Mode 4." But the actual validate modes are: structural (1), architecture review (2), scenario walkthrough (3), debug (4). Architecture review is Mode 2 in the menu, not Mode 4. — **Consistency**

    The design rationale says "implemented it as Mode 4 of `/validate`" which appears to be the original numbering from when the proposal was accepted. The actual dispatcher presents architecture review as the second option. The numbering discrepancy is minor (the modes aren't really "numbered" in the dispatcher) but could confuse someone reading the rationale alongside the dispatcher.

### Note

13. **`update-notes.md`**: References `update-notes-archive.md` which does not yet exist. — **Conditional completeness**

    Line 9: "For older notes, check `update-notes-archive.md`." This file does not exist yet. The update notes system was just designed and implemented; the archive file will be created when notes are first archived. This is a forward reference that's not yet needed. The `/update` skill also references the archive (line 63: `check install/update-notes-archive.md too`).

    Not an issue now — the file will be created when needed. But if `/update` is run and tries to read the archive, it will get a file-not-found. The skill's conditional language ("if the project's last-known commit is old enough") should prevent this in practice, since all current update notes are very recent.

14. **`reference/installed-packages.md`**: Only records the penny post package. The NLA Framework itself is not recorded as an "installed package" in the framework's own install log. — **Consistency**

    Domain projects would have the framework as their first install log entry (per `/create-app` guidance). The framework itself doesn't have a framework entry, which makes sense (the framework doesn't install itself). But the file's purpose statement says "Record of NLA packages installed in this project" — and the framework does have penny post installed.

    This is fine — penny post is the only external package. Noting for awareness.

15. **`friction-log-archive.md`**: Contains a reference to `/plan` in a resolved entry. — **Orphaned content**

    The 2026-02-12 entry says: "...with `/plan` if scope warrants it." This is a historical record, so updating it would alter the archive. Archives should preserve history. Not worth changing.

16. **`README.md`**: The "Upgrading" section doesn't mention `/update`. — **Prerequisite sufficiency**

    The upgrading section says `git pull` is all that's needed, with a table of what updates automatically vs. what requires manual sync. It doesn't mention that `/update` exists for checking whether intent file changes need to propagate to domain projects. For simple framework users this is fine — `git pull` does handle most updates. But the existence of `/update` as a tool for catching intent-file-level changes is worth a mention, especially since the update notes system now exists to surface these.

17. **Framework `.claude/skills/install/SKILL.md` and `update/SKILL.md`**: These are thin wrappers using `../nla-framework/` paths. — **Path resolution**

    These two skills use the domain-project pattern (`Read and follow ../nla-framework/core/skills/install.md`) rather than framework-relative paths. When invoked from the framework itself, `../nla-framework/` resolves to `../../nla-framework/` which would fail if the framework's parent directory doesn't contain another `nla-framework/`.

    In practice, these skills are unlikely to be invoked from the framework directory (you don't install the framework into itself). But it's inconsistent with the other framework skills (maintain, validate, friction-log, preferences) which use full, framework-specific wrappers. If someone ever runs `/install` from the framework to add a package, it would try to read `../nla-framework/core/skills/install.md` which resolves incorrectly.

18. **`core/skills/friction-log.md`**: No mention of blast radius in the entry format. — **Generic/specific alignment**

    The core friction-log skill (used by domain projects) doesn't include a "Blast radius" field in its entry guidance. The framework's own friction-log wrapper adds blast radius awareness. This is correct — domain projects don't have the same blast radius concept (they're self-contained). However, the framework wrapper adds blast radius but doesn't tell the LLM to also include it in the entry format fields. The framework's `reference/friction-log.md` entry format DOES include blast radius, so the format definition wins. No real issue — the format file is the source of truth.

19. **`CLAUDE.md`**: The skills table lists `/plan` as a skill. — **Wait, re-checking...**

    I verified earlier that `/plan` does not appear in CLAUDE.md. Confirmed: CLAUDE.md is clean. Disregard this tentative finding.

## Summary

18 findings: 3 fix, 9 improve, 6 note. (Finding 19 was retracted.)

**Overall assessment:** The framework is in strong shape following the Duet feedback session. The major changes (NLA Shapes, broadened Cardinal Rule, output-spec conditionality, /plan removal, update notes system) were implemented cleanly with good traceability. The issues found are mostly in peripheral documentation (README directory tree, core/skills README table) and in the inherent tension between core skill files designed for domain projects and the framework's own self-maintenance needs.

The most impactful fix is the README directory tree (#1), which significantly understates the framework's capabilities. The core/skills README missing install and update (#3) is a similar gap. The validate dispatcher path issue (#2) is architecturally interesting but compensated by the framework's wrapper.

The recurring theme is **documentation artifacts that mirror filesystem state drifting after changes** — exactly the pattern noted in the friction log entry from this same session. The README tree, the core/skills README table, and the structure-intent directory tree are all manual mirrors that fall behind when files are added, moved, or removed.

No contradictions were found. No orphaned content that matters (the /plan reference in the friction-log archive is historical and should stay). The language breadth improvements from the Duet session appear to have landed cleanly — I found no remaining transformation-specific language in places that should be shape-neutral.
