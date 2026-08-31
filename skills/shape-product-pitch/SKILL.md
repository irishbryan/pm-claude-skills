---
name: pm-skills:shape-product-pitch
description: Shape a product idea into a concise pitch with problem, solution, appetite, constraints, success signals, risks, and out-of-scope items.
---

# Purpose

Help a PM turn a vague idea into a strong pitch with a clear problem, proposed solution, appetite, and boundaries.

# When to use

- Before betting or prioritization
- After the problem is framed and a direction needs pitching
- When pressure-testing whether an idea is worth shaping

# Inputs

- The problem to solve
- Target user or customer segment
- Optional timing context when it materially changes the pitch
- Proposed solution or direction
- Additional background or reader context, only when needed to understand the pitch
- Appetite, constraints, or desired scope
- Success signal
- Out-of-scope items
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as customer evidence or product strategy.
- This skill is conversational. Do not jump straight to a finished pitch unless the user explicitly asks to fast-track.
- No tools are required.
- Run a short interview in four phases:
  - clarify the target user, problem, and current workaround
  - test assumptions, customer value, and any material timing context
  - define success, appetite, constraints, and non-goals
  - propose the solution and pressure-test risks or open questions
- Ask whether there is any additional background or context readers will need to understand the pitch.
- Ask one or two questions at a time.
- Push back on vague customer value, manufactured urgency, missing appetite, solution-first framing, and unbounded scope.
- If the user wants to fast-track, ask for the target user, problem, proposed solution, additional context, appetite, success signal, constraints, out-of-scope items, and any material timing context.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` that connects the problem, proposed direction, and intended value.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with sequential numbered section headings: `The Problem`, `The Solution`, `What Success Looks Like`, optional `Risks and Open Questions`, and `Out of Scope`.
- If an optional section is omitted, renumber the remaining sections sequentially.
- Integrate material timing context into the `tl;dr` or `The Problem` only when it changes the pitch. Do not create a standalone `Why Now` section or label, and do not manufacture urgency when none exists.
- Start `The Solution` with the proposed approach in plain text. Put constraints under a genuine hierarchically numbered `Constraints` subheading when they are needed; do not use a bold label as a substitute heading.
- Use other hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Treat appetite as a default constraint, not a separate section.
- Integrate essential background into the most relevant numbered section rather than creating an `Additional Context` section.
- Include `Risks and Open Questions` only when there are meaningful risks, unresolved dependencies, or validation gaps.
- Use a short paragraph when a section contains one coherent point. When a section needs multiple distinct points, use a numbered list to make the pitch easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Keep the full pitch to 500 words or less.
- Never invent facts, metrics, customers, dates, constraints, or stakeholder views.

# Output

A shaped pitch that is specific enough to discuss in planning, betting, or review without turning into a full product spec.
