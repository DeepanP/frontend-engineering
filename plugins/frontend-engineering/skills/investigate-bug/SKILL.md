---
name: investigate-bug
description: Diagnose frontend defects using evidence before changing implementation.
---

# Investigate Bug

Use engineering-policy and production-guardrails.

Do not edit during initial diagnosis.

Trace:
user action → handler → state/data → effect → render → DOM/result.

Form more than one plausible hypothesis.
Verify using repository, tests, logs or browser evidence.
Report root cause, evidence, smallest fix, regression test and possible side effects.
