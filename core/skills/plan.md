# Planning Mode

You are planning a change to the NLA system — a new task, a structural change, or a significant modification. Your job is to think through the design before implementation begins.

## Required Reading

Before planning, read these to understand the current system:

1. **`../nla-framework/core/nla-foundations.md`** — NLA concepts and principles
2. **`app/overview.md`** — What this NLA does, how pieces connect
3. **`reference/design-rationale.md`** — Why things are the way they are
4. **`reference/system-status.md`** — Current state

Then read any files specific to the area you're planning changes for.

## Planning Process

### 1. Articulate Intent

What should the system do differently? What new capability is needed? Write this in plain language before diving into files and structure.

### 2. Identify Affected Pieces

- What shared foundations apply?
- What new task docs are needed?
- What existing behaviors change?
- What skills need creating or updating?

### 3. Think Through the Structure Gradient

For each part of the planned change, consider:
- **Where does the human need flexibility?** Accept whatever they provide.
- **Where does the LLM add structure?** Translate between human messiness and system requirements.
- **Where does traditional code handle things?** API calls, validation, deterministic operations.

### 4. Design the Learning Loop

How will we know if this works?
- What does success look like?
- What should the friction log capture?
- How will human corrections feed back into improvements?

### 5. Produce a Plan Document

Save to `reference/` as a plan document. Include:
- Intent (what and why)
- Affected files and changes
- Implementation phases
- What's being deferred and why

## After Planning

The plan document is reviewed and approved by the human before implementation begins. Use `/maintain` to implement approved plans.

---

*Plan first, build second. The time spent planning saves time in implementation and prevents structural debt.*
