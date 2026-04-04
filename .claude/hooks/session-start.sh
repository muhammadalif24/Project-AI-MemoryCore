#!/bin/bash
# Matt Memory Core - Session Start Hook
# Ensures Claude loads Matt's identity at every session start
set -euo pipefail

# Only run in remote (Claude Code web) environment
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

exit 0
