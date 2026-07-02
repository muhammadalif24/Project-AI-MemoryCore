# Active Reminders
*Persistent reminders that survive session changes. Updated at session end.*

## Open
- **Register marketplace on new machines**: The plugin itself is now enabled via `.claude/settings.json` (committed, works automatically once you pull). But Claude Code's marketplace registry is per-machine, not per-repo. On any machine that hasn't used this repo's plugin before (e.g. first pull on Windows), run this **once**: `claude plugin marketplace add ./plugins` — then the already-enabled matt-skills plugin will activate automatically on the next session. No install step needed after that.

## Completed
<!-- Resolved reminders move here. Format: -->
- **Activate Skill Plugin** (completed 2026-07-02): Created `plugins/.claude-plugin/marketplace.json` (matt-skills wasn't a marketplace on its own, so it needed one to be installable), ran `claude plugin marketplace add ./plugins` and `claude plugin install matt-skills@matt-marketplace --scope project`. Plugin is now enabled via `.claude/settings.json` (committed to repo). One caveat remains — see Open section above.
