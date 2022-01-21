#Unit Tests for gdpcleaner.py
from gdphelper import gdpcleaner
import pandas as pd
import pytest

@pytest.fixture
def input_frame():
   input_dataframe = pd.read_csv('example.csv')
   return input_dataframe

def test_correct_output():
    # TEST 1: Test that gdpcleaner returns a dataframe and a string
    output_1 = gdpcleaner(input_frame)

    assert type(output_1) == pd.DataFrame, "Output #1 is not a pandas DataFrame"

def test_column_count():
    #TEST 2: Test the dataframe has the correct column count
    output_1 = gdpcleaner(input_frame)
    assert len(output_1.columns) >= 5, "Wrong number of columns"

def test_empty():
    #TEST 3: Check the dataframe is not empty
    output_1 = gdpcleaner(input_frame)
    assert len(output_1) != 0, "Dataframe should not be empty!"

def test_column_names():
    #TEST 4: Any unaccounted for columns in output
    output_1 = gdpcleaner(input_frame)

    for c in output_1.columns:
        assert c in any("Date", "Location", "Scale", "Unit", "Value", "NAICS_Class", "Industry", "Sub-sector", "Special_Industry"), "Unknown Column in output"