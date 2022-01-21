#Unit Tests for gdpcleaner.py
from gdphelper import gdpcleaner
import pandas as pd
import pytest

@pytest.fixture
def input_frame():
   input_dataframe = pd.read_csv('example.csv')
   return input_data_frame

def test_correct_output():
    # TEST 1: Test that gdpcleaner returns a dataframe and a string
    output_1, output_2 = gdpcleaner(input_frame)

    assert type(output_1) == pd.DataFrame, "Output #1 is not a pandas DataFrame"
    assert type(output_2) == str, "Output #2 is not a String"

def test_correct_columns():
    #TEST 2: Test that the dataframe has the appropriate column names
    output_1, output_2 = gdpcleaner(input_frame)
    expected_columns=['Date', 'Location', 'Prices', 'Scale', 'Value']
    assertCountEqual(output.columns, expected_columns)

def test_column_count():
    #TEST 3: Test the dataframe has the correct column count
    output_1, output_2 = gdpcleaner(input_frame)
    assert len(output_1.columns) == 5, "Wrong number of columns"
