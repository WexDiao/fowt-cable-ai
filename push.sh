#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

echo -e "${GREEN}=== fowt-cable-ai push ===${NC}"

# Check remote origin is configured
if ! git remote get-url origin &>/dev/null; then
  echo -e "${RED}[ERROR] No remote origin found.${NC}"
  echo "Run this once to connect your GitHub repo:"
  echo "  git remote add origin https://github.com/WexDiao/DailyNotes.git"
  exit 1
fi

# Show what changed
STATUS=$(git status --short)
if [ -z "$STATUS" ]; then
  echo -e "${YELLOW}Nothing to commit. Already up to date.${NC}"
  exit 0
fi

echo "$STATUS"
echo ""

# Stage all (_local/ is gitignored, PDFs and raw data are skipped automatically)
git add -A

# Commit message (default: today's date)
DEFAULT_MSG="update: $(date +%Y-%m-%d)"
read -rp "Commit message [$DEFAULT_MSG]: " MSG
MSG="${MSG:-$DEFAULT_MSG}"

git commit -m "$MSG"

# Push
BRANCH=$(git rev-parse --abbrev-ref HEAD)
git push origin "$BRANCH"

echo -e "${GREEN}Done — pushed to GitHub (branch: $BRANCH)${NC}"
