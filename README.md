# PM Tools for Claude Code

**Simple status updates using Claude Code.** Type `/team-status`, get Slack-ready output

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/39222af1-c639-4999-9af1-7f318843f666" />

## Install

**Prerequisites:** [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code/overview) must be installed first.

**Steps:**
1. **Clone the repository**
   ```bash
   git clone <repo-url> pm-claude-skills
   cd pm-claude-skills
   ```

2. **Run setup script** (asks for your name, email, teams, and optional integrations)
   ```bash
   script/setup
   ```

3. **Open Claude Code**
   ```bash
   claude
   ```

4. **Connect MCP servers** (Linear, Granola, etc.)
   ```
   /mcp
   ```
   Follow the browser prompts to authenticate each service.

5. **Try it!**
   ```
   /pm-claude-skills:my-status for last week
   ```

**Uninstall:** Run `script/uninstall` from the repo directory.

## Usage

| Command | What You Get |
|---------|-------------|
| 📊 `/pm-claude-skills:team-status last week` | **Shipped** → **In Progress** → **Blocked**<br/>Clean rollup of what your team shipped, what's moving, what's stuck |
| 👤 `/pm-claude-skills:my-status since Monday` | 🟢🟡🔴 **PROGRESS** → **NEXT** → **RISKS**<br/>Your personal wins, upcoming work, and what needs help |
| 🤝 `/pm-claude-skills:meeting-digest partnership` | **tl;dr** + **Key Points** + **Action Items**<br/>Instant recap ready to post in Slack |

💡 **All outputs are Slack-ready** — just copy and paste

**Customize:** Edit `~/.claude/pm-claude-skills.local.md` to change teams or preferences.
