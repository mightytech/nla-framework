# System Validation

You are validating this NLA system — checking that its pieces are consistent, its document references resolve, and its instructions would produce the intended behavior. You are not transforming content and you are not editing the system. You are inspecting it.

---

## Required Reading

Before validating, read:

1. **`CLAUDE.md`** — Skills table, key files, runtime identity
2. **`app/overview.md`** — How pieces connect, skill tables, document hierarchy

Do not read every app file upfront. Read specific files as validation requires them.

---

## Mode Selection

When invoked with clear intent, skip the menu and route directly to the appropriate mode. When invoked without clear intent, present these options:

> **"Are my files wired up correctly?"**
> Structural check. Verifies file references, skill tables, and document hierarchy. Fast and mechanical.

> **"Do my docs tell a consistent story?"**
> Architecture review. Walks the full document chain checking for coherence issues. Thorough — reads most of your app docs. Writes findings to a file in `reference/sessions/`.

> **"Walk me through a scenario"**
> Scenario walkthrough. Describe a situation and I'll trace through the docs showing what would happen and where gaps exist.

> **"Something's not working as expected"**
> Debug. Describe expected vs. actual behavior and I'll trace through docs to explain the divergence.

---

## Mode Routing

After selecting a mode, read and follow the corresponding file:

| Mode | File |
|------|------|
| Structural check | `../nla-framework/core/skills/validate-structural.md` |
| Architecture review | `../nla-framework/core/skills/validate-architecture.md` |
| Scenario walkthrough | `../nla-framework/core/skills/validate-scenario.md` |
| Debug | `../nla-framework/core/skills/validate-debug.md` |

---

## Scope

**You do:**
- Check internal consistency of the project's documentation structure
- Walk the document chain checking for coherence issues
- Trace through docs for hypothetical scenarios
- Diagnose behavior divergence from expected outcomes
- Read trace files when available
- Suggest documentation fixes

**You don't:**
- Edit any files (that is `/maintain`)
- Run actual tasks (you narrate what would happen)
- Fix issues you find (report them; the user decides what to act on)
- Generate friction log entries (the user can invoke `/friction-log` for issues worth tracking)

---

*Validation is read-only inspection. Find problems, explain them, point to fixes — then hand off to `/maintain` or `/friction-log`.*
