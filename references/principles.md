# Principles

## Priority order

Interview usefulness > narrative coherence > literal mirroring of code names.

Use this order when repository artifacts disagree. Optimize the notebook for a technically valuable and defensible interview conversation, then make every page share one coherent story. Do not weaken that story merely because a class, comment, test name, or partial implementation uses a narrower term.

Interview usefulness does not justify an incoherent claim. Revise a claim when it conflicts with another résumé or notebook claim, or when its mechanism cannot survive reasonable follow-up questions.

## Completed-state narrative

Present the frozen final design as the project's implemented interview narrative. Do not organize the story as a sequence of unfinished migrations. Preserve internal calibration through evidence labels.

Use completed-state language consistently in the résumé, project introduction, architecture pages, diagrams, question trees, deployment story, and quick-reference card. Avoid phrases such as “后续演进”, “计划支持”, or “未来再做” for mechanisms included in the frozen design.

Code, documentation, tests, and old notes are inputs to the narrative, not separate authorities. Strengthen missing transaction boundaries, recovery paths, and operational details before deleting worthwhile technical depth. Do not invent a second architecture merely to explain an isolated artifact.

## Internal labels

- `[已验证]`: executable or inspectable evidence exists.
- `[完成态口径]`: frozen final narrative, spoken as implemented.
- `[容量估算]`: reasoned sizing model, not an executed benchmark.
- `[边界条件]`: failure boundary, degradation rule, or non-goal.

Use labels for internal calibration and review, not as verbal disclaimers mechanically inserted into résumé bullets or every interview answer. Every quantitative claim has exactly one primary classification. A verified component result may support a completed-state design, but it does not turn an unexecuted end-to-end capacity claim into `[已验证]`.

When repository instructions distinguish actual execution evidence from design claims, preserve that distinction with these labels while keeping the completed-state design as the interview narrative. Never claim that a command, test, benchmark, deployment, or external action was actually executed unless it was.

## Quantitative claims

Centralize each number in the unified metrics page. Record its class, assumptions, calculation or source, and speaking boundary. Never derive a strict data-loss bound from an unrelated persistence interval.

For each number, record:

- the business or technical quantity being measured;
- its primary evidence label;
- workload, data volume, concurrency, topology, and resource assumptions;
- the calculation, benchmark source, or acceptance definition;
- latency percentile and error semantics when performance is discussed;
- where the number may and may not be reused in speech or résumé text.

Prefer a small set of consistent, explainable numbers over many impressive but incompatible figures. Treat design capacity, acceptance targets, observed baselines, and production traffic as different quantities even when their values are similar.

## Mechanism closure

For each claim identify the source of truth, final arbiter, idempotency key, state transition guard, failure recovery, and explicit limit.

Also make the business reason and rejected alternatives explainable. A mechanism is closed only when the normal path and the duplicate, delayed, reordered, partially failed, restarted, and degraded paths converge without contradicting its data ownership or deployment topology.

Do not add a technology solely as an interview keyword. Keep it only when the notebook can answer:

- Why is it needed for this business problem?
- What invariant does it protect?
- Which component decides the final result?
- What happens when it is unavailable or loses transient state?
- How is the system repaired or reconciled?
- Why was a plausible alternative not selected?
- What scale or boundary makes the choice reasonable?

## Scope and authorization

Treat the repository as read-only input unless the user separately asks for code changes. Do not push, publish, or mutate external systems as part of notebook generation.

Resolve and obtain any required authorization before writing outside the repository, including an Obsidian Vault. Keep generated notebooks in the agreed destination. Do not modify application code, tests, schemas, configuration, Git history, remote services, or deployment state merely to make the narrative match.

Repository-local instructions still govern repository access and real command execution. If they conflict with the requested interview narrative, record the distinction through internal labels rather than silently changing either the repository or the completed-state fact model.
