# Adversarial Review

Use this reference after the completed-state fact model is drafted and again after diagrams and mainline pages exist. The goal is to find the second or third follow-up question that breaks the story, then repair the frozen design without reflexively removing technical depth.

## Review method

For each mainline, trace one concrete business key, run, or decision through normal execution and these disturbance classes:

- duplicate request or message;
- concurrent execution;
- delay and reordering;
- crash before and after each durable write;
- dependency timeout or failover;
- stale client, cache, route, lease, cursor, prompt, model, tool schema, retrieval index, or evaluation policy;
- retry after the original response is lost;
- reconciliation after an extended outage.

Require every answer to name the authority or run-state owner, final arbiter or evaluation gate, idempotency/replay/version key, state or decision guard, recovery trigger, and boundary of the guarantee. Reject answers that stop at “the framework handles it”, “the middleware guarantees it”, “we retry”, “we add a lock”, or “the database handles it”.

Classify each finding:

- **Mechanism conflict:** two frozen facts cannot both be true. Reopen the design freeze.
- **Missing closure:** the design is plausible but lacks ownership, transition, recovery, or boundary details. Complete it.
- **Capacity mismatch:** numbers, connections, write amplification, or topology do not fit. Recalculate the unified registry.
- **Expression risk:** the design is sound but terminology invites a false interpretation. Rewrite and add an attack answer.
- **Accepted boundary:** the behavior is intentionally degraded or unavailable. Mark `[边界条件]` and make the trade-off explicit.

A mainline passes only when normal and failure paths converge on its invariants and its deployment can deliver the stated guarantee.

## Cross-cutting questions

Ask these before domain-specific checks:

1. What exact business fact, run state, or decision is protected, and where is its authority or durable owner?
2. Which operation finally arbitrates a deterministic race, or which versioned evaluation gate accepts a probabilistic decision?
3. What is the idempotency, replay, or decision-version scope; how long is it retained; and what result does repetition return?
4. Which order is required: global, per aggregate, per partition, or none?
5. Can a stale writer or decision act after leadership, lease, route, state, prompt, model, tool schema, retrieval index, or evaluation-policy changes? What guard rejects it?
6. If the response is lost after a commit or accepted decision, can the caller safely retry and recover the original result and version context?
7. If an asynchronous step never happens, who detects it, when, and from which durable evidence?
8. Does a repair or compensation itself support retries, duplication, and late arrival?
9. Do all call sites possess the routing and ownership information the design assumes?
10. Do topology and capacity numbers match the strongest claim on the résumé?

## Domain-specific review

Read every profile selected during repository audit and apply only its relevant probes. Do not load backend probes merely because the repository has an API around an Agent.

## Closure record

For each finding record:

| Attack | Failure demonstrated | Invariant at risk | Design correction | Evidence label | Boundary or rejected alternative | Pages/diagrams to update |
|---|---|---|---|---|---|---|

After corrections, rerun the original attack and at least one adjacent failure case. Update the canonical fact model first, then propagate to résumé, overview, mainline pages, diagrams, metrics, attack answers, and quick-reference material.

The review is complete when no unresolved finding can produce conflicting final authority or outcomes, an unsafe or duplicate side effect, an accepted result or decision record that cannot be recovered, skipped output where ordering is required, or a claim unsupported by the selected profiles and frozen evidence registry.
