# Contributing to the NLA Framework

Thank you for your interest in contributing. This document explains how to propose changes and what to keep in mind.

---

## The Key Principle: Intent Over Implementation

When proposing a change, describe the *behavioral intent* — what the system should do differently and why. A diff shows what text changed; intent explains what actually matters.

**Good:** "The /maintain skill should check for downstream effects before proposing edits, because changes to shared docs silently affect all tasks."

**Less useful:** "Add a paragraph to maintain.md between lines 45 and 50."

NLA changes are behavioral, not textual. The same intent might be implemented with different wording depending on context. Start with why, not where.

---

## Types of Changes

### Core changes (`core/`)

These affect every domain project on their next `git pull`. They should be:
- Universal — applicable to any NLA, not just one domain
- Well-tested — verified against an example NLA at minimum
- Backwards-compatible when possible

Changes to `core/nla-foundations.md` affect how LLMs understand what NLAs are. Changes to `core/skills/` affect how every project's skills behave.

### Intent file changes (`install/`)

These affect how `/create-app` generates new projects and how `/install`/`/update` modify existing ones. They should be:
- Consistent with the structures they describe
- Complete — every framework-provided file should have structural guidance
- Intent-focused — describe WHAT and WHY, not literal templates

### Documentation changes

README, CONTRIBUTING, and other developer-facing docs. Always welcome.

---

## How to Propose a Change

1. **Open an issue** describing the behavioral intent — what should change and why
2. **Include context** — what you observed, what friction prompted this, what you tried
3. **If you have a fix**, submit a PR with:
   - The behavioral description in the PR body (not just "updated file X")
   - Before/after examples if the change affects LLM behavior
   - Confirmation that you tested with an example NLA

---

## What to Avoid

- **Domain-specific changes to core** — If it only applies to your use case, it belongs in your domain project, not the framework
- **Style-only changes** — NLA prose is functional, not decorative. Rewording for style risks changing behavior
- **Adding /learning-feedback to core** — This was intentionally excluded. It's a domain extension, not universal infrastructure. See the design rationale.

---

## Testing

### Intent file test

Verify that intent files are consistent with the framework:

1. Check that every core skill has a reference wrapper in `install/skills-intent.md`
2. Check that structural guidance in `install/structure-intent.md` covers all framework-provided files
3. Run `/validate` to check framework consistency

### /create-app test

If your change affects intent files or `/create-app`:

1. Run `/create-app` from the framework directory
2. Create a test project (any domain)
3. In the new project: run `/startup` — confirm it reads all five documents
4. Run the domain task skill — confirm it works
5. Check that CLAUDE.md skills table matches actual `.claude/skills/` contents

---

*This project treats its own documentation with the same care it asks of NLA builders. When you change the framework, you're changing how every NLA built on it behaves.*
