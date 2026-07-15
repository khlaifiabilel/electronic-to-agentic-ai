# Mathematical Foundations Track (Months 1–3)

**Spec:** [Main README §5](../README.md#5-mathematical-foundations-track-months-13) ·
**Status:** ⬜ Not started ·
**Load:** 2–3 h/week, parallel to Modules 1–3

Primary resource: [Steve Brunton — @Eigensteve](https://www.youtube.com/@Eigensteve) ·
Companion text: Brunton & Kutz, *Data-Driven Science and Engineering* ([databookuw.com](http://databookuw.com))

## Deliverables

| Module | Notebook | Verification |
|---|---|---|
| A — Linear algebra (Month 1) | `notebooks/a-svd-pca.ipynb` — SVD image compression + PCA on sensor telemetry | Rank-r reconstruction error curve; PCA ≡ SVD demonstrated numerically |
| B — Calculus & optimization (Month 2) | `notebooks/b-backprop.ipynb` — manual backprop on a 2-layer MLP | Gradients match `torch.autograd` to `1e-6` |
| C — Probability & statistics (Month 3) | `notebooks/c-mle-crossentropy.ipynb` — MLE for a sensor-noise model; cross-entropy vs. KL study | MLE recovers known parameters within CI; CE/KL identity verified numerically |

## Checklist

- [ ] A1 — Vector spaces, norms, orthogonality (Eigensteve linear algebra series)
- [ ] A2 — Eigendecomposition; SVD: low-rank approximation, condition number
- [ ] A3 — PCA–SVD equivalence; embedding geometry / cosine similarity
- [ ] A4 — Notebook `a-svd-pca.ipynb` committed
- [ ] B1 — Partial derivatives, Jacobians, chain rule
- [ ] B2 — Backpropagation derivation by hand
- [ ] B3 — GD → SGD → momentum → Adam; LR schedules
- [ ] B4 — Notebook `b-backprop.ipynb` committed (autograd-verified)
- [ ] C1 — Random variables, distributions, expectation/variance
- [ ] C2 — MLE; Bayes' theorem
- [ ] C3 — Entropy, cross-entropy, KL divergence as loss functions
- [ ] C4 — Notebook `c-mle-crossentropy.ipynb` committed

## Planned layout

```
math-foundations/
├── notebooks/
│   ├── a-svd-pca.ipynb
│   ├── b-backprop.ipynb
│   └── c-mle-crossentropy.ipynb
└── notes/          # derivations, summaries per module
```

## Results

*Appended upon completion: key takeaways, numeric verification outputs, open questions.*
