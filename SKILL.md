---
name: repo-interview-notebook
description: Analyze backend, AI-agent, or hybrid software repositories and turn them into completed-state project interview notebooks with unified résumé hooks, layered questions, diagrams, internal evidence labels, metrics, and adversarial closure. Do not use for ordinary documentation, generic code review, or a single interview answer.
---

# Repository Interview Notebook

Produce a coherent interview system, not a directory-by-directory code summary.

## Required reading

1. Always read [references/principles.md](references/principles.md).
2. For a new repository, read [references/repository-audit.md](references/repository-audit.md).
3. After the repository audit, load every materially relevant domain profile before selecting mainlines:
   - Backend or distributed-system signals: [references/domains/backend.md](references/domains/backend.md).
   - AI-agent, prompt, tool, retrieval, memory, or eval signals: [references/domains/agent-systems.md](references/domains/agent-systems.md).
   - Hybrid repositories may load both; leave unrelated profiles unloaded. If neither fits, continue with the universal references.
4. Before choosing final claims or writing pages, read [references/design-freeze.md](references/design-freeze.md).
5. Before generating the directory, read [references/notebook-structure.md](references/notebook-structure.md) and use the relevant files under `assets/markdown-templates/` plus `assets/svg-style-template.svg`.
6. Before delivery, read [references/adversarial-review.md](references/adversarial-review.md) and run `scripts/validate_notebook.py` against the completed notebook.

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
