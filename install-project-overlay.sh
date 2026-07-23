#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-}"
if [ -z "$TARGET" ]; then
  echo "Usage: $0 /path/to/project"
  exit 1
fi
SOURCE="$(cd "$(dirname "$0")" && pwd)/project-overlay/.github"
DEST="$TARGET/.github"
mkdir -p "$DEST"
cp -Rn "$SOURCE/." "$DEST/"
echo "Installed project overlay into $DEST"
echo "Now customize copilot-instructions.md, instructions/, skills/, and PROJECT-GUARDRAILS.md"
