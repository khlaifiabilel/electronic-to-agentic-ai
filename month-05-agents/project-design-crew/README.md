# `design-crew` — Multi-Agent Electronic-Design Assistant

**Spec:** [Main README §10.3](../../README.md#10-module-5--agentic-architectures--design-patterns) ·
**Status:** ⬜ Not started ·
**Orchestration:** CrewAI or LangGraph (decision recorded in W4 comparison note)

## Roles

| Agent | Responsibility | Key tools |
|---|---|---|
| Researcher | Component specs via datasheet RAG (Module 4 index) | `datasheet-rag` retriever |
| Design Engineer | Topology + engineering calculations (dividers, pull-ups, RC filters) | Deterministic Python calc tools |
| Reviewer | Rubric-based critique; evaluator–optimizer loop | Rubric + patterns library |
| Technical Writer | Structured design dossier | Template renderer |

## Requirements

| ID | Requirement |
|---|---|
| FR-1 | Four roles wired as above; Reviewer runs an evaluator–optimizer loop |
| FR-2 | All numeric engineering claims produced by deterministic Python tools — never LLM arithmetic |
| FR-3 | Full LangSmith trace; per-run cost and token report |
| FR-4 | Reviewer must catch seeded faults: missing decoupling, wrong divider ratio, absent current-limit check |

**Acceptance:** 3 seeded-fault scenarios caught · dossiers generated for 2 reference briefs · cost/run documented.

## Evaluation assets

- [ ] `briefs/` — 2 reference design briefs (e.g., 5 V→3.3 V sensor interface; debounced button + LED PWM)
- [ ] `seeded-faults/` — 3 deliberately flawed intermediate designs for Reviewer testing

## Results

*Appended upon completion: dossiers, trace links, fault-detection matrix, cost table, post-mortem.*
