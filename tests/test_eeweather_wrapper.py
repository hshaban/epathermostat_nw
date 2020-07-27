from thermostat.eeweather_wrapper import get_indexed_temperatures_eeweather

import pytest
import pandas as pd


from .fixtures.thermostats import thermostat_type_1


def test_get_indexed_temperatures_eeweather_empty_index():
    empty_index = pd.DataFrame()
    results = get_indexed_temperatures_eeweather('720113', empty_index)
    assert results.empty is True


def test_get_index_temperatures_eeweather():
    begin_timestamp = pd.Timestamp('2011-01-01 00:00:00')
    periods = 35064
    hourly_index = pd.date_range(begin_timestamp, periods=periods, freq="H")
    results = get_indexed_temperatures_eeweather('720113', hourly_index)
    assert results.shape == (35064,)
