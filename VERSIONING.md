# Plugin Versioning

Current frontend engineering plugin version: `2.0.0`.

The plugin version is stored in two places and must match:

- `plugins/frontend-engineering/plugin.json`
- `.github/plugin/marketplace.json` → `plugins[].version`

The marketplace catalog's `metadata.version` is independent and does not need to match the plugin version.

## Bump

```sh
python3 scripts/bump-plugin-version.py patch
python3 scripts/bump-plugin-version.py minor
python3 scripts/bump-plugin-version.py major
```

You may also set an explicit version:

```sh
python3 scripts/bump-plugin-version.py 2.5.0
```

## Validate

```sh
python3 scripts/validate-plugin-version.py
python3 scripts/release-check.py
```

## Release

1. Make the engineering change.
2. Choose PATCH / MINOR / MAJOR.
3. Run the bump script.
4. Update `CHANGELOG.md`.
5. Run release checks.
6. Open/merge the PR after CI passes.
7. Tag the release:

```sh
git tag frontend-engineering-vX.Y.Z
git push origin frontend-engineering-vX.Y.Z
```

8. Consumers refresh/update the marketplace/plugin using their supported Copilot plugin commands.

Do not manually delete Copilot's installed-plugin directory as a version-management strategy.
