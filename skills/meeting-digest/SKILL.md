---
name: pm-skills:meeting-digest
description: Summarize meeting notes into a brief digest with decisions, discussion context, action items, owners, and open questions.
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
- Optional source material, such as pasted notes, transcript excerpts, or meeting summaries
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as meeting evidence.
- Preferred tool: Granola.
- Use Granola when connected; otherwise ask the user to paste meeting notes or a transcript excerpt.
- Use the user input as a topic, date, or meeting filter when provided.
- If the user gives an exact title or narrow filter, digest that meeting.
- If multiple plausible meetings match, ask the user to narrow before summarizing.
- If no meeting matches, say no matching Granola meeting was found and ask for a tighter title, date, or topic.
- Extract only the highest-signal details:
  - one concrete summary
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
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` with the most important decision, change, blocker, or next action.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with supported sections from `Decisions Made`, `Discussion Context`, and `Action Items` as sequential numbered headings.
- Treat `Decisions Made`, `Discussion Context`, and `Action Items` as optional sections.
- Omit optional sections that are not supported by the meeting notes.
- Renumber the remaining sections sequentially when an optional section is omitted.
- Use hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Do not include empty sections or filler like `None`.
- Use a short paragraph when a section contains one coherent point. When a section needs multiple distinct points, use a numbered list to make the digest easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Keep the full answer to 150 words or less, and prefer 75-120 words.

# Output

A short meeting digest with a title, concrete `tl;dr`, and only the decision, discussion, and action sections supported by the meeting notes.
