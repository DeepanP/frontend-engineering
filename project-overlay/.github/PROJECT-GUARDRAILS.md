# Project Guardrails

Customize and enforce these in CI/platform settings where possible.

## Commands
Typecheck: <COMMAND>
Lint: <COMMAND>
Unit tests: <COMMAND>
Build: <COMMAND>
Accessibility: <COMMAND>
E2E: <COMMAND>

## Protected areas
Auth/security modules: <PATHS>
Payments/critical transactions: <PATHS>
Shared design system: <PATHS>
Public APIs: <PATHS>

## Human review triggers
- changes to authentication/authorization
- public API contracts
- data migrations
- critical accessibility behavior
- production configuration
