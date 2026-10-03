# Notebook Structure

Use this reference after the design has been frozen and before generating notebook pages. It defines the output contract; it does not determine project-specific architecture or claims.

## Output mode

Default to generic Markdown. Enable Obsidian mode when the destination is a Vault or the user explicitly requests Obsidian. Content and technical claims must remain identical across modes; only linking, embedding, and ordering conventions differ.

Determine Obsidian mode from an explicit user request or a destination inside a Vault, such as a directory containing `.obsidian/` in its ancestor chain. Do not infer Obsidian mode merely because an input notebook uses wiki links.

## Approved root structure

Adapt mainline names and count to the frozen design while retaining this navigation spine:

```text
project-interview-notebook/
├── 00 使用说明与复习路径.md
├── 00 口径与生成规范.md
├── 01 项目总览与 60 秒介绍.md
├── 02 完成态架构与部署拓扑.md
├── 03 简历条目与 STAR 拆解.md
├── 04 术语、不变量与状态机.md
├── 10 主线一/
│   ├── 01 完成态设计.md
│   ├── 02 三级问答树.md
│   └── 03 故障与质疑.md
├── 20 主线二/
│   ├── 01 完成态设计.md
│   ├── 02 三级问答树.md
│   └── 03 故障与质疑.md
├── 70 部署与中间件选型.md
├── 80 容量估算与统一指标.md
├── 90 攻击性追问与答辩.md
├── 99 面试前速记卡.md
└── assets/
    └── architecture/
        ├── overview.svg
        └── source/overview.drawio
```

Use numbered root pages and mainline directories to keep reading order stable. Four to eight mainlines is a useful default, not a quota; select only themes that carry business relevance, mechanism depth, quantitative framing, and failure discussion.

## Link and embed conventions

### Generic Markdown

- Use relative links from the current document: `[容量口径](../80%20容量估算与统一指标.md)`.
- URL-encode spaces where the renderer requires it, and keep link targets portable within the notebook directory.
- Embed SVG with relative image syntax: `![总体架构](../assets/architecture/overview.svg)`.
- Link to a heading only when it is stable and uniquely owned: `[故障边界](../70%20部署与中间件选型.md#故障边界)`.

### Obsidian

- Use wiki links: `[[80 容量估算与统一指标]]`.
- When page basenames repeat, always qualify the directory: `[[10 主线一/01 完成态设计]]` rather than `[[01 完成态设计]]`.
- Embed SVG with `![[assets/architecture/overview.svg]]`.
- Use aliases when the sentence needs natural wording: `[[10 主线一/01 完成态设计|主线一完成态设计]]`.
- Keep targets relative to the Vault and avoid absolute filesystem links inside notebook content.

### Diagram source retention

Every delivered architecture SVG must have an editable draw.io source with the same basename under `assets/architecture/source/`. Keep a solid background in the SVG so the diagram remains legible in light and dark themes. Diagrams may summarize only mechanisms already frozen in the canonical fact model; they must not introduce components, guarantees, metrics, or failure behavior of their own.

## Root-page contracts

### `00 使用说明与复习路径.md`

Explain the evidence labels, intended reading paths, rehearsal order, and where canonical answers live. Offer a short preparation path and a deeper review path without duplicating the mainline content.

### `00 口径与生成规范.md`

Record the governing narrative rules, selected mainlines, evidence-label semantics, deprecated narratives, and the ownership map for terms, metrics, states, diagrams, and résumé statements.

### `01 项目总览与 60 秒介绍.md`

Provide the business problem, user and scale context, completed-state system summary, personal contribution, primary technical hooks, and a rehearsable 60-second introduction. Link each hook to its owner mainline.

### `02 完成态架构与部署拓扑.md`

Show the frozen component topology, request and data flows, deployment/failure domains, data ownership, and degradation boundaries. Link to editable diagram sources and the deployment-selection page.

### `03 简历条目与 STAR 拆解.md`

Keep one recommended résumé version, optional length variants, and a STAR mapping for each bullet. Every bullet must map to a business problem, owned mechanism, defensible result, and mainline questions. Do not insert internal evidence labels mechanically into résumé prose; retain them beside the supporting notes.

### `04 术语、不变量与状态机.md`

Define canonical terminology, identities and keys, state machines, terminal states, illegal transitions, invariants, sources of truth, and final arbiters. This page owns names; mainline pages link back instead of inventing synonyms.

### `70 部署与中间件选型.md`

Own node topology, failure domains, quorum assumptions, failover/fencing, RTO/RPO, connection budgets, middleware responsibilities, rejected alternatives, and dependency-specific degradation.

### `80 容量估算与统一指标.md`

Maintain the single quantitative ledger. For each number include value, one primary evidence label, assumptions, derivation or evidence location, environment, error definition, applicable boundary, and allowed spoken phrasing. Other pages reference this ledger rather than redefining numbers.

### `90 攻击性追问与答辩.md`

Collect cross-mainline contradictions and high-pressure questions whose answers depend on more than one owner page. Give the direct answer first, then the mechanism, boundary, rejected alternative, and owner links.

### `99 面试前速记卡.md`

Compress the stable 60-second introduction, mainline one-liners, canonical numbers, final arbiters, failure responses, and dangerous phrasing into a last-minute rehearsal page. It is an index and mnemonic, not a second source of truth.

## Mainline document contracts

### `01 完成态设计.md`

Use `assets/markdown-templates/completed-design.md`. Cover:

- Business background and why the mechanism exists.
- Data ownership and source of truth.
- Normal path.
- State machine and invariants.
- Concurrency, idempotency, and consistency.
- Failure degradation and recovery.
- Capacity model and internal evidence labels.
- A rehearsable 60-second answer.
- Résumé hooks and links to related questions.

### `02 三级问答树.md`

Use `assets/markdown-templates/question-tree.md`. Organize each question as:

- 一级：a direct answer suitable for roughly 30 seconds.
- 二级：the mechanism, transaction/data boundary, and key implementation details.
- 三级：limits, failure cases, alternatives, and engineering trade-offs.

Questions should form a path from the résumé hook to mechanism-level follow-ups rather than a flat FAQ list.

### `03 故障与质疑.md`

Use `assets/markdown-templates/failure-review.md`. Record attacks, dependency failures, invariant preservation, recovery, aggressive follow-ups, prohibited phrasing, and the unique owner page for every corrected answer.

## Evidence and duplication rules

- Use `[已验证]`, `[完成态口径]`, `[容量估算]`, and `[边界条件]` inside the notebook to preserve internal calibration.
- Give each state machine, number, deployment fact, and mechanism one owner page. Other pages summarize and link to it.
- Keep completed-state language in the interview narrative. Put non-goals and failure limits under `[边界条件]`, not as future implementation promises.
- Replace every semantic template variable before delivery. Do not leave placeholder syntax, drafting markers, or empty sections in the generated notebook.

