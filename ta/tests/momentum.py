import unittest

import pandas as pd

from ta.momentum import (KAMAIndicator, MFIIndicator, ROCIndicator,
                         RSIIndicator, StochasticOscillator, TSIIndicator,
                         UltimateOscillator, WilliamsRIndicator, roc)
from ta.tests.utils import TestIndicator


class TestRateOfChangeIndicator(TestIndicator):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:on_balance_volume_obv
    """

    _filename = 'ta/tests/data/cs-roc.csv'

    def test_roc(self):
        target = 'ROC'
        result = roc(close=self._df['Close'], n=12, fillna=False)
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_roc2(self):
        target = 'ROC'
        result = ROCIndicator(close=self._df['Close'], n=12, fillna=False).roc()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestRSIIndicator(unittest.TestCase):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:relative_strength_index_rsi
    Note: Using a more simple initilization (directly `ewm`; stockcharts uses `sma` + `ewm`)
    """

    _filename = 'ta/tests/data/cs-rsi.csv'

    def setUp(self):
        self._df = pd.read_csv(self._filename, sep=',')
        self._indicator = RSIIndicator(close=self._df['Close'], n=14, fillna=False)

    def tearDown(self):
        del(self._df)

    def test_rsi(self):
        target = 'RSI'
        result = self._indicator.rsi()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestMFIIndicator(unittest.TestCase):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:money_flow_index_mfi
    """

    _filename = 'ta/tests/data/cs-mfi.csv'

    def setUp(self):
        self._df = pd.read_csv(self._filename, sep=',')
        self._indicator = MFIIndicator(
            high=self._df['High'], low=self._df['Low'], close=self._df['Close'], volume=self._df['Volume'], n=14,
            fillna=False)

    def tearDown(self):
        del(self._df)

    def test_mfi(self):
        target = 'MFI'
        result = self._indicator.money_flow_index()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestUltimateOscillator(unittest.TestCase):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:ultimate_oscillator
    """

    _filename = 'ta/tests/data/cs-ultosc.csv'

    def setUp(self):
        self._df = pd.read_csv(self._filename, sep=',')
        self._indicator = UltimateOscillator(
            high=self._df['High'], low=self._df['Low'], close=self._df['Close'],
            s=7, m=14, len=28, ws=4.0, wm=2.0, wl=1.0, fillna=False)

    def tearDown(self):
        del(self._df)

    def test_uo(self):
        target = 'Ult_Osc'
        result = self._indicator.uo()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestStochasticOscillator(unittest.TestCase):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:stochastic_oscillator_fast_slow_and_full
    """

    _filename = 'ta/tests/data/cs-soo.csv'

    def setUp(self):
        self._df = pd.read_csv(self._filename, sep=',')
        self._indicator = StochasticOscillator(
            high=self._df['High'], low=self._df['Low'], close=self._df['Close'], n=14, d_n=3, fillna=False)

    def tearDown(self):
        del(self._df)

    def test_so(self):
        target = 'SO'
        result = self._indicator.stoch()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_so_signal(self):
        target = 'SO_SIG'
        result = self._indicator.stoch_signal()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestWilliamsRIndicator(unittest.TestCase):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:williams_r
    """

    _filename = 'ta/tests/data/cs-percentr.csv'

    def setUp(self):
        self._df = pd.read_csv(self._filename, sep=',')
        self._indicator = WilliamsRIndicator(
            high=self._df['High'], low=self._df['Low'], close=self._df['Close'], lbp=14, fillna=False)

    def tearDown(self):
        del(self._df)

    def test_wr(self):
        target = 'Williams_%R'
        result = self._indicator.wr()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestKAMAIndicator(unittest.TestCase):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:kaufman_s_adaptive_moving_average
    """

    _filename = 'ta/tests/data/cs-kama.csv'

    def setUp(self):
        self._df = pd.read_csv(self._filename, sep=',')
        self._indicator = KAMAIndicator(close=self._df['Close'], n=10, pow1=2, pow2=30, fillna=False)

    def tearDown(self):
        del(self._df)

    def test_kama(self):
        target = 'KAMA'
        result = self._indicator.kama()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestTSIIndicator(unittest.TestCase):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:true_strength_index
    """

    _filename = 'ta/tests/data/cs-tsi.csv'

    def setUp(self):
        self._df = pd.read_csv(self._filename, sep=',')
        self._indicator = TSIIndicator(close=self._df['Close'], r=25, s=13, fillna=False)

    def tearDown(self):
        del(self._df)

    def test_kama(self):
        target = 'TSI'
        result = self._indicator.tsi()
        pd.testing.assert_series_equal(
            self._df[target].tail(), result.tail(), check_names=False, check_less_precise=True)
