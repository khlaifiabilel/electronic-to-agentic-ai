# `sensor-analyzer`

Module 1 deliverable — see [module README](../README.md) for requirements (FR-1…FR-4) and
[main README §6](../../README.md#6-module-1--scientific-python--software-engineering) for the full spec.

## Quick start

```bash
uv sync                    # create .venv and install (locked)
uv run pytest              # tests + coverage gate (>= 80%)
uv run ruff check .        # lint
uv run ruff format .       # format
uv run mypy                # strict type-check on src/
```

## Status

- [x] Project skeleton: typed package, tests, lint/typecheck/test tooling, CI green
- [ ] FR-1 — ingest: schema validation, unit normalization
- [ ] FR-2 — cleaning: gap interpolation, Hampel filter, drift detection (`rolling_zscore` primitive available in `stats.py`)
- [ ] FR-3 — anomaly report: threshold + k·σ violations → Markdown + PNG
- [ ] FR-4 — FFT periodicity summary per channel
- [ ] CLI entry point (`sensor-analyzer <input.csv> --report out/`)
- [ ] Acceptance run: 1M rows < 10 s, coverage >= 80%, zero mypy errors

`src/sensor_analyzer/stats.py` is the reference implementation pattern: fully typed,
NumPy-vectorized, NumPy-style docstrings, unit-tested. Extend the package following it.
