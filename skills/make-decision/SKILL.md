---
name: pm-skills:make-decision
description: Create a concise decision memo for tradeoffs, recommendations, pros and cons, scope choices, strategy questions, or should-we-do-X decisions.
---

# Purpose

Help a PM clarify a decision, pressure-test the real options, and produce a memo that someone can paste into a working doc.

# When to use

- Strategy tradeoffs
- Scope decisions
- Architecture or tooling choices
- Policy decisions that need explicit reasoning

# Inputs

- Decision mode: documenting an already-made decision or creating a worksheet to drive one
- The decision to make
- Background and urgency
- Viable options
- Main criteria or constraints
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as decision evidence or stakeholder input.
- This skill is conversational. Do not generate the final memo immediately unless the user explicitly asks to fast-track.
- No tools are required.
- Run a short interview in four phases:
  - clarify whether this is a decision memo or decision worksheet
  - establish background and urgency
  - enumerate viable options
  - pressure-test criteria and recommendation
- Ask one or two questions at a time.
- A decision memo documents an essentially made decision for clarity.
- A decision worksheet helps stakeholders stop circling and reach a decision.
- Push back on fuzzy scope, fake options, weak urgency, criteria that would not change the choice, and unresolved disagreement hidden as alignment.
- Always include a status quo or defer option if the user has not named one.
- Require at least two viable options before drafting.
- If the user fast-tracks, ask for the decision mode, decision question, background, urgency, viable options, main criteria or constraints, and likely recommendation.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...`. In memo mode, state the decision and main downside; in worksheet mode, state the best current recommendation and key tradeoff.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with sequential numbered section headings: `Decision`, `Background`, `Options`, and `Recommendation`.
- Put the decision question inside `Decision`; do not leave it as an unheaded line before the numbered sections.
- Use hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Use a short paragraph when a section contains one coherent point. When a non-tabular section needs multiple distinct points, use a numbered list to make the decision easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- The options section must include a criteria-first Markdown table.
- Start each option cell with exactly one marker, the criterion's `High`, `Medium`, or `Low` level, and a short rationale: `:{color}_circle: {High|Medium|Low}. Context`. Rendered emoji are fine.
- Use color for favorability and the rating for the level of the named criterion. For desirable criteria such as value or confidence, map `High` to green and `Low` to red. For undesirable criteria such as risk, cost, effort, complexity, or delay, invert the mapping: `Low` is green and `High` is red. `Medium` is yellow in either direction.
- Decide whether more or less of a criterion is desirable before scoring it. Rephrase ambiguous criteria, and never choose a color mechanically from the rating word.
- Do not use yellow to hide missing information. Ask for the evidence or state a clearly provisional assumption.
- Check each table row for directionality and color consistency before writing the recommendation.
- In decision memo mode, phrase the recommendation as the documented decision.
- In decision worksheet mode, state the best current recommendation directly and name what could change it.
- The recommendation must state the preferred option directly and name the main downside or open risk.
- Never invent facts, dates, constraints, stakeholder views, or metrics.

# Output

A compact decision memo with background, options, a comparison table, and a direct recommendation.
