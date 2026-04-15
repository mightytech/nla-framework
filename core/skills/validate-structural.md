# Structural Validation

Check that the system's internal references are consistent. This is a mechanical check — verify that things point where they claim to point.

**How to check:** Use built-in file tools (Glob, Read) rather than Bash for existence checks. These tools provide clearer output and don't require permission configuration.

**What to check:**

1. **File references.** Read CLAUDE.md, app/overview.md, all task docs in `app/`, and all skill files in `.claude/skills/`. For every file path mentioned, verify the file exists. Report any broken references with the source file and the missing target.

2. **Skill table consistency.** Compare the skills tables in CLAUDE.md and app/overview.md. They should list the same skills. Check `reference/system-status.md` too if it has a skills table. Report any mismatches (skill in one table but not another).

3. **Thin wrapper targets.** For every skill in `.claude/skills/` that delegates to the framework (contains a `Read and follow` line pointing to `packages/nla-framework/`), verify the target file exists. Report any broken wrappers.

4. **Task doc references.** For each task doc in `app/`, check that referenced shared docs exist (e.g., `app/shared/values.md`, `app/shared/voice.md`, `app/shared/common-patterns.md`). If a task doc references `app/shared/output-spec.md`, verify it exists — but don't flag its absence if nothing references it. Not every NLA needs an output spec file.

5. **Document hierarchy.** If `app/overview.md` has a document hierarchy or index section, check that every file listed exists and every existing `app/` file is listed. Report gaps in either direction.

6. **Config consistency.** If `config.md` exists, check that any sub-configs it routes to (files in `config/`) exist. If `app/config-spec.md` exists, check that CLAUDE.md references it. Report issues.

**Output format:**

```
## Validation Results

### Issues Found
- [Category]: [Specific issue — source file, missing target, or mismatch details]

### All Clear
- [Category]: [What was checked and passed]
```

7. **Package consistency.** If `reference/feedback-log.md` exists but no `/write-letter` skill is registered in `.claude/skills/`, note it: "Feedback infrastructure exists but penny post isn't installed. Run `/install` to add it, or remove the feedback log files if feedback isn't needed." Similarly, check that other package-created files have their corresponding skills.

8. **Submodule consistency.** If `reference/installed-packages.md` exists, check that each installed package has a corresponding submodule in `packages/`. Run `git submodule status` and verify each logged package appears. Report missing submodules: "[Package] is recorded as installed but has no submodule in `packages/`." If no install log exists, check whether `packages/` contains submodules at all — if it does, note: "Found submodules in `packages/` but no install log. Run `/update` to bootstrap an install log."

If everything passes, say so clearly. If issues are found, suggest fixes but do not make them — that is `/maintain`'s job.
