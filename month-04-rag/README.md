# Module 4 — Prompt Engineering & Retrieval-Augmented Generation

**Spec:** [Main README §9](../README.md#9-module-4--prompt-engineering--retrieval-augmented-generation) ·
**Status:** ⬜ Not started ·
**Deliverable:** `datasheet-rag` ·
**Exit criterion:** faithfulness ≥ 0.85 · context precision ≥ 0.75 · 0 fabricated citations · ≥ 8/10 correct refusals

> Note: the RAG index built here is a **runtime dependency of the capstone** (Module 6).

## Objective

Build retrieval systems whose answers are grounded, cited, and quantitatively evaluated: hybrid retrieval (dense + BM25 + RRF), cross-encoder re-ranking, layout-aware PDF chunking, RAGAS evaluation.

## Weekly checklist

- [ ] **W1:** Prompt-technique matrix (zero/few-shot, CoT, self-consistency) benchmarked with deterministic decoding; prompt regression file established
- [ ] **W2:** Embedding + ChromaDB lab: HNSW parameter sweep (`M`, `ef_construction`, `ef_search`) with recall@k / latency plots; metadata-filtered retrieval
- [ ] **W3:** End-to-end RAG over ≥ 10 real datasheets (STM32 RM excerpts, LM317, DHT22, …); chunking ablation (fixed vs. recursive vs. layout-aware)
- [ ] **W4:** Hybrid retrieval + re-ranking; RAGAS harness; adversarial hallucination audit; deliverable freeze

## Deliverable requirements — `datasheet-rag`

| ID | Requirement |
|---|---|
| FR-1 | Ingestion: PDF → structured chunks with `{part, section, page}` metadata |
| FR-2 | Hybrid retrieval (dense + BM25 + RRF), cross-encoder re-rank, configurable top-k |
| FR-3 | Answers cite `(document, page)`; refusal path when context is insufficient |
| FR-4 | RAGAS report on ≥ 50-question golden set incl. 10 adversarial (unanswerable) questions |

**Acceptance:** faithfulness ≥ 0.85 · context precision ≥ 0.75 · 0 fabricated citations · ≥ 8/10 correct refusals.

## Planned layout

```
month-04-rag/
├── corpus/                    # datasheet PDFs (or download script + manifest)
├── project-datasheet-rag/
│   ├── pyproject.toml
│   ├── src/
│   ├── eval/                  # golden set + RAGAS harness
│   └── tests/
└── notes/
```

## Results

*Appended upon completion: RAGAS table, HNSW sweep plots, chunking ablation, post-mortem.*
