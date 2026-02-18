---
name: plan
description: Planning mode for framework changes — new features, structural changes, or significant modifications
disable-model-invocation: true
---

# Framework Planning Mode

You are planning a change to the NLA Framework — a new capability, a structural change, or a significant modification. Your job is to think through the design before implementation begins.

## Required Reading

Before planning, read these to understand the current system:

1. **`core/nla-foundations.md`** — NLA concepts and principles
2. **`reference/design-rationale.md`** — Why things are the way they are
3. **`reference/friction-log.md`** — Recent learnings, unresolved issues

Then read any files specific to the area you're planning changes for.

## Planning Process

### 1. Articulate Intent

What should the framework do differently? Write this in plain language before diving into files.

### 2. Identify Blast Radius

For each proposed change:
- **Core changes** — affect all domain projects on `git pull`
- **Scaffold changes** — affect new projects only
- **Reference changes** — affect framework maintainers only

### 3. Think Through the Structure Gradient

- **Where does the human need flexibility?**
- **Where does the LLM add structure?**
- **Where does traditional code handle things?**

### 4. Check Downstream Effects

- Will this break existing domain projects?
- Do intent files need updating? (`install/`)
- Does the framework README need changes?
- Should this be documented in CONTRIBUTING.md?

### 5. Produce a Plan Document

Save to `reference/` as a plan document. Include:
- Intent (what and why)
- Blast radius for each change
- Implementation phases
- What's being deferred and why

## After Planning

The plan document is reviewed and approved by the human before implementation begins. Use `/maintain` to implement approved plans.

---

*Plan first, build second. Framework changes ripple to every project — the time spent planning prevents disruption.*
