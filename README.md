# Frontend Engineering Copilot Marketplace

A GitHub Copilot plugin marketplace containing a reusable frontend engineering plugin plus organization and project overlays.

<p align="center">
  <img
    src="assets/frontend-engineering-logo.png"
    alt="Frontend Engineering Copilot Marketplace"
    width="700"
  />
</p>

<h1 align="center">Frontend Engineering Copilot Marketplace</h1>

<p align="center">
  An evolving open-source toolkit for agentic frontend engineering.
</p>

## Repository structure

```text
.github/plugin/marketplace.json       Marketplace manifest
plugins/frontend-engineering/         Installable Copilot plugin
organization-policy/                  Layer 2 organization standards/templates
project-overlay/.github/              Layer 3 project-specific starter configuration
community-skills/                     Optional community-skill guidance
```

## 1. Add this repository as a marketplace

After pushing this repository to GitHub:

```sh
copilot plugin marketplace add OWNER/REPO
```

Verify:

```sh
copilot plugin marketplace list
copilot plugin marketplace browse frontend-engineering-marketplace
```

## 2. Install the plugin

```sh
copilot plugin install frontend-engineering@frontend-engineering-marketplace
```

Then verify inside Copilot:

```text
/plugin list
/agent
/skills list
```

## 3. Direct plugin test

Before testing the marketplace, you can validate the plugin itself:

```sh
copilot plugin install OWNER/REPO:plugins/frontend-engineering
```

Or from a local checkout:

```sh
copilot plugin install ./plugins/frontend-engineering
```

If direct install works but marketplace registration does not, inspect `.github/plugin/marketplace.json`.

## 4. Add project-specific Layer 3

From a local checkout:

```sh
./install-project-overlay.sh /path/to/your/project
```

This adds project-specific `.github/copilot-instructions.md`, path-specific instructions and project/domain skills.

## Three layers

**Layer 1 — Standard plugin:** reusable agents, skills and production guardrails.

**Layer 2 — Organization policy:** company engineering standards and policy templates.

**Layer 3 — Project overlay:** architecture, commands, domain rules and project-specific Copilot instructions.

## MCP

The plugin includes `.mcp.json.example` only. MCP remains optional so the plugin works without organization-specific server commands or credentials. When ready, configure approved MCP servers using GitHub Copilot's supported `.mcp.json` format and update `plugin.json` with the `mcpServers` field.

## Production note

Agent instructions/skills are behavioral guidance. Enforce critical controls using CI, branch protection, repository permissions, secret management, required human review and deployment approvals.

## Version management

Plugin releases now use semantic versioning with automated synchronization between the plugin manifest and marketplace entry.

```sh
python3 scripts/bump-plugin-version.py minor
python3 scripts/validate-plugin-version.py
python3 scripts/release-check.py
```

See `VERSIONING.md` and `CHANGELOG.md`.

GitHub Actions runs the version/source/structure checks whenever plugin, marketplace, release-script, or changelog files change.
