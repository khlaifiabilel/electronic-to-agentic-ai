# Agentic Design Pattern Library

**Spec:** [Main README §10.1](../../README.md#10-module-5--agentic-architectures--design-patterns) ·
**Status:** ⬜ Not started

Five canonical patterns (Anthropic, *Building Effective Agents*; Ng's taxonomy), each implemented as a **minimal, tested, reusable LangGraph graph** — deliberately small so they can be composed into Module 5/6 systems.

| # | Pattern | Mechanism | Use when | Module file | Status |
|---|---|---|---|---|:---:|
| 1 | Routing | Classifier node directs to specialist subgraph | Heterogeneous input classes | `routing.py` | ⬜ |
| 2 | Parallelization | Fan-out/fan-in (sectioning or voting) | Independent subtasks; ensemble judgment | `parallelization.py` | ⬜ |
| 3 | Orchestrator–workers | Dynamic decomposition and delegation | Unpredictable subtask structure | `orchestrator_workers.py` | ⬜ |
| 4 | Evaluator–optimizer | Generator + critic loop against a rubric, bounded iterations | Quality thresholds, iterative repair | `evaluator_optimizer.py` | ⬜ |
| 5 | Reflection | Self-critique pass over own output | Error-prone generation (code) | `reflection.py` | ⬜ |

## Per-pattern definition of done

- [ ] Typed `StateGraph` with documented state schema and reducers
- [ ] Termination guards (max iterations / explicit exit conditions)
- [ ] Unit tests with a mocked LLM (deterministic fixtures)
- [ ] LangSmith tracing enabled; one recorded example trace
- [ ] Docstring: mechanism, when-to-use, failure modes

## Planned layout

```
patterns/
├── pyproject.toml
├── src/patterns/
│   ├── routing.py
│   ├── parallelization.py
│   ├── orchestrator_workers.py
│   ├── evaluator_optimizer.py
│   └── reflection.py
└── tests/
```
