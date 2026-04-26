---
name: pm-skills:make-decision
description: Turn a fuzzy tradeoff into a concrete decision memo.
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
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context only.
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
- Follow `examples/output.md` as the canonical output template.
- Match its title format, decision line, numbered section headings, criteria-first table, and recommendation style.
- The options section must include a criteria-first Markdown table.
- Each option cell must start with exactly one traffic-light marker, then a rating, then a short rationale.
- Use this pattern exactly: `:green_circle: High. Context`, `:yellow_circle: Medium. Context`, or `:red_circle: Low. Context`
- In rendered output, those markers may appear as `🟢`, `🟡`, or `🔴`. That is fine.
- `:green_circle:` means favorable on that criterion, `:yellow_circle:` means mixed or uncertain, and `:red_circle:` means unfavorable.
- In decision memo mode, phrase the recommendation as the documented decision.
- In decision worksheet mode, state the best current recommendation directly and name what could change it.
- The recommendation must state the preferred option directly and name the main downside or open risk.
- Never invent facts, dates, constraints, stakeholder views, or metrics.

# Output

A compact decision memo with background, options, a comparison table, and a direct recommendation.

# Examples

Use `examples/output.md` as the formatting source of truth.
