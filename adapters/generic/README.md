# Generic Adapter Notes

This repo keeps the shared PM skill instructions and templates in `plugins/pm-skills/skills`.

For a new agent integration:

1. Reuse the existing skill names:
   - `pm-skills:team-status`
   - `pm-skills:my-status`
   - `pm-skills:meeting-digest`
   - `pm-skills:slack-recap`
   - `pm-skills:make-decision`
2. Read the shared `instructions.md` and template file from the matching skill directory.
3. Map optional integrations by capability, not by hardcoded product choice:
   - Linear for `team-status` and `my-status`
   - Granola for `meeting-digest`, optional for status skills
   - Notion optional for `team-status`
   - Slack for `slack-recap`
4. Read user profile context from `~/.config/pm-skills/profile.md`.
5. If a required integration is missing, stop and print the skill's setup message instead of guessing.
