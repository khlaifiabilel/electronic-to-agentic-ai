# Module 1 — Scientific Python & Software Engineering

**Spec:** [Main README §6](../README.md#6-module-1--scientific-python--software-engineering) ·
**Status:** ⬜ Not started ·
**Deliverable:** `sensor-analyzer` ·
**Exit criterion:** coverage ≥ 80% · 1M-row end-to-end < 10 s · zero mypy errors

## Objective

Convert C/C++ fluency into production-quality Python and vectorized numerical computing; establish the engineering baseline (uv, ruff, mypy, pytest, pre-commit, CI) used by all later modules.

## Weekly checklist

- [ ] **W1:** Toolchain bootstrap (Python 3.11, uv, VS Code, Git); syntax deep-dive with C/C++ contrast table; first typed, tested CLI utility
- [ ] **W2:** OOP (dunder protocol, composition vs. inheritance, ABCs vs. `Protocol`); packaging; exception design; structured logging
- [ ] **W3:** NumPy internals (dtypes, strides, broadcasting) + Pandas pipelines on sensor CSVs; profiling; vectorization benchmark (target ≥ 50× vs. loops)
- [ ] **W4:** Matplotlib diagnostics (time series, FFT spectrograms); project assembly; coverage ≥ 80%; CI green

## Deliverable requirements — `sensor-analyzer`

| ID | Requirement |
|---|---|
| FR-1 | Schema validation and unit normalization on ingest |
| FR-2 | Cleaning: gap interpolation policy, spike rejection (Hampel filter), drift detection via rolling z-score |
| FR-3 | Anomaly report: threshold + k·σ violations with timestamps → Markdown + PNG |
| FR-4 | FFT-based periodicity summary per channel |

**Acceptance:** ≥ 80% test coverage · 1M rows < 10 s · zero mypy errors.

## Planned layout

```
month-01-python/
├── notebooks/                 # exploration only; logic lives in src/
├── project-sensor-analyzer/
│   ├── pyproject.toml
│   ├── src/sensor_analyzer/
│   └── tests/
└── notes/
```

## Results

*Appended upon completion: benchmark table, coverage report, post-mortem.*
