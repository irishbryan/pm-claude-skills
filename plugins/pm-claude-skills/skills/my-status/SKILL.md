---
name: my-status
description: >
  Generate your personal status update from Linear. Use when asked for "my
  status", "what am I working on", "my weekly update", "1:1 prep",
  "what did I do this week", or "personal status".
allowed-tools:
  - mcp__linear__*
---

## PM Guidance
- You are assisting a Product Manager. Prioritize clarity, data, and stakeholder communication.
- Output style: BLUF (Bottom Line Up Front), Slack-ready, no fluff.
- Never create or modify Linear issues unless explicitly asked.
- Never fabricate Linear issue identifiers — only use real data from the API.
- If a section has no data, write "None this period" — don't omit the section.
- Date format: Mon DD (e.g., Feb 22).
- Read ~/.claude/pm-claude-skills.local.md for personal context (name, email, focus areas, and any additional config).

## Instructions

**TEMPLATE ENFORCEMENT**: You MUST read and follow `@templates/my-status-template.md` EXACTLY. The template defines the required format with three sections: PROGRESS, NEXT, and RISKS/ASKS. Do not deviate from this structure.

### 1. Load Context
- Read `~/.claude/pm-claude-skills.local.md` for user context (name, email, focus areas, team preferences)
- Check if teams are specified in config; if not, query Linear to discover user's teams
- Default time period: last 7 days (override with `$ARGUMENTS`)
- Note: For personal status, include work you're coordinating across your team(s), not just issues assigned to you

### 2. Gather Data from Multiple Sources

**Linear (broad project view):**
- Get user's teams using list_teams (include both public AND private teams), then:
  - Query all projects on user's team(s) to understand team-level work
  - For each active project, get recent issues to understand project status
- Issues assigned to user (completed, in-progress, blocked, backlog with recent updates)
- Issues user created (shows what you initiated/coordinated)
- Query by project to get all issues in projects you're involved in (not just assigned to you)
- Use list_projects with recent updates to see what's moving across your area
- Cast a wide net: You're a PM, so include work you're coordinating even if not directly assigned
- Query multiple times if needed to get full picture of your scope
- **Important**: Some users track tasks in private teams — ensure private teams are included in all queries

**Granola (strategic context):**
- Query for "decisions made, action items, and key outcomes from meetings in last [N] days"
- Query for "current blockers, ongoing issues, and problems discussed in meetings"
- Query for "upcoming milestones, deadlines, and meetings scheduled"
- Use context to enrich the report but do NOT include Granola citation links (they are private)

### 3. Build PROGRESS Section
For each completed/progressing item:
- **Health indicator**: Assess status and add emoji prefix:
  - 🟢 = shipped/on track
  - 🟡 = in progress with caveats/unknowns
  - 🔴 = blocked/user-impacting issue
- **Headline**: Outcome-focused, link to Linear project when applicable
- **Context**: One-liner with specific details (percentages, dates, next steps, review status)
- **Evidence**: Include Slack thread links when relevant (but NOT Granola citation links as they are private)
- Include items from both Linear AND Granola (completed work, alignment progress, shipped features, ongoing issues)

### 4. Build NEXT Section
Structure as specific upcoming actions, not just in-progress issues:
- Upcoming meetings/milestones from Granola
- Decisions that need to be made (with your stated preferences if mentioned in meetings)
- In-progress Linear work
- Follow-up categories (e.g., "Offsite follow ups")
- Include user's opinions/recommendations from meeting notes (e.g., "my vote: yes")

### 5. Build RISKS/ASKS Section
For each risk or ask:
- **Prefix**: Start with **RISK:** or **ASK:**
- **Concern**: State the specific risk or ask
- **Mitigation**: If user mentioned mitigation strategy in meetings, include it (e.g., "I'll align w/ Sebastian")
- **Context**: Who's involved, when decision needed
- Query Granola specifically for strategic risks beyond just blocked Linear issues

### 6. Format Requirements
**CRITICAL**: Follow `@templates/my-status-template.md` EXACTLY:
- Use ONLY these three sections in this order: ## PROGRESS, ## NEXT, ## RISKS/ASKS
- Use numbered lists (1., 2., 3.) within each section, NOT headers or bullet points
- Each item: one line preferred, two lines max
- Max 5-6 items per section (this is a manager-level overview)
- Group by project when possible
- Link project names (not individual issues) when applicable
- Total output: ≤250 words (increased from 200 to accommodate detail)
- Format: Slack-ready, scannable, BLUF style
- Focus on outcomes and impact, not issue IDs
- Do NOT add extra sections like "Work Summary", "Strategic Planning", etc.
