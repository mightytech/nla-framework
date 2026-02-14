---
name: create-sample-app
description: Install a complete sample NLA project (article formatter) to see how a working NLA looks before building your own.
disable-model-invocation: true
---

# Create Sample App

Install the scaffold as a standalone example NLA project. This gives the user a working article formatter they can explore, run, and learn from — before building their own project with `/create-app`.

---

## What to Do

1. **Ask where to install.** Default: `../nla-sample-app/`. Accept any path, but note the two constraints:
   - The framework path (`../nla-framework/`) must resolve from the install location (thin wrappers depend on it)
   - The install location shouldn't be inside another project's directory tree (Claude Code may pick up conflicting CLAUDE.md files)

2. **Copy the scaffold.** Copy the contents of `scaffold/` to the target directory. All files, preserving structure.

3. **Orient the user.** Explain what they're getting:

```
Sample app installed at ../nla-sample-app/

This is a complete, working NLA — an article formatter that transforms
rough drafts into polished, publication-ready Markdown.

What's inside:
- app/              The application (voice, patterns, output spec, task doc)
- reference/        Maintenance records (friction log, design rationale)
- .claude/skills/   Skill entry points (thin wrappers to the framework)

Next steps:
1. cd ../nla-sample-app
2. git init && git add -A && git commit -m "Sample NLA project"
3. Start Claude Code
4. Run /startup to load context
5. Try /format-article with some rough text

When you're ready to build your own project, come back here and run /create-app.
```

4. **Adjust paths if non-sibling.** If the user chose a non-default location, update the framework reference paths in thin wrappers and CLAUDE.md so `../nla-framework/` resolves correctly from the actual install location.

---

## What You Don't Do

- **Don't modify scaffold files.** Copy as-is — the scaffold has working sample content ready to use.
- **Don't run `git init`.** The user handles setup.
- **Don't start a conversation flow.** This is a quick install, not a design session. Ask the location question, copy, orient, done.
