"""Vectorized statistics primitives for sensor telemetry analysis.

This module is the reference implementation pattern for the project:
fully typed, NumPy-vectorized, and unit-tested. Extend it with the
Hampel filter (FR-2) and FFT periodicity primitives (FR-4).
"""

from __future__ import annotations

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from numpy.typing import ArrayLike, NDArray

__all__ = ["rolling_zscore"]


def rolling_zscore(values: ArrayLike, window: int) -> NDArray[np.float64]:
    """Compute the trailing-window z-score of a 1-D signal.

    Each output sample ``z[i]`` measures how far ``values[i]`` deviates from
    the mean of the trailing window ``values[i - window + 1 : i + 1]``, in
    units of that window's population standard deviation (``ddof=0``).
    Intended for drift and spike screening (FR-2).

    Parameters
    ----------
    values : ArrayLike
        One-dimensional numeric signal with at least ``window`` samples.
    window : int
        Trailing window length, ``>= 2``.

    Returns
    -------
    NDArray[np.float64]
        Array with the same shape as ``values``. The first ``window - 1``
        samples are ``nan`` (insufficient history); samples whose window has
        zero variance are also ``nan``.

    Raises
    ------
    ValueError
        If ``window < 2``, ``values`` is not one-dimensional, or ``values``
        is shorter than ``window``.
    """
    x = np.asarray(values, dtype=np.float64)
    if window < 2:
        raise ValueError(f"window must be >= 2, got {window}")
    if x.ndim != 1:
        raise ValueError(f"values must be one-dimensional, got ndim={x.ndim}")
    if x.size < window:
        raise ValueError(f"values needs at least {window} samples, got {x.size}")

    windows = sliding_window_view(x, window)  # shape: (n - window + 1, window)
    mean = windows.mean(axis=1)
    std = windows.std(axis=1)  # population std (ddof=0)

    z = np.full(x.shape, np.nan, dtype=np.float64)
    tail = np.arange(window - 1, x.size)
    stable = std > 0.0
    z[tail[stable]] = (x[tail[stable]] - mean[stable]) / std[stable]
    return z
