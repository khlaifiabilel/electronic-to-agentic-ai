# Module 5 — Agentic Architectures & Design Patterns

**Spec:** [Main README §10](../README.md#10-module-5--agentic-architectures--design-patterns) ·
**Status:** ⬜ Not started ·
**Deliverables:** [`patterns/`](patterns/) library + [`project-design-crew/`](project-design-crew/) ·
**Exit criterion:** 5 patterns implemented and tested · seeded-fault scenarios caught by Reviewer loop

## Objective

Treat agents as engineered state machines: implement the canonical agentic design patterns as reusable, tested LangGraph components, then compose them into a role-specialized multi-agent system (CrewAI or LangGraph orchestration).

## Weekly checklist

- [ ] **W1:** Tool-calling agent from raw API (no framework) — schemas, Pydantic validation, retry envelope; rebuild in LangGraph; document the control delta
- [ ] **W2:** LangGraph deep-dive: typed state + reducers, conditional edges, checkpointing, HITL interrupt; LangSmith spans on every node
- [ ] **W3:** Pattern library: routing, parallelization, orchestrator–workers, evaluator–optimizer, reflection ([`patterns/`](patterns/))
- [ ] **W4:** CrewAI vs. AutoGen comparative build; architecture selection; assemble and evaluate [`project-design-crew/`](project-design-crew/)

## Sub-deliverables

| Path | Content | Acceptance |
|---|---|---|
| `patterns/` | Five minimal, tested, reusable LangGraph graphs | Each: unit-tested, traced, documented with a mechanism/use-when note |
| `project-design-crew/` | Multi-agent electronic-design assistant | 3 seeded-fault scenarios caught; 2 reference-brief dossiers; cost/run documented |

## Results

*Appended upon completion: framework comparison notes, trace links, cost/token report, post-mortem.*
