# Package Structure Intent

What an NLA package looks like, described as differences from a domain project.

A package IS a domain NLA — it has `app/`, `reference/`, `.claude/skills/`, config,
the full maintenance cycle. Start from `structure-intent.md` and `CLAUDE-intent.md`
for the base. This file describes only what's different.

---

## What Makes a Package Different

A domain project is a standalone NLA that does work. A package is an NLA whose
primary purpose is providing capabilities that other NLAs install. The package
itself is maintained like any NLA (friction logs, /maintain, /validate), but its
skills run mostly in other projects via thin wrappers.

---

## install/ Directory

Domain projects don't have `install/`. Packages do — it's how other NLAs consume
the package.

```
install/
├── install.md           # Manifest — what the package is, prerequisites, how
│                        #   installation works, how updating and removing work
├── CLAUDE-intent.md     # What to add to the installing NLA's CLAUDE.md
└── skills-intent.md     # What skill wrappers to create in the installing NLA
```

**install.md** describes the package, its prerequisites, and the installation flow:
read each intent file, examine the target NLA's current state, synthesize the intent
into existing files (don't paste, integrate), log what was done in the target NLA's
`reference/installed-packages.md`.

**CLAUDE-intent.md** describes what the installing NLA's CLAUDE.md should know about
the package — typically a skills table section and any execution principles the
package needs.

**skills-intent.md** describes what skill wrappers to create in the installing NLA.
Package skill wrappers point to `../[package-name]/app/[skill].md` — the same thin
wrapper pattern as framework skills, but pointing at the package instead of the
framework.

---

## CLAUDE.md Differences

A package CLAUDE.md follows the same reference structure as CLAUDE-intent.md but
with these adjustments:

- **Title/Identity** names the package as an extension ("the first NLA extension,"
  "the second NLA extension") and explains that most users interact via thin wrappers
  from their own NLAs. Running the package directly is for maintenance and feedback.
- **Default mode** is package maintenance (maintaining the techniques, processing
  feedback about the package), not end-user task execution.
- **Skills table** splits into two sections: package skills (the capabilities other
  NLAs install) and framework skills (general NLA infrastructure).
- **Execution principles** include a package-specific third principle reflecting the
  package's character (e.g., "Rationale Over Speed" for penny post, "Facilitation
  Over Direction" for process helpers).
- **Remember** reinforces the dual context: when running directly, you maintain the
  package; when package skills run in other NLAs, the NLA's own context drives behavior.

---

## app/ Differences

Skill logic files in `app/` serve a dual role. They're both:
- The package's own task docs (executed when running the package directly)
- The delegation targets for thin wrappers in other NLAs

This means skill logic files need to work without assuming the package's own
CLAUDE.md is loaded. When another NLA's wrapper says "Read and follow
`../nla-process-helpers/app/unpack.md`", that file runs in the other NLA's context.

---

## What Stays the Same

Everything not mentioned above follows the domain project conventions in
`structure-intent.md` and `CLAUDE-intent.md`:

- `app/overview.md`, `app/config-spec.md`, `app/shared/` — same structure
- `reference/` — all the same files (design-rationale, friction-log, feedback-log,
  installed-packages, system-status, sessions/)
- `.claude/skills/` — framework wrappers (same thin wrapper pattern) plus domain
  skills for package-specific capabilities
- `config.md`, `config/`, `.gitignore` — same config system
- `README.md` — same structure, describing the package

---

*This describes intent, not literal text. A future `/create-package` skill or a
human creating a package should start from the domain project conventions and apply
these differences.*
