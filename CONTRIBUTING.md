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
- Well-tested — verified against the sample formatter at minimum
- Backwards-compatible when possible

Changes to `core/nla-foundations.md` affect how LLMs understand what NLAs are. Changes to `core/skills/` affect how every project's skills behave.

### Scaffold changes (`scaffold/`)

These only affect new projects. Existing projects don't receive scaffold updates. These are lower risk and good starting points for contributors.

### Documentation changes

README, CONTRIBUTING, and other developer-facing docs. Always welcome.

---

## How to Propose a Change

1. **Open an issue** describing the behavioral intent — what should change and why
2. **Include context** — what you observed, what friction prompted this, what you tried
3. **If you have a fix**, submit a PR with:
   - The behavioral description in the PR body (not just "updated file X")
   - Before/after examples if the change affects LLM behavior
   - Confirmation that you tested with the sample formatter

---

## What to Avoid

- **Domain-specific changes to core** — If it only applies to your use case, it belongs in your domain project, not the framework
- **Style-only changes** — NLA prose is functional, not decorative. Rewording for style risks changing behavior
- **Adding /learning-feedback to core** — This was intentionally excluded. It's a domain extension, not universal infrastructure. See the design rationale.

---

## Testing

The scaffold includes a sample article formatter. At minimum, test that:

1. Copy scaffold to a temp directory
2. Run `/startup` — confirm it reads all five documents
3. Run `/format-article` with sample content — confirm output follows voice and patterns
4. Run `/friction-log` — confirm entries follow the format in `reference/friction-log.md`

---

*This project treats its own documentation with the same care it asks of NLA builders. When you change the framework, you're changing how every NLA built on it behaves.*
