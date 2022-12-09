import pytest
from pandas.core.groupby.generic import DataFrameGroupBy
from units.reader import ReadCsv

csv = ReadCsv('./input.csv')


def test_read_csv():
    assert isinstance(csv._get_grouped(), DataFrameGroupBy)
