---
name: maintenance
description: "Runs the full maintenance workflow: upgrade GitHub Actions, sync deps, lint, test, and commit changes. Use when the user says 'run maintenance', 'do maintenance', or 'maintenance run'."
allowed-tools: Bash, Read, Edit, Write, Agent, WebFetch, WebSearch
---

## Workflow

Run each step in order. Stop and report if any step fails.

1. Ensure on latest `main`: `git pull`
2. Create a maintenance branch: `git checkout -b chore/maintenance`
3. Upgrade GitHub Actions using the `upgrade-github-workflows` skill
4. Check the CI matrix in `.github/workflows/ci.yml` — verify new Python/Django versions are covered. Old EOL versions stay until a major release drops them.
5. `make install` — sync and upgrade dependencies
6. `source .venv/bin/activate && make lint` — check for lint errors; fix any issues found
7. `source .venv/bin/activate && make test` — run test suite
8. Commit any changes to the branch (separate commits per logical change)

Report a summary of which steps passed or failed and what was changed.

## When the Django version matrix changes

If a new Django version is added or an old one is dropped, audit `example_project/` for modernization opportunities:

- Remove compatibility shims for dropped versions
- Adopt newer Django APIs when the minimum supported version provides them
- Keep the example project bare-bones — remove anything not needed to demonstrate django-object-actions features
