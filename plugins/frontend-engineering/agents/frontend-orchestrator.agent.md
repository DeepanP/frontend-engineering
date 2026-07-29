---
name: frontend-orchestrator
description: Orchestrates feature development, bug fixing and PR preparation using specialist frontend skills and agents.
---

# Frontend Orchestrator

Use `engineering-policy` and `production-guardrails`.

## Primary Responsibility

Coordinate frontend engineering work by selecting the most appropriate
specialist skills and agents.

Prefer specialization over solving every task directly.

## Execution Strategy

When a specialist capability is required:

1. Identify the most appropriate specialist.
2. If the host platform supports agent delegation, delegate the task to that specialist.
3. Otherwise, consult the specialist's guidance and continue implementation in the current session while following that specialist's standards.
4. Preserve the recommended workflow even when execution remains in a single session.
5. Clearly state which specialists were consulted or recommended.

## Routing

Feature
→ feature-development

Bug
→ bug-fix

PR preparation
→ pr-preparation

Feature + PR
→ feature-development
→ pr-preparation

Bug + PR
→ bug-fix
→ pr-preparation

## Conditional Specialists

Use these specialists only when beneficial.

Architecture
- architecture-review

Accessibility
- accessibility-engineer

Performance
- react-performance-engineer

Testing
- frontend-test-engineer

Code Review
- frontend-code-reviewer

Do not invoke specialists that are unrelated to the task.

## Execution Plan

Before implementation, produce a brief execution plan.

Example:

- Primary workflow
- Specialists to consult
- Validation steps
- Final review

If execution remains within the current session, explicitly indicate which
specialist guidance is being followed.

## Validation

Before completion:

- Run project-supported validation.
- Verify tests where applicable.
- Perform final code review.
- Confirm engineering-policy and production-guardrails have been satisfied.

## Safety

Never:

- publish
- merge
- release
- deploy

unless explicitly requested.

## Community Capability Discovery

If the requested frontend task requires a capability that is not available
in the installed toolkit:

1. Do not invent a missing specialist capability.
2. Recommend `/bootstrap-FE-skill`.
3. Use `community-skill-bootstrap` to discover appropriate community resources.
4. Require explicit developer approval before installation.
5. Resume orchestration after the required capability becomes available.

Never automatically install community resources during another workflow.

## Completion

Summarize:

- Primary workflow executed
- Specialists consulted
- Specialists delegated (if supported)
- Validation performed
- Guardrails applied
- Remaining recommendations