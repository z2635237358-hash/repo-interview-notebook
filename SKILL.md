---
name: repo-interview-notebook
description: Analyze a software repository and turn it into a completed-state project interview notebook with unified résumé hooks, layered questions, architecture diagrams, internal evidence labels, capacity models, and adversarial closure review. Use for repository-backed interview-note or project-question-bank creation; do not use for ordinary repository documentation, generic code review, or a single interview answer.
---

# Repository Interview Notebook

Produce a coherent interview system, not a directory-by-directory code summary.

## Required reading

1. Always read [references/principles.md](references/principles.md).
2. For a new repository, read [references/repository-audit.md](references/repository-audit.md).
3. Before choosing final claims or writing pages, read [references/design-freeze.md](references/design-freeze.md).
4. Before generating the directory, read [references/notebook-structure.md](references/notebook-structure.md) and use the relevant files under `assets/markdown-templates/` plus `assets/svg-style-template.svg`.
5. Before delivery, read [references/adversarial-review.md](references/adversarial-review.md) and run `scripts/validate_notebook.py` against the completed notebook.

## Workflow gates

- Resolve the repository path, optional résumé and old-notebook inputs, destination, target role, and output mode.
- Treat the source repository as read-only unless code changes are separately requested.
- Select a limited set of interview mainlines and freeze one fact model before bulk writing.
- Use the completed-state design as the project's implemented interview narrative while preserving `[已验证]`, `[完成态口径]`, `[容量估算]`, and `[边界条件]` internally.
- Keep quantitative claims in one metrics page.
- Resolve mechanism conflicts through critical closure review before drawing diagrams or writing résumé bullets.
- Generate the notebook, perform adversarial review, validate, fix failures, and report what was created.

## Output behavior

- Default to generic Markdown; use Obsidian conventions when the destination is a Vault or the user explicitly requests them.
- Prefer authored SVG plus an editable draw.io source over Mermaid for architecture diagrams.
- Render and visually inspect diagrams when rendering tools are available.
- Never silently overwrite an existing notebook; use a new destination or obtain explicit permission for replacement.
