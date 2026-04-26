---
name: pm-skills:create-issue
description: Turn a rough task into a well-shaped issue anyone can pick up and execute.
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
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context only.
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
- Follow `examples/output.md` as the canonical output template.
- Match its title format, `tl;dr` blockquote, section headings, numbered list style, and bold-first-sentence item pattern.
- Include `Suggested Approach` only when the user provides one.
- Every list item must start with a bold, concrete first sentence on the same line as the supporting detail.
- Use numbered lists.
- Keep the full issue to 300 words or less.
- Never invent facts the user did not provide.

# Output

A shaped issue that is specific enough to file in a tracker and clear enough for someone to start work without a handoff conversation.

# Examples

Use `examples/output.md` as the formatting source of truth.
