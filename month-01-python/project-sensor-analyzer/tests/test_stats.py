"""Unit tests for sensor_analyzer.stats."""

import math

import numpy as np
import pytest

from sensor_analyzer import rolling_zscore


class TestRollingZscore:
    def test_known_values_linear_ramp(self) -> None:
        z = rolling_zscore([1.0, 2.0, 3.0, 4.0], window=3)
        # For a linear ramp, (x - mean) / population_std == sqrt(1.5) at each full window.
        expected = math.sqrt(1.5)
        np.testing.assert_allclose(z[2:], [expected, expected], rtol=1e-12)

    def test_warmup_region_is_nan(self) -> None:
        z = rolling_zscore(np.arange(10, dtype=float), window=4)
        assert np.isnan(z[:3]).all()
        assert not np.isnan(z[3:]).any()

    def test_constant_signal_yields_nan(self) -> None:
        z = rolling_zscore(np.ones(8), window=3)
        assert np.isnan(z).all()

    def test_step_change_is_flagged(self) -> None:
        signal = np.concatenate([np.zeros(20), [10.0]])
        z = rolling_zscore(signal, window=10)
        # Zero-variance windows are nan; the step's window has mean 1, std 3.
        assert np.isnan(z[:-1]).all()
        assert z[-1] == pytest.approx(3.0)

    def test_accepts_plain_lists(self) -> None:
        z = rolling_zscore([0.0, 0.0, 1.0], window=2)
        assert np.isnan(z[0])
        assert z[1] is not None

    @pytest.mark.parametrize("window", [-1, 0, 1])
    def test_window_too_small_raises(self, window: int) -> None:
        with pytest.raises(ValueError, match="window must be >= 2"):
            rolling_zscore([1.0, 2.0, 3.0], window=window)

    def test_non_1d_raises(self) -> None:
        with pytest.raises(ValueError, match="one-dimensional"):
            rolling_zscore(np.zeros((3, 3)), window=2)

    def test_shorter_than_window_raises(self) -> None:
        with pytest.raises(ValueError, match="needs at least"):
            rolling_zscore([1.0, 2.0], window=3)
