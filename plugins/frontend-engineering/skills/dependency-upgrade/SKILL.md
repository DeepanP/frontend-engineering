---
name: dependency-upgrade
description: Plan and execute safe incremental frontend dependency upgrades.
---

# Dependency Upgrade

Before editing versions:
1. inspect package.json and lockfile
2. identify current and target versions
3. verify breaking/deprecated APIs using trusted documentation when available
4. map repository usage
5. plan migration
6. upgrade incrementally
7. run typecheck/lint/tests/build
8. report remaining deprecations and rollback

Avoid unrelated major upgrades.
