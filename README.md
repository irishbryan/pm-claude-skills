# PM Tools for Claude Code

**Simple status updates using Claude Code.** Type `/team-status`, get Slack-ready output

## Install & Uninstall

```bash
# Install
git clone <repo-url> pm-claude-skills && cd pm-claude-skills && script/setup

# Uninstall
script/uninstall
```

Setup asks for your name, email, teams, and optional integrations (Granola, Notion).

## Usage

| Command | What You Get |
|---------|-------------|
| `/team-status [period]`<br/>*Example: `/team-status last week`* | **Shipped**<br/>• [Project A](url): Feature X launched, metrics improved 20%<br/>• [Project B](url): Integration complete<br/>**In Progress**<br/>• [Project C](url): Design review in progress<br/>**Blocked**<br/>• [Project D](url): Waiting on vendor decision |
| `/my-status [period]`<br/>*Example: `/my-status since Monday`* | **PROGRESS**<br/>🟢 Feature shipped — achieved 95% success rate<br/>🟡 Decision doc in progress — need stakeholder review<br/>**NEXT**<br/>• Complete roadmap planning by Friday<br/>**RISKS**<br/>• Vendor contract negotiations stalled |
| `/meeting-digest [topic]`<br/>*Example: `/meeting-digest partnership`* | **tl;dr:** Partnership agreement on technical integration approach<br/>**Key Points:**<br/>1. Technical framework selected<br/>2. Integration timeline finalized<br/>**Action Items:**<br/>• Partner: Share technical docs<br/>• You: Schedule follow-up call |

**Customize:** Edit `~/.claude/pm-claude-skills.local.md` to change teams or preferences.
