# Design Freeze

Use this reference after repository audit and mainline selection, before writing résumé bullets, diagrams, or question-bank pages. The freeze turns conflicting artifacts into one completed-state interview model. It is a design decision record for the notebook, not a claim that every repository artifact already matches it.

## Freeze before bulk writing

Do not bulk-generate the notebook until all selected mainlines satisfy these conditions:

- one business purpose and one completed-state mechanism are named;
- every durable fact has one owner and every race has one final arbiter;
- states, transitions, identifiers, routing keys, transaction boundaries, and idempotency keys are explicit;
- duplicate, delayed, reordered, partially failed, restarted, and degraded paths converge;
- topology, connection budget, throughput, write amplification, and failure claims are mutually compatible;
- every quantitative claim has one canonical value or range, one primary evidence label, and a speaking boundary;
- rejected names, numbers, states, and topologies are in the deprecated-narrative registry.

If a mechanism is impressive but incomplete, close the missing semantics before removing it. If two plausible choices would materially change the project identity or résumé positioning, ask the user; otherwise choose the more defensible design and record the rejected version.

## Canonical fact model

Maintain one compact fact model that every output page and diagram consumes. Use stable fact IDs so repeated claims can refer back to the same entry.

### Project and scale facts

| Field | Required content |
|---|---|
| Project identity | Users, core workflow, risk, and why the system exists |
| Workload | Ordinary traffic, burst shape, read/write mix, data volume, and hotspot distribution |
| Availability | Intended uptime, tolerated degradation, RPO/RTO or explicit absence of guarantees |
| Resource envelope | Service replicas, middleware topology, machine class, pools, and relevant limits |
| Mainlines | The limited set of interview themes and the business reason for each |

### Mechanism facts

For every mainline freeze:

| Field | Question |
|---|---|
| Completed-state claim | What does the interview say is implemented? |
| Business trigger | Why is the mechanism necessary here? |
| Source of truth | Which durable record owns each fact? |
| Final arbiter | Which conditional write, constraint, lock, quorum, or state transition decides a race? |
| Data ownership | Which service, partition, tenant, user, or aggregate owns the record? |
| Transaction boundary | Which writes commit atomically, and which cross-boundary work is asynchronous? |
| Idempotency | What is the business key, where is it enforced, and what is returned on replay? |
| Ordering | Is ordering global, per key, per partition, or unnecessary? How are stale writes rejected? |
| Recovery | How are retries, reconciliation, compensation, rebuild, and operator intervention handled? |
| Boundary | What failure or scale condition changes the guarantee? |
| Alternatives | Which plausible option was rejected and why? |
| Evidence | Which internal label and source support the claim? |

Never assign ownership to a cache, transient queue, process-local map, or connection. Such components may accelerate access or transport change, but the fact model must identify the durable authority used for rebuild and reconciliation.

## Contradiction resolution

Resolve disagreements among code, comments, tests, old notes, diagrams, and résumé text deliberately:

1. Preserve explicit user choices and avoid contradictions with other frozen résumé claims.
2. Select the design with the strongest business justification and defensible engineering trade-offs.
3. Close its ownership, transaction, idempotency, ordering, recovery, topology, and capacity semantics.
4. Assign internal labels without weakening the completed-state interview language.
5. Put every discarded term or mechanism into the deprecated-narrative registry.

Do not create hybrid designs by keeping incompatible fragments from both sides. Typical conflicts to resolve include two components both claiming final arbitration, two routing layers with different keys, multiple meanings for the same state, different deployment topologies, and a metric used once as measured traffic and elsewhere as design capacity.

## Unified number registry

Centralize numbers before repeating them. Each row has exactly one primary classification.

| Fact ID | Quantity | Canonical value/range | Label | Assumptions or source | Derivation | Speaking boundary | Used by |
|---|---|---|---|---|---|---|---|
| `NUM-*` | Meaningful system quantity | One value or bounded range | `[已验证]`, `[完成态口径]`, `[容量估算]`, or `[边界条件]` | Workload, topology, duration, data size, or evidence path | Formula, benchmark, or acceptance definition | What it does and does not prove | Résumé, overview, mainline, diagram |

Apply these rules:

- Separate observed baseline, production traffic, design capacity, acceptance target, and hard protocol limit.
- For performance results record duration, concurrency, workload mix, resource topology, co-location, latency percentiles, error semantics, and version or commit when known.
- For estimates expose the formula and sensitivity: replicas × pools × connections, requests × writes per request, ingress rate × retention, retry rate × amplification, or equivalent.
- Reconcile aggregate numbers with their parts. A total cannot be lower than a mandatory component, and a per-node value cannot silently become a cluster value.
- Never infer a strict loss window from a flush interval alone or a strict availability guarantee from replica count alone.
- Résumé bullets may use only a small subset; the unified metrics page remains the canonical explanation.

## State-machine freeze

Write each business lifecycle independently. Do not overload one status column with payment, fulfillment, delivery, risk, and notification semantics when they can advance independently.

For each machine record:

| Item | Required decision |
|---|---|
| Entity and owner | The aggregate whose state changes and its durable owner |
| States | Canonical names and user-visible meaning |
| Allowed transitions | From, event/command, guard, to, and side effects |
| Terminal states | States that reject later commands except explicit repair operations |
| Versioning | CAS version, fencing token, lease generation, sequence, or other stale-write guard |
| Timeout | Durable deadline, trigger, fallback scan, and idempotent expiry action |
| Replay result | Result returned when the transition already succeeded or became impossible |

Freeze invariants separately from transitions. Useful invariant forms include:

- at most one active winner, owner, lease, settlement, or terminal decision per business key;
- balances equal the sum of immutable ledger entries and every journal entry balances;
- a state transition and its durable outbound event commit atomically;
- a consumer side effect is unique by business event key;
- every accepted cursor is monotonic only within its declared scope;
- a migrated key resolves to exactly one writable owner for a routing version.

Every invariant names its enforcement point. Application checks alone are not sufficient for cross-request races unless supported by an atomic write, unique constraint, lock, fencing token, or equivalent final arbiter.

## Data-ownership and consistency freeze

Build a data map before drawing topology:

| Dataset | Owner | Partition key | Durable authority | Cached/projected copies | Write path | Read consistency | Repair path |
|---|---|---|---|---|---|---|---|

Then verify:

- every write is routed from information actually available at that call site;
- identifiers, partition keys, directory mappings, and migration units agree;
- global views are declared as authoritative data or asynchronous projections, never both;
- cross-owner workflows define coordinator ownership, terminal acknowledgement, late-message rejection, and compensation or reconciliation;
- cache invalidation, rebuild, and degraded reads all return to the same durable authority;
- user-visible cursors and ordering use a sequence with the same scope as the query.

Physical co-location does not erase logical transaction boundaries. If the completed-state model forbids cross-owner transactions, apply that rule consistently even when the current deployment could technically join or commit across those owners.

## Topology and operational freeze

For every service and middleware component record replicas, role placement, client routing, leader election or failover owner, quorum assumptions, health detection, fencing, and degraded behavior.

Check that:

- failure domains support the claimed automatic recovery;
- only one layer owns each responsibility such as partition routing or read/write selection;
- old primaries or lease holders are fenced before replacement accepts writes;
- connection-pool and thread budgets fit database, broker, cache, and host limits;
- recovery does not depend on the failed component retaining ephemeral state;
- the notebook distinguishes automatic failover, manual recovery, and disaster recovery.

## Deprecated-narrative registry

Maintain a table in the generation specification. Deprecated entries are negative constraints, not historical storytelling.

| Deprecated phrase or fact | Replacement | Reason for rejection | Scan scope |
|---|---|---|---|
| Old term, number, state, topology, or guarantee | Canonical fact ID or wording | Contradiction, incomplete closure, ambiguous ownership, or weaker interview value | Résumé, diagrams, mainline pages, all output |

Register substrings likely to reappear, including aliases and translated names. Do not ban a word when it is needed to explain a rejected alternative; instead require that such occurrences be explicitly framed as rejected and never shown as the active design.

## Freeze outputs

The freeze is complete when it produces:

1. the canonical fact and number registries;
2. a terminology table with one preferred name per concept;
3. state-machine and invariant tables;
4. a data-ownership and routing map;
5. a deployment and failure-boundary model;
6. a résumé claim set linked to mainlines;
7. the deprecated-narrative registry;
8. an unresolved-questions list containing only choices that require user input.

Run the adversarial review against these outputs. If that review changes ownership, invariants, topology, numbers, or terminology, reopen the freeze and propagate the correction before notebook generation.
