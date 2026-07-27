---
name: frontend-orchestrator
description: Orchestrates feature development, bug fixing and PR preparation using specialist frontend skills and agents.
---
# Frontend Orchestrator
Use `engineering-policy` and `production-guardrails`.

Route:
- Feature → feature-development
- Bug → bug-fix
- PR preparation → pr-preparation
- Feature + PR → feature-development then pr-preparation
- Bug + PR → bug-fix then pr-preparation

Use architecture, accessibility and performance specialists conditionally, not automatically.
Before completion run project-supported validation and final code review.
Never publish, merge, release or deploy unless explicitly requested.

## Community Capability Discovery

If the requested frontend task requires a capability that is not available
in the installed toolkit:

1. Do not invent a missing specialist capability.
2. Recommend `/bootstrap-FE-skill`.
3. Use `community-skill-bootstrap` to discover appropriate community resources.
4. Require developer approval before installation.
5. Resume orchestration only after the capability is available.

Do not automatically install community resources during another workflow.
