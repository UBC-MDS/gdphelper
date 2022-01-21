#Unit Tests for gdpcleaner.py
from gdphelper.gdpcleaner import gdpcleaner
import pandas as pd
import pytest

@pytest.fixture
def input_frame():
   input_dataframe = pd.read_csv('tests/test_13100347.csv')
   return input_dataframe

def test_correct_output():
    # TEST 1: Test that gdpcleaner returns a dataframe and a string
    output_1 = gdpcleaner(pd.read_csv('tests/test_13100347.csv'))

    assert isinstance(output_1, pd.core.frame.DataFrame), "Output is not a pandas DataFrame"

def test_column_count():
    #TEST 2: Test the dataframe has the correct column count
    output_1 = gdpcleaner(pd.read_csv('tests/test_13100347.csv'))
    assert len(output_1.columns) >= 5, "Wrong number of columns"

def test_empty():
    #TEST 3: Check the dataframe is not empty
    output_1 = gdpcleaner(pd.read_csv('tests/test_13100347.csv'))
    assert len(output_1) != 0, "Dataframe should not be empty!"
