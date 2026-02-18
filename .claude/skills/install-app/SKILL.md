---
name: install-app
description: Browse and install example NLA projects to explore how working NLAs look before building your own.
disable-model-invocation: true
---

# Install Example App

Help the user browse and install example NLA projects. These are complete, working NLAs
they can explore, run, and learn from — before building their own with `/create-app`.

---

## What to Do

1. **Read the catalog.** Read `install/example-catalog.md` for available example projects.

2. **Check for available examples.** If no repos have cloneable URLs yet (URLs marked
   as TBD), tell the user:

   > No example apps are available for cloning yet. Use `/create-app` to build your own
   > NLA project — it only takes a few minutes.

   End the skill here.

3. **Present the catalog.** Show the available examples with their descriptions and
   complexity levels. If there's only one, present it directly. If multiple, let the
   user choose.

4. **Clone the chosen project.** Clone to a sibling directory (`../[repo-name]/`).
   The framework path (`../nla-framework/`) must resolve from the install location.

5. **Orient the user.** Explain what they got:

```
Example app installed at ../[project-name]/

What's inside:
- app/              The application (voice, patterns, output spec, task doc)
- reference/        Maintenance records (friction log, design rationale)
- .claude/skills/   Skill entry points (thin wrappers to the framework)

Next steps:
1. cd ../[project-name]
2. Start Claude Code
3. Run /startup to load context
4. Try /[task-name] with some sample input

When you're ready to build your own project, come back here and run /create-app.
```

---

## What You Don't Do

- **Don't modify the cloned project.** Install as-is — the example has working content.
- **Don't run `git init`.** The cloned repo already has git history.
- **Don't start a conversation flow.** This is a quick install, not a design session.
  Read catalog, clone, orient, done.
