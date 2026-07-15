# Module 3 — NLP & Transformer/LLM Internals

**Spec:** [Main README §8](../README.md#8-module-3--nlp--transformerllm-internals) ·
**Status:** ⬜ Not started ·
**Deliverable:** `component-support-nlp` ·
**Exit criterion:** macro-F1 ≥ documented baseline · 100% structured-output schema validity

## Objective

Understand Transformer internals (attention, KV cache, positional encodings, sampling) deeply enough to predict system behavior, and fine-tune pretrained models (full FT vs. LoRA/PEFT).

## Weekly checklist

- [ ] **W1:** Tokenizer lab (train small BPE; inspect with `tiktoken`); embedding-space probing with sentence-transformers
- [ ] **W2:** Attention from scratch (NumPy/PyTorch, single → multi-head, shape-verified); annotated read of Vaswani et al. 2017; Karpathy GPT build
- [ ] **W3:** Fine-tune DistilBERT (HF `Trainer`) vs. LoRA (`peft`); quality / VRAM / wall-clock comparison table
- [ ] **W4:** OpenAI API engineering: structured outputs (strict JSON schema), function-calling primer, streaming, cost instrumentation; deliverable freeze

## Deliverable requirements — `component-support-nlp`

| ID | Requirement |
|---|---|
| FR-1 | Fine-tuned DistilBERT (full FT and LoRA variants), macro-F1 on held-out set |
| FR-2 | Token/cost accounting middleware for all API calls; retry with exponential backoff |
| FR-3 | Structured extraction: free-text ticket → typed Pydantic record (component, symptom, severity) |

**Acceptance:** macro-F1 ≥ baseline + top-10 confusion error analysis · 100% schema-valid extractions on test prompts.

## Planned layout

```
month-03-nlp-llm/
├── notebooks/
│   └── attention-from-scratch.ipynb
├── project-component-support-nlp/
│   ├── pyproject.toml
│   ├── src/
│   └── tests/
└── notes/
```

## Results

*Appended upon completion: FT vs. LoRA table, error analysis, post-mortem.*
