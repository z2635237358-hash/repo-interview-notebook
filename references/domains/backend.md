# Backend Systems Profile

Use this profile when server, persistence, distributed-systems, or operational signals materially affect the selected interview mainlines. Hybrid repositories may combine it with another profile.

## Repository signals and evidence

Inspect handlers and APIs, schemas/migrations/indexes, transactional use cases, caches, queues, schedulers, service configuration, deployment topology, integration tests, benchmark reports, and reconciliation/operations code.

## Candidate mainlines

Choose only business-relevant themes: concurrency and arbitration; funds and ledgers; message reliability; cache/hotspot control; partitioning/routing; high availability; real-time delivery; authorization and operational repair.

## Concurrency and arbitration

- Identify the contention key and hotspot shape. Is contention per record, tenant, partition, account, or global?
- Distinguish admission control from final arbitration. If a cache or rate limiter loses state, can the durable arbiter still preserve the invariant?
- Show the exact conditional update, unique constraint, fencing token, or serialization point that decides the winner.
- Check whether read-then-write logic races under the database isolation level actually named.
- Define lock scope, timeout, lease renewal, owner identity, and behavior after lease expiry.
- If a queue or candidate list exists, state whether ordering is a business fact, where it persists, how capacity is bounded, and how stale rounds are rejected.
- Test retries after success, duplicate submissions from different devices, client timeouts, and concurrent cancellation.
- Decide fail-open versus fail-closed for each unavailable admission or arbitration dependency and connect that choice to the protected invariant.
- Reconcile the advertised burst with write connections, transaction duration, lock wait, downstream writes, and retry amplification.

Closure requires a durable invariant that remains true even when fast-path admission components fail. A design that merely reduces collision but cannot prevent duplicate final outcomes is not closed.

## Funds, ledgers, and settlement

- Define monetary units, rounding, sign conventions, and whether balances are stored, derived, or both.
- Name the authoritative ledger and prove each posting balances. If a cached balance exists, specify reconciliation against immutable entries.
- Put balance mutation, ledger entries, business status, and outbound event in explicit transaction boundaries.
- Enforce idempotency by a stable business number plus account/direction or an equivalent uniqueness model; process-local deduplication is insufficient.
- Test concurrent debit, refund, settlement, reversal, and retry. State which guard prevents overdraft or repeated settlement.
- For cross-owner transfer, identify the coordinator record and terminal states. Ask who advances it, how the target acknowledges, and how the source learns the final result.
- Prevent suspension anomalies: compensation before execution, duplicate compensation, and a late original action after reversal. Use a durable rejected/closed terminal at the receiving side when necessary.
- Explain reconciliation levels: business order versus ledger, account balance versus ledger sum, and source versus target owner.
- State what happens when replication safety degrades: continue, reject money writes, or accept a bounded risk. Include detection delay and repair of the exposure window.

Closure requires conservation, uniqueness, retry-safe reversal, and an auditable repair path. “Eventually consistent” is not an answer unless the acceptable intermediate states and terminal convergence are specified.

## Messaging and scheduled work

- Identify why messaging is needed and whether delivery is at-most-once, at-least-once, or effectively-once at the business side effect.
- Show how the business write and outbound intent become atomic, or explain the broker transaction and its uncertainty protocol.
- Define producer replay, relay ownership, claim/lease semantics, backoff, poison-message handling, and retention.
- Give the consumer's idempotency key, uniqueness enforcement, and response to duplicate, stale, and reordered messages.
- For scheduled or delayed work, persist the deadline and make the database scan or equivalent durable index a fallback; do not let broker availability own the deadline.
- Test crash before send, after send before acknowledgement, after consume before side effect, and after side effect before acknowledgement.
- Distinguish queue sharing, fan-out, and broadcast semantics for the exact client model. Verify where offsets live and what a replacement consumer reads.
- If the broker loses quorum or is unavailable, state which business flows stop, which continue, how backlog is observed, and how catch-up is bounded.

Closure requires that lost acknowledgements create duplicates rather than lost facts, and that duplicates converge through durable business idempotency.

## Cache and hotspot control

- State whether the cache owns any business truth. If not, identify the database or log used to rebuild every cached structure.
- Choose and explain the consistency pattern for each data type; do not apply one cache pattern indiscriminately.
- For cache-aside, attack penetration, breakdown, avalanche, stale overwrite, delete failure, and a write racing with cache refill.
- If using delayed double deletion, state the window it reduces and why periodic comparison or event repair is still needed.
- Bound lock or single-flight scope and provide behavior when the lock holder crashes.
- Separate local and distributed cache invalidation, versioning, and expiry semantics when both exist.
- For hot keys, show sharding, replication, request coalescing, or admission control without breaking a global invariant.
- Verify failover behavior: transient cache loss may increase database load, but must not create multiple durable winners or irreparable ordering loss.
- Reconcile cache hit-rate claims with workload distribution, TTL, cold start, and bypass traffic; reconcile latency claims with database fallback.

Closure requires a rebuildable cache, a bounded stale-read story, database protection during misses, and a repair mechanism for invalidation loss.

## Partitioning, routing, and migration

- Declare the logical owner, partition key, virtual routing unit if any, and physical placement independently.
- Confirm every request, message, callback, timeout scan, and repair job can derive the route from information it possesses.
- Check identifier encoding against directory-based routing. An encoded physical location becomes stale after migration unless it represents a stable virtual unit.
- State how global data is stored: dedicated owner, replicated reference data, or asynchronous projection. Avoid hidden cross-partition joins.
- Define the rule for cross-partition transactions even when partitions are physically co-located.
- For migration, explain snapshot/copy, incremental catch-up, dual-read or verification if used, write ownership, route-version switch, rollback, and fencing of the old owner.
- Test stale routes, in-flight messages, retries created before cutover, and readers with old directory caches.
- Reconcile partition count and pool count with database connection limits and operational complexity.

Closure requires exactly one writable owner for a routing version, deterministic handling of stale traffic, and a migration unit consistent with identifiers and routing tables.

## High availability and deployment

- Draw processes, replicas, zones or failure domains, and client paths. Count votes rather than inferring availability from “three nodes”.
- Name the component that detects failure, elects or promotes, updates routing, and fences the old primary.
- Distinguish process failure, host failure, zone loss, network partition, dependency loss, and total disaster recovery.
- Verify quorum placement for the claimed automatic-failover scenario. If a failure loses majority, call it manual recovery or add an appropriate witness/failure domain.
- State replication mode, acknowledgement point, lag behavior, and what happens when synchronous protection falls back.
- Include DNS, VIP, proxy, driver, and connection-pool refresh behavior; a promoted primary is useless if clients remain pinned to the old route.
- Prevent responsibility overlap: one layer should own partition routing, read/write routing, discovery, and fencing unless their boundaries are explicit.
- Budget recovery time from detection, election, promotion, routing propagation, connection recreation, and backlog catch-up.
- Check observability for lag, quorum, pool exhaustion, retry storms, backlog, reconciliation difference, and degraded-mode switches.

Closure requires a topology that survives the exact failure named, rejects stale writers, and states honest RPO/RTO boundaries.

## Real-time delivery and offline recovery

- Separate durable notification creation from best-effort online push. The push channel is not the source of truth.
- Define inbox ownership, recipient and tenant scope, durable sequence, retention, read model, and unread aggregation.
- Use a cursor monotonic in the same scope as the query. A globally generated ID is not automatically commit-ordered per recipient.
- Test event creation before connection, connection loss during push, duplicate delivery, out-of-order delivery, acknowledgement loss, multi-device acknowledgement, and reconnect.
- Bound per-connection queues and define slow-consumer behavior: backpressure, disconnect, coalescing, or durable catch-up.
- Define whether acknowledgement means delivered to process, written to socket, received by client, or read by user.
- State how clients authenticate the upgrade or stream, how short-lived credentials are consumed, and what happens when the credential store is unavailable.
- If messages are fanned out through a broker, verify consumer-group semantics, replacement-node offsets, node identity, and historical backfill.
- Compare WebSocket, server-sent events, long polling, and polling using actual requirements such as client support, bidirectional acknowledgements, heartbeats, and operational cost.
- Avoid a separate gateway or user-to-node registry unless scale and routing needs justify its failure modes. Explain the simpler topology's connection and load-balancing constraints.
- When broker, cache, or socket delivery fails, require inbox polling or another durable recovery path and specify backlog limits.

Closure requires no permanent notification loss from channel failure, a non-skipping cursor, retry-safe acknowledgements, and a clear definition of “real time”.

## Additional backend probes

Apply where relevant:

- **Identity and sequence:** clock rollback, worker/lease reuse, generation overflow, and ordering assumptions.
- **Credit, risk, or reputation:** event ownership, idempotent projection, stale eligibility reads, recalculation, abuse, and whether scores are advisory or monetary authority.
- **Search and analytics projections:** source-of-truth replay, schema change, lag visibility, and deletion/privacy propagation.
- **Authorization:** entry checks versus transaction-time authoritative checks, revocation races, and ownership changes.
- **Operations:** safe manual replay, repair audit trail, poison-data quarantine, and prevention of two operators applying the same repair.

## Metrics and dangerous claims

Classify throughput, latency percentiles, errors, concurrency, cache hit rate, connection budgets, write amplification, replication lag, backlog, RPO/RTO, and recovery time. Reject claims that multiply logical partitions into physical capacity, infer loss bounds from flush intervals, or infer quorum from node count alone.
