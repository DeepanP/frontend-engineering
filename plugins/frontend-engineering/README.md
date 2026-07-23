# Layer 1 — Standard Plugin

Install:

```sh
copilot plugin install ./layer-1-standard-plugin
```

Contains portable agents, skills, production guardrails and a lightweight session-start hook.

The MCP file is an example rather than active configuration so the plugin remains installable without organization-specific MCP commands or credentials.

Skills use GitHub Agent Skills `SKILL.md` frontmatter (`name` + `description`) so Copilot can discover them based on task relevance.
