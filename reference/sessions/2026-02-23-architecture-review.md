# Architecture Review: NLA Framework

**Date:** 2026-02-23
**Focus:** Recent changes — startup friction-entry awareness, friction-log session awareness, update-notes entry, friction-log pending entry

## Document Chain

The review traced these paths through the framework:

**Startup path (domain projects):**
`CLAUDE.md` → `.claude/skills/startup/SKILL.md` (thin wrapper) → `core/skills/startup.md` → reads `reference/friction-log.md` for pending entries

**Friction-log path (domain projects):**
`CLAUDE.md` → `.claude/skills/friction-log/SKILL.md` (thin wrapper) → `core/skills/friction-log.md` → reads/writes `reference/friction-log.md`

**Friction-log path (framework):**
`CLAUDE.md` → `.claude/skills/friction-log/SKILL.md` (ejected, full skill) → reads/writes `reference/friction-log.md`

**Update path (domain projects):**
`core/skills/update.md` → reads `install/update-notes.md` (step 3b)

**Maintain path (domain/framework):**
`core/skills/maintain.md` / `.claude/skills/maintain/SKILL.md` → reads `reference/friction-log.md` at session start

## Findings

### Fix

*(none)*

### Improve

1. **`reference/friction-log.md` (lines 156-158):** Double `---` separator between the last entry and "Patterns to Watch." The deferred entry (2026-02-22) ends with `---` at line 156, then an empty line, then another `---` at line 158 before "Patterns to Watch." This creates a visually empty section. One separator is enough. — **Consistency**
   - **Blast radius:** Framework operation (the framework's own friction log)

2. **`.claude/skills/friction-log/SKILL.md` (framework wrapper):** The framework's friction-log skill is an ejected (full) implementation, not a thin wrapper. It is missing the "Session Awareness" section added to `core/skills/friction-log.md`. This means when the framework itself is used, the `/friction-log` skill will not surface pending entries at session boundaries. The update-notes entry (2026-02-23) says "No action needed — these propagate automatically via thin wrappers. If you ejected either skill, review the changes and consider incorporating them." The framework itself is the primary example of an ejected friction-log skill, and the new behavior does not propagate to it. — **Conditional completeness**
   - **Blast radius:** Framework operation
   - The session log (2026-02-23-friction-log-communication-path.md) does not mention this gap. The framework is a single-maintainer context, so the non-maintainer communication path is less relevant, but the session awareness nudge ("N pending entries, process or share") would still be useful for the framework's own maintainer.

3. **`.claude/skills/friction-log/SKILL.md` (framework wrapper):** The ejected framework wrapper is also missing several other sections that have been added to `core/skills/friction-log.md` over time: "Diagnostic richness" (self-aware diagnostics with exact quotes), "When invoked mid-task" (fast capture during other work), and the "Patterns to Watch" post-drafting check. These predate the current review's focus but compound the ejection drift. — **Consistency**
   - **Blast radius:** Framework operation

4. **`core/skills/startup.md` (line 40):** The directive "If the user isn't the project's maintainer" relies on the LLM inferring the user's role without any established mechanism for determining this. The framework does not define what makes someone a "maintainer" vs. a regular user, or how the LLM should determine this during a session. In practice, the LLM would need to guess based on context (did the user run /maintain? did they ask about the system vs. using it?). This is acceptable as a judgment call, but the ambiguity may cause inconsistent behavior — the LLM might always or never surface the sharing suggestion depending on how it reads the context. — **Prerequisite sufficiency**
   - **Blast radius:** All domain projects

### Note

5. **`core/skills/friction-log.md` vs. `core/skills/startup.md`:** The startup skill explicitly mentions `/write-letter` as a potential sharing mechanism (line 41-42: "if `/write-letter` or other sharing tools are available, mention them naturally"). The friction-log Session Awareness section (lines 143-149) says only "processed (`/maintain`) or shared with the project's maintainer" without mentioning any specific sharing tool. This is intentionally different — startup is the more detailed surface point, friction-log session awareness is deliberately brief ("menu bar, not wizard"). The asymmetry is a design choice, not an inconsistency. — **Consistency** (confirmed consistent)

6. **`install/update-notes.md` (2026-02-23 entry):** The update note correctly describes both changes and accurately states "No action needed" for thin-wrapper users with appropriate ejection guidance. The note omits the `**Commit:**` field, which is documented as optional in the entry format spec. The note's "Affects" line lists both changed core files. Well-formed entry. — **Cross-reference integrity** (confirmed consistent)

7. **`reference/friction-log.md` (2026-02-23 entry):** The new "Should friction logs be gitignored?" entry is well-formed and correctly tagged as pending. It raises a design question about whether friction logs should be gitignored (like config.md). The session log (2026-02-23) correctly records the design decision to log this as an open question rather than act on it. The entry's "Proposed fix" correctly directs to a `/think` session. — **Cross-reference integrity** (confirmed consistent)

8. **`core/skills/maintain.md` Session Start (lines 28-36) vs. `core/skills/startup.md` After Loading (lines 37-43):** Both surfaces count pending friction log entries, but for different audiences: maintain is for the maintainer starting a maintenance session, startup is for any user starting a regular session. The maintain session start includes more detail (counts both friction and feedback logs, checks for resolved-but-unarchived entries, reads last session log for continuity). Startup just checks pending friction entries. These are complementary, not duplicative. — **Consistency** (confirmed consistent)

9. **Session log `2026-02-23-friction-log-communication-path.md`:** The session log's "Changes Made" lists a penny post letter as one of the changes. This is cross-project work logged from the framework's perspective. The session correctly notes "that work happens in penny post's context in a separate session." The log is well-formed, status is Complete, blast radius is documented, and all changes are accounted for. — **Cross-reference integrity** (confirmed consistent)

10. **`core/skills/friction-log.md` Session Awareness scope boundary:** The Session Awareness section says to "briefly surface any pending entries" at session boundaries. This creates an implicit responsibility for the AI to monitor for session boundaries even when the `/friction-log` skill is not actively loaded. The section is part of the skill file, which is only loaded when `/friction-log` is invoked. The AI would need to remember this guidance after the skill invocation ends. In practice, the CLAUDE.md skills table doesn't mention session awareness, and the skill's `disable-model-invocation: true` means it's not loaded into the active prompt. The guidance may only be effective if the AI happens to have recently read the friction-log skill. — **Prerequisite sufficiency**
    - **Blast radius:** All domain projects

## Summary

10 findings: 0 fix, 4 improve, 6 note.

The recent changes (startup friction-entry awareness, friction-log session awareness, update note, friction log entry) are internally consistent with each other and with the broader framework. The update note accurately describes the changes and their propagation characteristics. The session log correctly records design decisions and blast radius.

The main findings:

- The framework's own ejected friction-log wrapper has drifted from the core skill and is missing the new Session Awareness section plus several earlier additions (Improve #2, #3). This is the expected consequence of ejection, but the gap is growing.
- A double `---` separator in the framework's friction log is a minor formatting issue (Improve #1).
- The "user isn't the project's maintainer" check relies on LLM inference without a defined mechanism (Improve #4).
- The friction-log Session Awareness section lives in a skill file that's only loaded on invocation, creating a "remember this even when I'm not loaded" pattern that may not be effective in practice (Note #10).
