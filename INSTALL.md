# Installation

## Marketplace install

1. Push the **contents of this directory** to the root of a GitHub repository.
2. Confirm this exact file exists in GitHub:
   `.github/plugin/marketplace.json`
3. Confirm this exact plugin manifest exists:
   `plugins/frontend-engineering/plugin.json`
4. Register:
   `copilot plugin marketplace add OWNER/REPO`
5. Browse:
   `copilot plugin marketplace browse frontend-engineering-marketplace`
6. Install:
   `copilot plugin install frontend-engineering@frontend-engineering-marketplace`

## Troubleshooting

### "Not a valid plugin marketplace"
Check:
- You uploaded the extracted repository contents, not only the ZIP binary.
- `.github/plugin/marketplace.json` exists on the branch Copilot is reading.
- JSON is valid.
- Marketplace `source` is `./plugins/frontend-engineering`.
- `plugins/frontend-engineering/plugin.json` exists.

### Test plugin independently
Run:
`copilot plugin install OWNER/REPO:plugins/frontend-engineering`

If that succeeds, the plugin is valid and the remaining issue is marketplace discovery/configuration.

### Changes not showing
Installed plugins are cached. Reinstall/update after changing the plugin.

## Important: archive root

This ZIP has no enclosing toolkit directory. Extract/copy its contents directly into the Git repository root.

Before pushing:

```sh
test -f .github/plugin/marketplace.json
test -f plugins/frontend-engineering/plugin.json
git status
```

On GitHub, `plugins` must be visible directly beside `.github`, `README.md`, `organization-policy`, and `project-overlay`.
