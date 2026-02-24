# PM Tools for Claude Code

Simple status updates using Claude Code. Works with Linear, Granola, and Notion. Type `/team-status`, get Slack-ready output.

<p align="center">
  <img width="600" alt="PM Tools Overview" src="https://github.com/user-attachments/assets/d6cfc988-1056-4a23-962a-90e5c31852a0" />
</p>

## Install

**Prerequisites:** [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code/overview)

```bash
git clone <repo-url> pm-claude-skills && cd pm-claude-skills && script/setup
```

`script/setup` personalizes a private context file. Then open Claude Code and type `/mcp` to connect your tools. 

```
/my-status for last week
```

## Commands

| | |
|---------|-------------|
| 📊 `/team-status` | What your team shipped, what's in progress, what's blocked |
| 👤 `/my-status` | Your progress, upcoming work, and risks |
| 🤝 `/meeting-digest` | Meeting summary with key points and action items |

💡 All outputs are Slack-ready — just copy and paste

---

**Customize:** `~/.claude/pm-claude-skills.local.md` • **Uninstall:** `script/uninstall`
