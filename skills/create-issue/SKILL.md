---
name: pm-skills:create-issue
description: Create a clear issue from a vague bug, task, feature request, or follow-up, with context, done criteria, scope, and next steps.
---

# Purpose

Help a PM write a clear, self-contained issue that gives enough context for anyone to pick it up and deliver without a handoff conversation.

# When to use

- Filing a bug or feature task in a tracker
- Turning a conversation or decision into concrete next work
- Writing work items that will be picked up by someone else
- Breaking a larger initiative into executable pieces

# Inputs

- The problem or task
- Why it matters now
- Optional suggested approach
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as task evidence or a replacement for asking the user.
- This skill is conversational. Do not jump straight to the final issue unless the user explicitly asks to fast-track.
- Optional tool: Linear. If Linear is available, offer to create the issue after the user approves the draft.
- Run a short interview in four phases:
  - clarify the problem and why it matters now
  - define what done looks like
  - optionally surface a suggested approach while preserving creative freedom
  - set boundaries and out of scope
- Ask one or two questions at a time.
- Push back on vague problem statements, missing context, and acceptance criteria that cannot be verified.
- A suggested approach is a starting point, not a mandate. The person picking up the issue has creative freedom on implementation.
- If the user has no suggested approach, omit the `Suggested Approach` section entirely.
- If the user wants to fast-track, ask for the problem, why it matters, what done looks like, and what is out of scope.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` that states the problem and needed outcome.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with sequential numbered section headings: `The Problem`, `What Done Looks Like`, optional `Suggested Approach`, and `Out of Scope`.
- If `Suggested Approach` is omitted, renumber the remaining sections sequentially.
- Use hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Include `Suggested Approach` only when the user provides one.
- Use a short paragraph when a section contains one coherent point. When a section needs multiple distinct points, use a numbered list to make the issue easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Keep the full issue to 300 words or less.
- Never invent facts the user did not provide.

# Output

A shaped issue that is specific enough to file in a tracker and clear enough for someone to start work without a handoff conversation.
