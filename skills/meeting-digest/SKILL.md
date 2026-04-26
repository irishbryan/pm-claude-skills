---
name: pm-skills:meeting-digest
description: Summarize recent meetings and extract decisions and action items.
---

# Purpose

Pull the highest-signal takeaways out of recent meetings so a PM can quickly share what matters.

# When to use

- After a staff meeting
- After a project sync
- After a roadmap or decision review

# Inputs

- Optional topic or date range
- Optional meeting title or project scope
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context only.
- Required tool: Granola.
- If Granola is unavailable, say: `Granola is not connected for pm-skills in this agent yet. Connect it, then rerun pm-skills:meeting-digest.`
- Use the user input as a topic, date, or meeting filter when provided.
- If the user gives an exact title or narrow filter, digest that meeting.
- If multiple plausible meetings match, ask the user to narrow before summarizing.
- If no meeting matches, say no matching Granola meeting was found and ask for a tighter title, date, or topic.
- Extract only the highest-signal details:
  - one concrete `tl;dr`
  - decisions made
  - discussion context needed to understand decisions, risks, disagreements, or open questions
  - action items with owners and next steps when available
- A decision is a choice, agreement, approval, deferral, rejection, or explicit change in direction.
- Include discussion summary items only when they explain what changed, what matters, or what remains unresolved.
- Include action items only when the notes contain explicit or strongly implied follow-up work.
- If an action item's owner or timing is strongly implied by the notes, infer lightly.
- If an action item's owner or timing is missing, say what is missing in the item.
- Never invent attendees, decisions, action items, owners, dates, or metrics beyond what the meeting notes support.
- Do not include Granola citation links.
- Keep the output brief, high-signal, and Slack-ready.
- Follow `examples/output.md` as the canonical output template.
- Match its title format, `tl;dr` line, italic optional section headings, numbered list style, and bold-first-sentence item pattern.
- Treat `Decisions Made`, `Discussion Summary`, and `Action Items` as optional sections.
- Omit optional sections that are not supported by the meeting notes.
- Do not include empty sections or filler like `None`.
- Use numbered lists under optional sections.
- Each list item must follow this pattern: `1. **Concise statement.** Short supporting context.`
- Keep each bold first sentence concrete, standalone, and ideally under 10 words.
- Do not bold the whole list item.
- Keep the full answer to 150 words or less, and prefer 75-120 words.

# Output

A short meeting digest with a title, one `tl;dr`, and only the decision, discussion, and action sections supported by the meeting notes.

# Examples

Use `examples/output.md` as the formatting source of truth.
