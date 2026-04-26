---
name: pm-skills:shape-product-pitch
description: Turn a rough idea into a shaped product pitch.
---

# Purpose

Help a PM turn a vague idea into a strong pitch with a clear problem, proposed solution, appetite, and boundaries.

# When to use

- Before betting or prioritization
- When framing a new initiative
- When pressure-testing whether an idea is worth shaping

# Inputs

- The problem to solve
- Target user or customer segment
- Why now
- Proposed solution or direction
- Appetite, constraints, or desired scope
- Success signal
- Out-of-scope items
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context only.
- This skill is conversational. Do not jump straight to a finished pitch unless the user explicitly asks to fast-track.
- No tools are required.
- Run a short interview in four phases:
  - clarify the target user, problem, and current workaround
  - test assumptions, customer value, and urgency
  - define success, appetite, constraints, and non-goals
  - propose the solution and pressure-test risks or open questions
- Ask one or two questions at a time.
- Push back on vague customer value, weak urgency, missing appetite, solution-first framing, and unbounded scope.
- If the user wants to fast-track, ask for the target user, problem, why now, proposed solution, appetite, success signal, constraints, and out-of-scope items.
- Follow `examples/output.md` as the canonical output template.
- Match its title format, `tl;dr` blockquote, section headings, numbered list style, and bold-first-sentence item pattern.
- `The Solution` must include a `**Constraints:**` list.
- Treat appetite as a default constraint, not a separate section.
- Include `## Risks and Open Questions` only when there are meaningful risks, unresolved dependencies, or validation gaps.
- Every list item must start with a bold, concrete first sentence on the same line as the supporting detail.
- Keep each bold first sentence concrete, standalone, and ideally under 10 words.
- Do not bold the whole list item.
- Use numbered lists.
- Keep the full pitch to 500 words or less.
- If no meaningful urgency exists, say so directly.
- Never invent facts, metrics, customers, dates, constraints, or stakeholder views.

# Output

A shaped pitch that is specific enough to discuss in planning, betting, or review without turning into a full product spec.

# Examples

Use `examples/output.md` as the formatting source of truth.
