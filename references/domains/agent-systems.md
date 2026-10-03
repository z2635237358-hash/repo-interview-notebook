# Agent Systems Profile

Use this profile when Agent orchestration, model decisions, prompts, tools, retrieval, memory, evals, or safety boundaries materially affect the interview story. The purpose is to expose second- and third-level failure modes and force a completed-state contract, not to produce an Agent terminology catalog.

## Repository signals and read order

Inspect the artifacts that can prove how a run is decided and controlled, not only the happy-path demo:

1. orchestration code, graphs, run stores, checkpoints, retry policies, and termination guards;
2. prompt hierarchy, template/version management, model configuration, routing, and fallback;
3. tool or MCP schemas, permission checks, execution adapters, approval gates, and audit records;
4. retrieval, reranking, citation construction, memory extraction, and context assembly;
5. structured-output validation, repair loops, traces, and production failure taxonomy;
6. eval datasets, graders, human calibration, release thresholds, safety filters, and sandboxing;
7. latency, token, model-mix, tool-call, retry, and cost reports.

Treat configuration and prompts as executable behavior. When a README conflicts with run-state, eval, memory, or tool contracts, freeze one defensible completed-state design rather than combining incompatible fragments.

## Candidate interview mainlines

Select four to eight themes because they carry business value and defensible engineering depth, not because every Agent concept deserves a chapter:

- orchestration, persisted run state, resumability, and bounded termination;
- model routing, prompt architecture, and structured decisions;
- tool reliability, permissions, and deterministic side-effect safety;
- retrieval, grounding, citations, and evidence-absence behavior;
- memory ownership, context construction, privacy, and repair;
- multi-agent coordination, arbitration, and measurable value;
- evaluation, release gates, online drift, and failure attribution;
- safety, human control, latency, token, and cost engineering.

Reject a mainline that has only a framework name or demo flow. Keep it only after its owner, decision boundary, failure convergence, eval contract, and speaking metrics are explicit.

## Orchestration, state, and termination

Attack the run as a durable state machine:

- Who owns the canonical run state: an orchestration store, a queue, a process-local graph, or the conversation transcript? Which one survives a worker restart?
- What uniquely identifies a run, step attempt, tool intent, checkpoint, and resume token? How is a retried or late step rejected after the run has advanced?
- Which conditions terminate the loop: terminal node, maximum steps, wall-clock deadline, recursion depth, token budget, cost budget, repeated-state detector, or human cancellation? Which condition wins when several fire together?
- Are model retries, tool retries, and graph retries counted separately? Can nested retries multiply beyond the advertised budget?
- After a crash between recording a decision and scheduling the next step, who detects the gap and resumes it? After scheduling but before acknowledging, why does replay not duplicate work?
- What happens when cancellation races with an in-flight model or tool call? Is the result discarded by run version, compensated, or allowed to commit?
- Can a paused or human-reviewed run resume against a changed prompt, model, tool schema, retrieval index, or permission set? If so, which version contract applies?

Close the mainline with a persisted run/step model, explicit attempt or fencing version, bounded budgets, idempotent scheduling, checkpoint/replay semantics, and terminal states that reject stale continuation. “The framework manages the loop” is not a closure answer.

## Models, prompts, and structured outputs

Attack every model result as a versioned, fallible proposal:

- Which prompt, model, sampling parameters, tool schema, retrieval-index version, and policy configuration produced the decision? Can a failed trace be reproduced closely enough to classify it?
- How are system, developer, user, retrieved, memory, and tool-result instructions delimited and ordered? Can untrusted content impersonate a higher-priority instruction?
- What is the routing policy by task, risk, latency, language, or context size? Does fallback preserve required capabilities such as tool use, structured output, vision, or context length?
- How is schema validity enforced: provider-native constraints, parser validation, semantic validation, or all three? What is the bounded repair policy when syntax is valid but fields are contradictory or unsafe?
- Does retry reuse the same prompt and evidence, or can changing context make the second result incomparable? Is a low-confidence or conflicting result allowed to abstain?
- How does the team detect that a cheaper model, prompt edit, schema change, or fallback improved average cost while regressing a critical slice?
- If two valid structured decisions disagree, what deterministic policy or human boundary selects the action?

Close with a version manifest, instruction-trust boundary, capability-aware routing/fallback table, bounded validation/repair path, abstention policy, and eval gate tied to the exact version bundle. Do not claim determinism merely because JSON is valid.

## Tool use and side-effect safety

Attack the boundary between probabilistic intent and deterministic execution:

- Where are tool names, argument schemas, permissions, tenant scope, rate limits, deadlines, and return contracts enforced independently of the model?
- Does the executor distinguish read-only, reversible, externally visible, financial, destructive, and privileged tools? Which classes require user confirmation or a human approval token?
- What business idempotency key identifies the intended effect? Is it enforced at the real side-effect owner rather than only in Agent memory or a local cache?
- If the tool succeeds but the response is lost, does retry query the prior result, return the committed outcome, or repeat the action?
- If a multi-step tool partially succeeds, what transaction, compensation, reconciliation, or operator workflow converges it? Who owns the final status?
- Can prompt injection choose a tool, expand its scope, or smuggle arguments outside the validated schema? Are URLs, file paths, SQL fragments, recipients, and resource IDs independently allowlisted or resolved?
- How are timeouts, provider 429/5xx errors, ambiguous responses, and non-retryable business errors classified? Can retries multiply external side effects?
- What audit record connects user authorization, model proposal, validated arguments, approval, execution attempt, and final result?

Close with deterministic authorization and validation before execution, per-effect idempotency, explicit transaction/final-arbiter semantics, lost-response recovery, approval gates, and an auditable intent-to-result chain. A model-selected action never relaxes the ordinary guarantees required by the underlying business system.

## Retrieval, grounding, and citations

Force failure attribution beyond “the model hallucinated”:

- Can the system distinguish corpus absence, permission filtering, chunking loss, embedding miss, metadata-filter error, reranker error, context truncation, citation-mapping error, and reasoning error?
- What query transformations are performed, and can they erase names, dates, negation, or tenant constraints? Which trace fields reveal the original and transformed queries?
- How are chunk boundaries, overlap, parent-child expansion, metadata filters, reranking depth, and top-K chosen and evaluated on representative slices?
- What is the freshness contract? How are deleted, revoked, superseded, or re-embedded documents prevented from appearing in results and citations?
- Are access controls enforced before retrieval and again before answer delivery? Can shared indexes leak metadata or snippets across tenants?
- Does every cited claim map to retrieved evidence that actually entails it, or does the system merely cite a nearby document? How are conflicting sources represented?
- What happens when evidence is absent, stale, low confidence, mutually inconsistent, or too large for the token budget: abstain, ask a question, broaden retrieval, use a trusted fallback, or escalate?

Close with a versioned corpus/index contract, permission and freshness enforcement, observable retrieval stages, claim-to-evidence citation validation, evidence-absence behavior, and slice-based retrieval plus answer-quality evals. Do not use end-to-end answer accuracy to hide retrieval failure.

## Memory and context management

Classify each memory store before discussing algorithms: authoritative fact, durable user preference, rebuildable projection, lossy summary, or retrieval hint.

- Which source owns a fact when conversation text, structured memory, summary, vector recall, and current user input disagree?
- How is a memory candidate extracted, validated, versioned, scoped to user/tenant/task, and committed? Can the model write an unverified inference as a durable fact?
- How are corrections, concurrent updates, expiry, supersession, deletion requests, retention, and privacy boundaries enforced across structured and vector copies?
- Can malicious or accidental content poison future prompts? Is stored content treated as data rather than privileged instruction?
- What token budget is allocated among instructions, recent turns, retrieved knowledge, memory, and tool results? Which content is dropped first, and is truncation visible in traces?
- If an embedding model or schema changes, how is memory rebuilt or migrated? What happens while old and new representations coexist?
- What precision/recall or task-success evidence justifies remembering an item rather than recomputing or asking the user?

Close with one authority per fact class, provenance and version fields, validation before durable writes, conflict and deletion semantics, context-budget policy, poisoning defenses, and rebuild/repair paths. A vector store should normally be a retrieval index, not the sole authority for structured facts.

## Multi-agent coordination

Demand a reason that multiple agents exist beyond framework novelty:

- Who owns task decomposition, each subtask, shared state, final synthesis, and cancellation? Can two agents believe they own the same externally visible action?
- What is the handoff contract: typed input/output, evidence, assumptions, budget, deadline, version, and failure status? Can the receiver detect missing context?
- How are duplicate work, cyclic delegation, incompatible plans, conflicting facts, and contradictory recommendations detected and resolved?
- Is merge/arbitration performed by another nondeterministic model, a deterministic policy, a verifier, or a human? What prevents the arbiter from repeating the same failure mode?
- How are global step, token, tool, concurrency, and cost budgets enforced when children can spawn or retry work?
- What happens when a child completes after its task was cancelled or reassigned? Which generation/fencing value rejects the stale result?
- Against what single-agent baseline does the design improve success, latency, cost, safety, or fault isolation? Are gains maintained on hard slices rather than only aggregate demos?

Close with explicit ownership and handoff schemas, bounded delegation, stale-result rejection, merge policy, cancellation propagation, shared-state authority, and an eval showing why multi-agent complexity pays for itself.

## Evaluation and release gates

Attack the claim before accepting the metric:

- What task distribution, dataset version, sample size, source, labeling guide, and train/dev/test split support the result? Was the prompt or model tuned on the reported test set?
- Which failures require deterministic assertions, domain-expert review, pairwise human preference, or an LLM judge? Why is the chosen grader valid for that property?
- How was an LLM judge calibrated against blinded human labels? Report agreement, bias by model family or verbosity, and disagreement handling—not only judge score.
- Are confidence intervals, repeated runs, nondeterministic variance, and slice metrics reported? Could an aggregate improvement hide a safety-critical regression?
- What failure taxonomy separates routing, retrieval, prompt, tool, memory, policy, and model errors so fixes target the correct layer?
- Which thresholds block release, trigger shadow/canary evaluation, or force rollback? Are quality, safety, latency, and cost gates evaluated together?
- How are production feedback, abstentions, human overrides, and incident samples added without contaminating the locked test set or creating feedback loops?

Close with versioned datasets and graders, leakage controls, human calibration, uncertainty and slice reporting, multi-dimensional release gates, and post-release drift/rollback rules. “Accuracy improved” is unusable without this contract.

## Safety and human control

Test whether safety survives hostile inputs and component failure:

- Which inputs are untrusted: user text, webpages, files, retrieved chunks, tool output, memory, inter-agent messages, or all of them? How are instructions separated from data at each boundary?
- Are model credentials and tool privileges scoped by task, tenant, resource, action, and duration? Can a compromised prompt reach secrets or tools it never needed?
- Which controls are deterministic—schema validation, permission checks, allowlists, sandboxing, network/file isolation, rate limits—and which are probabilistic filters?
- Which actions require explicit user confirmation or human review, what exact intent is displayed, how long is approval valid, and what change invalidates it?
- How are secrets and PII prevented from entering prompts, traces, eval sets, memory, citations, and third-party providers? How are deletion and incident response propagated?
- What are the measured false-allow and false-refusal rates by risk slice? Can the system fail closed without making the product unusable?
- After an unsafe or incorrect action, what evidence supports containment, revocation, replay, compensation, user notification, and audit?

Close with threat boundaries, least-privilege execution, deterministic enforcement for high-risk actions, calibrated classifiers where judgment is unavoidable, human control for irreversible effects, and an incident/repair path. A system prompt is not an authorization boundary.

## Latency, token, and cost engineering

Interrogate end-to-end economics rather than quoting one model latency:

- Break P50/P95/P99 into queueing, orchestration, retrieval, reranking, model time-to-first-token, generation, tool calls, retries, approvals, and persistence. Which stage dominates each tail?
- How many model steps, input/output/cached tokens, retrieval calls, tool calls, repairs, retries, and fallbacks occur per successful task and per failed task?
- Does routing to a cheaper or faster model change task success, citation quality, safety, or retry rate enough to erase the savings?
- Are context pruning, prompt caching, semantic caching, batching, speculative work, or parallel tools safe for the task's freshness, privacy, and ordering requirements?
- How do timeouts and budgets degrade: partial answer, smaller model, reduced retrieval, user clarification, human handoff, or explicit failure? Which quality guarantees remain?
- Are costs attributed per tenant, feature, model, route, and successful task? Can one looping run exhaust shared budgets or starve other users?

Close with a measured stage breakdown, hard per-run budgets, quality-aware routing, tail-latency policy, cost per successful task, and graceful degradation that does not silently violate safety or grounding.

## Metrics and dangerous claims

Maintain Agent metrics with their denominator, dataset or traffic slice, grader, sample size, version bundle, uncertainty, and failure semantics:

- task success, step success, tool-call success, side-effect reconciliation, and human takeover;
- Recall@K, reranker metrics, groundedness, claim-level citation precision/recall, and evidence-absence abstention;
- invalid structured output, repair success, hallucination or unsupported-claim rate, and memory extraction precision;
- steps per run, retry distribution, repeated-state detection, loop exhaustion, cancellation, and stale-result rejection;
- P50/P95/P99 end-to-end and stage latency, tokens and cost per successful task, model/fallback mix, and cache effects;
- safety false allow/false refusal, approval rate, incident rate, and judge-human agreement.

Reject these claims unless the notebook supplies the missing contract:

- “accuracy” or “success rate” without task definition, dataset/traffic source, grader, sample size, slices, and confidence;
- “hallucinations reduced” without a supported-claim definition and evidence-grounded annotation method;
- “RAG improved quality” without separating retrieval and generation errors;
- “multi-agent improved reasoning” without a single-agent baseline and cost/latency comparison;
- “safe” because a system prompt, moderation call, or approval UI exists;
- “production reliable” because a demo or a few cherry-picked traces succeeded;
- “cost reduced” when retries, fallback, cached-token accounting, and success-rate changes are omitted.

## Completed-state closure

For every selected Agent mainline, freeze and cross-link:

1. the business objective and user-visible success/failure definition;
2. the durable run-state owner and deterministic final arbiter for any side effect;
3. prompt, model, tool-schema, retrieval-index, memory-schema, policy, and eval versions;
4. the nondeterministic boundary: acceptable variation, abstention, fallback, and escalation;
5. the context contract: sources, permissions, freshness, token allocation, truncation, and provenance;
6. the eval contract: dataset, grader, human calibration, slices, uncertainty, threshold, and release gate;
7. the safety and human-control boundary, including irreversible-action confirmation;
8. step/model/tool/token/cost and end-to-end latency budgets;
9. retry, replay, compensation, reconciliation, cancellation, and operator-repair paths;
10. the internal evidence label and speaking boundary for every qualitative or quantitative claim.

A completed-state Agent story is not closed merely because the model returns an answer. It is closed when probabilistic proposals are versioned and evaluated, deterministic effects remain safely arbitrated, failures converge, and the notebook can explain both capability and boundary under adversarial follow-up.
