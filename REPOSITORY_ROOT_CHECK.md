# Repository Root Verification

This archive is intentionally packaged WITHOUT an outer directory.

After extracting/copying into the Git repository root, these commands must succeed:

```sh
test -f .github/plugin/marketplace.json
test -f plugins/frontend-engineering/plugin.json
git ls-files plugins/frontend-engineering/plugin.json
```

Expected GitHub repository root:

```text
.github/plugin/marketplace.json
plugins/frontend-engineering/plugin.json
organization-policy/
project-overlay/
README.md
```

Marketplace source is:

```json
"source": "plugins/frontend-engineering"
```

Do not commit this package inside another enclosing folder.
