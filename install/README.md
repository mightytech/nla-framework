# install/ — Intent Files

This directory describes what an NLA needs to be built on the NLA Framework. It is the
single source of truth for project structure, skill wrappers, and runtime identity.

---

## What Intent Files Are

Intent files describe **what should exist** in a framework-based NLA — not literal
templates to copy. They specify sections, structures, and purposes at a conceptual level.
The AI reading them synthesizes actual content that matches the target NLA's voice,
domain, and conventions.

This is the **synthesis principle**: the same intent produces different content for
different NLAs. A formal legal-document NLA and a casual social-media NLA both get
the same structural elements, expressed in their own voice.

---

## The Three Intent Files

| File | Integration Point | Describes |
|------|------------------|-----------|
| `CLAUDE-intent.md` | NLA's `CLAUDE.md` | Runtime identity, grounding principles, modes, execution rules, reference section structure |
| `skills-intent.md` | NLA's `.claude/skills/` | Framework skill wrappers with complete reference implementations, domain skill pattern |
| `structure-intent.md` | NLA's directory layout | Required directories, reference file structures, mechanical file templates |

Each file covers a different integration point. Together they describe everything the
framework provides to a domain project.

---

## How They're Used

**`/create-app`** reads these files as its primary source when generating new NLA
projects. Intent files provide the structural guidance; the creation conversation
provides domain-specific content.

**`/install`** reads these files when adding the framework to an existing NLA. It
compares intent against the NLA's current state and synthesizes what's missing.

**`/update`** diffs these files against the install log (`reference/installed-packages.md`)
to detect what's changed since the last install or update.

---

## Building an Install Directory for a New Package

Extension packages (like penny post) follow the same pattern:

1. Create an `install/` directory in your package
2. Add an `install.md` manifest describing the package and prerequisites
3. Add intent files for each integration point your package touches
4. Include reference implementations where applicable (skill wrappers, file structures)

The `/install` skill reads any package's `install/` directory using the same synthesis
principle — intent in, domain-appropriate content out.

---

*This directory is maintained as part of the NLA Framework. Changes here affect what
every framework-based NLA is expected to have.*
