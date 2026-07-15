# Module 2 — Machine Learning & Deep Learning

**Spec:** [Main README §7](../README.md#7-module-2--machine-learning--deep-learning) ·
**Status:** ⬜ Not started ·
**Deliverable:** `predictive-maintenance` ·
**Exit criterion:** beats majority-class baseline with a statistically defensible, documented margin

## Objective

Command the full supervised-learning workflow (leakage-safe pipelines, stratified CV, imbalance-aware metrics) and PyTorch training loops with reproducible results.

## Weekly checklist

- [ ] **W1:** Regression + L1/L2 regularization; residual analysis; scikit-learn `Pipeline`/`ColumnTransformer` (leakage prevention)
- [ ] **W2:** Classification zoo (logistic, trees, random forest, kNN); PR-AUC vs. ROC-AUC under imbalance; CV with confidence intervals
- [ ] **W3:** MLP forward/backward by hand (ties to Math B); PyTorch reimplementation; overfit-then-regularize exercise
- [ ] **W4:** Full PyTorch pipeline (DataLoader, early stopping, checkpointing, seeds); ablation table; deliverable freeze

## Deliverable requirements — `predictive-maintenance`

Dataset: **AI4I 2020 Predictive Maintenance** (UCI) or **NASA C-MAPSS** (RUL).

| ID | Requirement |
|---|---|
| FR-1 | Reproducible data pipeline (fixed splits, seeded), feature documentation |
| FR-2 | Baselines: logistic regression + random forest, stratified 5-fold CV |
| FR-3 | PyTorch MLP with early stopping; ablation over depth/dropout/BatchNorm |
| FR-4 | Report: PR-AUC (primary), ROC-AUC, F1 at cost-optimal threshold, calibration curve |

**Acceptance:** documented improvement over baseline · single-command reproduction (`make train && make report`).

## Planned layout

```
month-02-ml-dl/
├── notebooks/
├── project-predictive-maintenance/
│   ├── pyproject.toml
│   ├── src/
│   ├── tests/
│   └── Makefile
└── notes/
```

## Results

*Appended upon completion: metric table with CIs, ablations, calibration plot, post-mortem.*
