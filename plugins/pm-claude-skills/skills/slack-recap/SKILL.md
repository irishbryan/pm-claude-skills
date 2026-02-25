---
name: slack-recap
description: >
  Recap important Slack messages you need to action. Use when asked for
  "slack recap", "slack catch-up", "important slack messages", "slack inbox",
  or "actionable slack messages".
allowed-tools:
  - mcp__claude_ai_Slack__*
---

## PM Guidance
- You are assisting a Product Manager. Prioritize clarity, data, and stakeholder communication.
- Output style: BLUF (Bottom Line Up Front), Slack-ready, no fluff.
- Never fabricate Slack message data — only use real data from the API.
- If a section has no data, write "None found" — don't omit the section.
- Time format: "2h ago", "Yesterday", "Mon DD" (e.g., Feb 22).
- Read ~/.claude/pm-claude-skills.local.md for personal context (Slack workspace, key channels, stakeholders).

## Instructions

**TEMPLATE ENFORCEMENT**: You MUST read and follow `@templates/slack-recap-template.md` EXACTLY. The template defines the required format with four urgency sections. Do not deviate from this structure.

### 1. Load Context
- Read `~/.claude/pm-claude-skills.local.md` for user context (Slack workspace, key channels, stakeholders)
- Default time period: last 7 days (override with `$ARGUMENTS`)
- Check Slack MCP connection — if unavailable, display setup instructions with link to https://mcp.slack.com

### 2. Search Strategy

**Critical Note**: Slack does NOT provide API access to "saved for later" / "Later" items. Instead, use intelligent search queries to identify high-signal messages:

Execute multiple Slack searches to gather comprehensive results:
1. `mentions:@me after:{N}d` — messages where you were mentioned
2. `mentions:@me has:reaction after:{N}d` — high-engagement mentions
3. `(urgent OR asap OR blocker OR "decision needed") mentions:@me after:{N}d` — urgency keywords
4. `from:@me after:{N}d` — messages YOU sent (high signal for follow-ups)
5. `from:@me has:reaction after:{N}d` — your messages that got engagement
6. `from:@me has:thread after:{N}d` — your messages with thread replies
7. `from:{key_stakeholder} after:{N}d` — messages from leadership/key people (if configured)
8. `in:{key_channel} has:reaction after:{N}d` — high-engagement in key channels (if configured)

Combine results, deduplicate by message timestamp/ID, then score and categorize.

### 3. Urgency Scoring Algorithm

Categorize each message using the following criteria:

**🔴 URGENT (Act Today):**
- Contains: "urgent", "asap", "emergency", "blocker", "broken"
- From CEO/VP/key stakeholder in last 24 hours
- Explicit deadline today
- Direct question to user requiring immediate response
- **Your sent message**: Question you asked >24h ago with new thread replies (needs follow-up)

**🟡 ACTION NEEDED (This Week):**
- Contains: "decision needed", "needs approval", "can you", "please review"
- @mentions with asks or questions
- Follow-up requests in threads where user participated
- Deadlines within current week
- **Your sent message**: Request/question with 3+ reactions or thread activity (awaiting response)
- **Your sent message**: Contains "?" and has replies (your question got answered)

**🟠 FOR REVIEW:**
- 5+ reactions indicating high engagement
- Strategic keywords: "RFC", "launch", "roadmap", "announcement"
- In user's key channels (from config)
- Thread discussions with significant activity (10+ messages)
- **Your sent message**: Announcement/update with 5+ reactions (high engagement on your content)

**🟢 FYI:**
- General updates in followed channels
- Lower priority mentions
- Informational announcements
- 3-4 reactions (moderate engagement)
- **Your sent message**: Standard updates with 1-2 reactions (acknowledged but low priority)

### 4. Message Formatting

For each message:
- **Sender**: Extract user's display name or real name
- **Channel**: Include channel name (use DM indicator for direct messages)
- **Snippet**: First 15 words of message text, truncated at word boundary
- **Link**: Slack permalink (ensure it's valid)
- **Time**: Format as "2h ago" (<1h), "5h ago" (<24h), "Yesterday", "Mon" (this week), "Feb 18" (older)
- **Thread indicator**: Add "↪️ Thread (N msgs)" if message has replies

Strip markdown formatting and sanitize sensitive content (credentials, PII).

### 5. Build Output Sections

Follow the template format EXACTLY:
- Four sections in order: URGENT, ACTION NEEDED, FOR REVIEW, FYI
- Numbered lists (1., 2., 3.) within each section
- Format: **{Sender}** in #{channel} — {snippet} ([link]) · {time}
- Max 5 items per section (prioritize by score within category)
- Empty sections: Write "None found"

### 6. Quality Gates

Before outputting:
- Total output: ≤300 words
- All Slack permalinks are valid
- All four sections present
- Health indicators (🔴🟡🟠🟢) match urgency
- No fabricated data or placeholder content
- Scannable format with clear action hierarchy

## Error Handling

- **No Slack MCP**: "⚠️ Slack MCP not connected. Set up at https://mcp.slack.com"
- **No messages found**: "No important messages in the last {period}"
- **Missing channel access**: "Need access to #{channel} — contact your Slack admin"
- **Rate limits**: Show partial results with notice: "⚠️ Rate limited — showing partial results"
- **Search errors**: Fall back to simpler queries (just mentions) and note limitations

## Future Enhancement Path

When Slack MCP adds bookmark/saved message support, update to use:
- `mcp__claude_ai_Slack__get_bookmarks` (if/when available)
- `mcp__claude_ai_Slack__get_saved_items` (if/when available)

For now, the search-based approach is the only viable option given Slack API limitations.
