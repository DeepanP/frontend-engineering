# Changelog

All notable changes to `frontend-engineering` are documented here.

## [2.0.0] - 2026-07-23

### Added
- Frontend orchestrator
- Standalone feature-development workflow
- Standalone bug-fix workflow
- Standalone PR-preparation workflow
- Git diff analysis, validation and PR-description skills
- Three-layer marketplace/plugin/project architecture

### Changed
- Marketplace packaging uses repository-root `plugins/frontend-engineering`
- Production guardrails remain shared across standalone and orchestrated workflows

## Release convention

- PATCH: fixes or non-breaking instruction/guardrail corrections
- MINOR: backward-compatible skills, agents or workflows
- MAJOR: removed/renamed entry points, breaking project requirements or incompatible behavior
