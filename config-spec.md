# Configuration Spec

This document defines what users of the NLA Framework can configure. The `/preferences` skill reads this to guide the configuration conversation and enforce constraints.

---

## What's Configurable

Users can adjust how the framework's tools behave without modifying the framework itself. The main areas:

### `/create-app` Behavior

- **Project location** — Whether `/create-app` asks where to save the new project, or silently uses a default. Users who always create projects in the same place can skip the question.
- **Default project directory** — The default location for new projects (e.g., `~/projects/`). Only used when the location question is skipped.
- **Conversation depth** — How much guidance `/create-app` provides during the creation conversation. Ranges from verbose (explains each step, good for first-time users) to terse (minimal prompting, for experienced users who know what they want).
- **File narration** — Whether to explain what each generated file does during project creation, or generate silently with a summary at the end.

**Defaults:** Ask about project location. Moderate guidance. Narrate file generation.

### Maintenance Mode

- **Plan first** — Whether to always enter `/plan` before making framework changes, or allow direct editing for small changes.
- **Proposal style** — How detailed change proposals should be. Ranges from full (current text, proposed text, rationale) to brief (proposed text and one-line rationale).

**Defaults:** Propose before editing (always). Full proposal style.

### Friction Log

- **Default severity** — Default severity level for new friction log entries when the user doesn't specify one.
- **Inference level** — How much to infer from context vs. asking. Ranges from "infer what you can, ask about the rest" to "ask about everything explicitly."

**Defaults:** No default severity (always ask or infer from context). Infer what you can.

### General Preferences

- **Verbosity** — How much explanation to provide during operations. Ranges from verbose (explain reasoning, narrate steps) to terse (results only, minimal narration).
- **Explanation style** — Whether to lead with context or lead with action. "Context first" explains why before showing what; "action first" shows the result then explains if asked.

**Defaults:** Moderate verbosity. Context first.

### Tracing

Runtime tracing logs the LLM's decisions during real work sessions — which documents it read, what directives it found, what it decided and why. Useful for debugging unexpected behavior, understanding how docs interact, and verifying that the framework's tools work as intended.

**Trace level:**

- **Off** — No tracing. Default.
- **Standard** — Log major decisions: which docs read, what directives found, what was decided, and why. Enough to reconstruct the decision chain without cluttering the session.
- **Detailed** — Log everything including routine operations, alternatives considered, and directives that were read but didn't apply. Produces verbose output.
- **Custom** — User writes natural language describing exactly what to trace. Examples: "Detailed for maintenance decisions, standard for everything else" or "Only trace when reading intent files." The LLM interprets the description and applies judgment about what to log.

**Trace output:** `reference/sessions/trace-YYYY-MM-DD.md`. One file per day; if a trace file already exists for today, append with a session separator.

**Trace format:** Default format for trace entries. Users can override by creating `config/trace-format.md`. If that file exists, use its format instead.

Default trace entry format:

```
### [HH:MM] Decision Point

**Context:** [What was happening — which skill, what step]
**Read:** [Document path and section]
**Directive found:** [The relevant instruction, quoted or paraphrased]
**Decision:** [What was decided]
**Reasoning:** [Why — especially when judgment was applied]
```

For standard level, include only entries where a meaningful decision was made. For detailed level, include every document read and every directive evaluated.

**Observer effect:** Tracing changes behavior. The act of logging decisions consumes context window and may cause the LLM to reason more deliberately than it would untraced. At standard level this is minor. At detailed level it is significant — sessions will be slower and the LLM may reason differently. This is inherent to any introspective system and is not a bug, but users should be aware that traced sessions are not perfectly representative of untraced sessions.

**Performance:** Overhead scales with level. Standard adds modest context usage and minor latency. Detailed can substantially increase both. Custom depends on what's being traced. For routine debugging, standard is recommended. Use detailed for targeted sessions, not as an always-on setting.

**Defaults:** Tracing off. Default format as specified above.

---

## Constraints

- The grounding principles in `CLAUDE.md` are not configurable. "The human decides," "judgment over rules," and other core principles are architectural, not preferences.
- The approval gate (propose before editing) in maintenance mode can be relaxed but not disabled entirely — at minimum, structural changes must be proposed.
- Skill behavior can be tuned but not fundamentally altered. Config adjusts how a skill works, not what it does.

---

## Guidance for the Config Conversation

When users aren't sure what to configure, start with `/create-app` behavior and general verbosity. These have the most visible effect on day-to-day use.

For first-time users, suggest trying the defaults first and coming back to `/preferences` after they've used the framework a few times. Configuration is most useful when you know what you want to change.

---

*This spec is maintained by the framework developer via `/maintain`. Users interact with config through `/preferences`.*
