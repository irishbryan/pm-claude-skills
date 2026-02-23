# PM Tools for Claude Code

Simple status updates using Claude Code. Works with Linear, Granola, and Notion. Type `/team-status`, get Slack-ready output.

<p align="center">
  <img width="600" alt="PM Tools Overview" src="https://github.com/user-attachments/assets/39222af1-c639-4999-9af1-7f318843f666" />
</p>

## Install

**Prerequisites:** [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code/overview)

```bash
git clone <repo-url> pm-claude-skills && cd pm-claude-skills && script/setup
```

Setup asks for your name, email, and teams. Then open Claude Code, type `/mcp` to connect Linear/Granola, and try:

```
/pm-claude-skills:my-status for last week
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
