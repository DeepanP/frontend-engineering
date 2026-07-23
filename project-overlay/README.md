# Layer 3 — Project Overlay

This directory is intentionally separate from the reusable marketplace plugin.

Its actual Copilot repository configuration is under the hidden `.github/` directory.

## Install into a project

macOS/Linux:

```sh
cp -Rn .github /path/to/your/project/
```

Or use the root `install-project-overlay.sh`.

After copying, customize:
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- `.github/skills/project-context/SKILL.md`
- `.github/skills/domain-rules/SKILL.md`
- `.github/PROJECT-GUARDRAILS.md`

This layer should evolve per project.
