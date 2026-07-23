---
applyTo: "**/src/**/*.{ts,tsx}"
---
# Project API Rules

EDIT:
- API client location
- auth/token handling boundary
- retry policy
- error normalization
- caching/data-fetching conventions

Do not call APIs directly from components if the project architecture defines a service/query layer.
