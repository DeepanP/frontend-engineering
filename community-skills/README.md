# Optional Community Skills

Do not blindly install third-party skills.

GitHub supports shared Agent Skills and points to the `github/awesome-copilot` collection.

Recommended workflow:

```sh
gh skill search react
gh skill search accessibility
gh skill search testing
gh skill preview OWNER/REPOSITORY SKILL
gh skill install OWNER/REPOSITORY SKILL
```

Preview and review every skill before installation, especially skills that contain scripts or pre-approved shell tools.

Project skills can live in `.github/skills/`.
Personal reusable skills can live in `~/.copilot/skills/`.

The standard plugin already includes core frontend skills, so add community skills only where they provide additional value.
