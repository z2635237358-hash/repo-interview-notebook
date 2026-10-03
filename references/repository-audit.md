# Repository Audit

Use this reference when inspecting an unfamiliar repository and selecting the technical mainlines for its interview notebook. The audit is evidence collection and design interpretation, not authorization to edit the source repository.

## Read order

1. Repository instructions and README files.
2. Module tree and build manifests.
3. Schemas, migrations, and indexes.
4. Configuration and middleware integration.
5. Core business use cases and state transitions.
6. Tests, benchmarks, and evidence indexes.
7. Existing résumé text and interview notes.

Start broad enough to find service and data boundaries, then follow only the flows that can become interview mainlines. Prefer repository-native search and manifests over exhaustive file-by-file reading. Inspect generated files or vendored dependencies only when they materially affect the system story.

Repository instructions establish access, safety, and execution boundaries. They do not automatically determine the interview architecture. Record actual implementation evidence separately from the completed-state interpretation.

## Extraction table

For every candidate mechanism record: business problem, current artifact, completed-state interpretation, source of truth, invariant, failure mode, useful metric, and interview depth.

Use one row per mechanism or closely related mechanism group. A practical table contains:

| Field | Question to answer |
|---|---|
| Business problem | What user, risk, scale, or operational problem requires this mechanism? |
| Current artifact | Which code, schema, configuration, test, report, résumé line, or note informed the finding? |
| Completed-state interpretation | What single final design should the notebook and interview use? |
| Source of truth | Which durable record owns the fact? |
| Invariant and final arbiter | What must always hold, and which write, constraint, or state transition decides the result? |
| Failure mode and recovery | How do duplicate, delayed, reordered, unavailable, or partially completed paths converge? |
| Useful metric | Which verified result, capacity estimate, or boundary makes the mechanism concrete? |
| Interview depth | Can it sustain direct, implementation, and trade-off questions without relying on vocabulary alone? |

Attach the appropriate internal label to extracted evidence. Keep executed observations, completed-state claims, sizing models, and boundaries distinct even when they appear in the same row.

During extraction, identify cross-cutting facts that must later be frozen once: business scale, topology, data ownership, state names, identifiers, routing keys, transaction boundaries, idempotency keys, consistency level, deployment shape, capacity figures, and degraded behavior.

## Mainline selection

Select four to eight mainlines. Prefer topics with a real business reason, at least one non-trivial invariant, layered follow-up potential, a measurable result or capacity model, and a defensible failure story. Merge overlapping mechanisms. De-emphasize decorative frameworks and generic CRUD.

Score candidate mainlines by interview value rather than module size. Strong mainlines normally connect several layers, such as an API decision, persistent data model, concurrency control, middleware role, recovery process, and operational boundary. A sophisticated implementation without a clear business reason is weaker than a smaller mechanism with a crisp invariant and failure story.

Choose a limited set that collectively demonstrates breadth without duplicating the same consistency pattern. Combine caching, throttling, and hotspot protection when they share one traffic-control story; separate them only when their sources of truth or failure semantics differ. Treat framework labels, architectural styles, and routine CRUD as supporting detail unless they materially change an invariant or trade-off.

For each selected mainline, confirm that the future notebook can provide:

- a business trigger and a 30–60 second overview;
- an owned data model and explicit source of truth;
- a normal path, state transitions, and invariants;
- concurrency, idempotency, consistency, and failure recovery;
- one useful quantified claim with an internal evidence label;
- alternatives, limits, and at least three levels of follow-up.

If a candidate cannot meet these conditions, merge it into a stronger mainline, keep it as supporting context, or omit it. Do not manufacture a standalone chapter to preserve every technology found in the repository.

## Conflict handling

Do not let an isolated class name or stale comment create a second narrative. Record conflicts, choose one completed-state fact model, and add discarded versions to the deprecated-narrative registry.

Resolve conflicts in this order:

1. Preserve explicit user choices and avoid contradictions with the résumé or other frozen claims.
2. Choose the design that offers the strongest defensible business and engineering explanation.
3. Close its data ownership, transaction, idempotency, failure, deployment, and capacity semantics.
4. Mark supporting material with `[已验证]`, `[完成态口径]`, `[容量估算]`, or `[边界条件]` as appropriate.
5. Register rejected terminology, numbers, states, and topologies so they cannot re-enter later pages.

Do not silently upgrade an observed test into a production-capacity result, and do not downgrade the completed-state story merely because the repository contains a partial or older mechanism. Escalate to the user only when competing choices would materially change the project identity, résumé positioning, or authorization boundary.
