# EmbedAI Copilot — Capstone

**Spec:** [Main README §12](../../README.md#12-capstone-specification--embedai-copilot) (architecture, FR/NFR, acceptance) and [§11](../../README.md#11-module-6--evaluation-deployment--capstone) (evaluation, deployment, security) ·
**Status:** ⬜ Not started ·
**One-line spec:** natural-language firmware specification → grounded, reviewed, **compile-validated** Arduino/STM32 code with citations and full traceability.

## Pipeline (summary)

`FastAPI (SSE)` → `LangGraph orchestrator` → Spec Analyst → Retriever (Module 4 RAG index) → Code Generator → Critic → **PlatformIO compile sandbox** (repair loop ≤ 3, evaluator–optimizer) → artifact bundle. Every run traced in LangSmith.

## Key acceptance targets (§12.3)

| Category | Target | Status |
|---|---|:---:|
| Correctness | ≥ 85% compile-pass on held-out 25-prompt eval set | ⬜ |
| Grounding | 0 fabricated citations; hallucinated-pin rate = 0 | ⬜ |
| Security | ≥ 90% of 20-case injection corpus neutralized; sandbox-only execution | ⬜ |
| Latency / cost | p95 ≤ documented budget; per-request cost bounded | ⬜ |
| Reproducibility | `docker compose up` from clean clone; CI golden-set regression | ⬜ |
| Documentation | Architecture doc, runbook, demo video, failure post-mortem | ⬜ |

## Build checklist (Module 6 weekly plan)

- [ ] **W1:** LangSmith eval stack — golden datasets, custom evaluators, CI regression gate
- [ ] **W2:** FastAPI + SSE serving; Docker multi-stage images; Streamlit console; p95 smoke test
- [ ] **W3:** Security hardening — injection corpus (≥ 20 cases), tool privilege matrix, no-network compile sandbox, output validators
- [ ] **W4:** Integration, full evaluation run, documentation, demo recording, **v1.0 tag**

## Planned layout

```
embedai-copilot/
├── pyproject.toml
├── docker-compose.yml
├── src/
│   ├── api/                # FastAPI gateway (auth, rate limit, SSE)
│   ├── graph/              # LangGraph orchestrator + agents
│   ├── tools/              # RAG retriever, calc tools, compile validator
│   └── schemas/            # FirmwareSpec and artifact models (Pydantic)
├── sandbox/                # PlatformIO Docker image (no network, resource-limited)
├── eval/                   # 25-prompt eval set + injection corpus + harness
├── ui/                     # Streamlit operator console
└── tests/
```

## Results

*Appended at v1.0: acceptance table (green/red), eval metrics, cost/latency report, demo link, post-mortem.*
