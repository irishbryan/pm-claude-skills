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
- Why now
- Appetite, constraints, or desired scope
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context only.
- This skill is conversational. Do not jump straight to a finished pitch unless the user explicitly asks to fast-track.
- No tools are required.
- Run a short interview in four phases:
  - clarify the problem
  - test assumptions and urgency
  - define success and appetite
  - propose a solution and pressure-test it
- Ask one or two questions at a time.
- Push back on vague problem statements, weak urgency, and missing constraints.
- If the user wants to fast-track, ask for the problem, urgency, appetite, what success looks like, and what is out of scope.
- Follow this output shape exactly:
  - `# {Pitch Title}`
  - `> **tl;dr:** ...`
  - `## The Problem`
  - `## The Solution`
  - `## What Success Looks Like`
  - `## Out of Scope`
- `The Solution` must include constraints and appetite.
- Every list item must start with a bold, concrete first sentence on the same line as the supporting detail.
- Use numbered lists.
- Keep the full pitch to 500 words or less.
- If no meaningful urgency exists, say so directly.
- Never invent facts the user did not provide.

# Output

A shaped pitch that is specific enough to discuss in planning, betting, or review without turning into a full product spec.

# Examples

See `examples/output.md`.
