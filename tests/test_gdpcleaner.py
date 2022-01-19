"""Unit Tests for gdpcleaner.py"""
from gdphelper import gdpcleaner
import pandas as pd

# TEST 1: Test that gdpcleaner returns a dataframe and a string
input_dataframe = new pd.DataFrame(columns=['REF_DAT', 'GEO', 'Prices', 'SCALAR_FACTOR', 'VALUE'])
output_1, output_2 = gdpcleaner(input_dataframe)

assert type(output_1) == pd.DataFrame, "Output #1 is not a pandas DataFrame"
assert type(output_2) == str, "Output #2 is not a String"