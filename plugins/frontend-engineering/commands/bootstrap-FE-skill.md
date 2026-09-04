---
name: bootstrap-FE-skill
description: Initialize the Frontend Engineering Toolkit for the current repository and optionally discover and install approved community resources.
---

# Bootstrap Frontend Engineering Toolkit

1. Detect the current project.
2. Initialize `.github/copilot` if required.
3. Validate the existing toolkit configuration.
4. Discover optional community resources.
5. Require developer approval before installing optional resources.

## Phase 1 - Project Detection

Detect:
- Framework
- Language
- Package manager
- Build tool
- Existing `.github/copilot`

## Phase 2 - Project Initialization

If `.github/copilot` does not exist create:

.github/copilot/
- project-policy.json
- project-overlay/
- prompts/
- README.md

Never overwrite existing files without approval.

## Phase 3 - Community Discovery

Read `community/sources.json`.

Discover approved:
- Skills
- Agents
- Hooks
- Policy Packs

Show:
- Name
- Purpose
- Source
- License
- Destination

Require approval before installation.

## Phase 4 - Validation

Validate:
- project-policy.json
- project-overlay
- toolkit configuration

## Safety

Never silently install resources, overwrite configuration, execute downloaded scripts or modify application source code.
