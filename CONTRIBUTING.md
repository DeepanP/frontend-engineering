# Contributing to Frontend Engineering Copilot Marketplace

Thank you for contributing. This project explores reusable GitHub Copilot agents, skills, guardrails, and orchestration for frontend engineering.

## Contributions Welcome

We especially welcome improvements in React, TypeScript, frontend architecture, Vitest/React Testing Library, accessibility, performance, code review, dependency upgrades, technical debt, agent orchestration, production guardrails, MCP integrations, and developer experience.

## Three-Layer Model

- **Layer 1 — Engineering Standard:** reusable agents, skills, guardrails, orchestration, and engineering practices.
- **Layer 2 — Organization Policy:** organization-specific architecture, security, accessibility, testing, dependency, and PR policies.
- **Layer 3 — Project Overlay:** application-specific architecture, domain rules, commands, conventions, and constraints.

Keep organization- and project-specific assumptions out of the reusable core.

## Skills and Agents

Skills should solve a clear frontend engineering problem and explain when they should activate, workflow, validation, guardrails, completion criteria, and important gotchas.

Agents should have focused responsibilities and use the minimum tool permissions necessary. Avoid creating agents with substantially overlapping responsibilities.

Orchestration changes should preserve production guardrails, delegate work appropriately, avoid unnecessary specialists, and never publish, merge, release, or deploy without explicit intent.

## Third-Party Resources

Prefer installation from original upstream sources rather than copying community content into the core plugin. Do not submit third-party content unless its license permits redistribution. Preserve required copyright, license, attribution, and NOTICE information and identify the source in the pull request.

See `THIRD_PARTY_NOTICES.md`.

## Development Workflow

```sh
git checkout -b feat/my-change

# make changes

python3 scripts/bump-plugin-version.py patch
# or minor/major when appropriate

python3 scripts/validate-plugin-version.py
python3 scripts/release-check.py

git status
git diff
```

Update `CHANGELOG.md` where appropriate and test changed agents/skills locally with GitHub Copilot when practical.

## Versioning

- **PATCH:** fixes, documentation, guardrail corrections.
- **MINOR:** backward-compatible agents, skills, or capabilities.
- **MAJOR:** breaking public behavior/configuration changes.

Maintainers may adjust the release version during review.

## Pull Requests

Keep PRs focused. Explain the problem, solution, affected agent/skill/layer, validation actually performed, risks, and behavioral changes.

## AI-Assisted Contributions

AI-assisted development is welcome, but contributors remain responsible for reviewing and validating submissions. Do not submit content you do not understand, fabricated APIs/results, secrets/private information, or content that violates third-party licenses.

## Security

Do not disclose exploitable vulnerabilities or credentials in public issues. Use GitHub private vulnerability reporting when available.

## Licensing

By intentionally submitting a contribution for inclusion in this project, you agree that it may be distributed under the Apache License 2.0, consistent with the repository `LICENSE`. Do not contribute material you do not have the right to submit.

Participation is governed by `CODE_OF_CONDUCT.md`.
