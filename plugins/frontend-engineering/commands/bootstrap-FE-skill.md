---
name: bootstrap-FE-skill
description: Discover and bootstrap relevant community frontend engineering skills from approved upstream sources.
---
# Bootstrap Frontend Engineering Community Skills
1. Inspect the project and existing toolkit capabilities.
2. Identify frontend capability gaps.
3. Read `community/sources.json`.
4. Discover relevant upstream resources and prefer original sources.
5. Show name, purpose, source, license when available, and proposed destination.
6. Require explicit developer confirmation.
7. Install only approved resources using supported mechanisms.
8. Preserve upstream licensing and attribution.
9. Report installed, skipped, and changed resources.

Prioritize React, TypeScript, testing, accessibility, performance, architecture,
code review, dependency management, security, design systems and DX.

Do not silently install resources, execute unknown downloaded scripts, overwrite
existing skills, remove notices, modify organization policy, or promote community
content into Layer 1 without explicit approval.

## v2.3 Project Initialization

Before discovering community resources, determine whether the current
repository has already been initialized for the Frontend Engineering Toolkit.

### Project Detection

Detect:

- Framework (React, Next.js, Angular, Vue, etc.)
- Language (TypeScript / JavaScript)
- Build tool (Vite, Webpack, Turbopack, etc.)
- Package manager
- Existing `.github/copilot` configuration

### Project Initialization

If `.github/copilot` does not exist:

- Create the project overlay structure.
- Create `.github/copilot/project-policy.json`.
- Create a default project overlay using the detected framework.
- Do not overwrite existing files without explicit approval.

### Community Standards

If Policy Packs are available:

- Discover `policy-packs/registry.json`.
- List available Policy Packs.
- Recommend relevant packs based on the detected project.
- Require explicit developer approval before enabling any Policy Pack.
- Record approved Policy Packs in `project-policy.json`.

### Existing Projects

If the project has already been initialized:

- Validate the existing overlay.
- Validate `project-policy.json`.
- Report missing or outdated configuration.
- Never overwrite existing configuration without approval.
