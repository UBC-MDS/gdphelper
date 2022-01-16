from gdphelper.gdpimporter import gdpimporter
import os
import pandas as pd

def test_gdp_importer_return_type():
    """Test the return type of gdpimporter."""
    out_df, out_str = gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip")
    assert isinstance(out_df, pd.core.frame.DataFrame), "The first element of the returned tuple is not a pandas dataframe!"
    # assert isinstance(out_str, str), "The second element of the returned tuple is not a string!"
    assert out_str == 'Gross domestic product (GDP) at basic prices, by industry', "The title information from MetaData is not correctly extracted!"

def test_gdp_importer_download_data():
    """Test if gdpimporter unzips the file and rename the csv as expected."""
    # if filename is not specified
    gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip")
    assert os.path.isfile('data_opencan.csv'), "The csv data file is not upzipped and/or renamed correctly!"
    assert '36100400_MetaData.csv' in os.listdir(), "The metadata csv is not properly unzipped."
    # if filename is specified
    gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100401-eng.zip", filename='gdp_census')
    assert os.path.isfile('gdp_census.csv'), "The csv data file is not upzipped and/or renamed correctly!"
    assert '36100401_MetaData.csv' in os.listdir(), "The metadata csv is not properly unzipped."

def test_gdp_importer_unzip_all():
    """Test if gdpimporter unzips all files without further renaming them."""
    gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100401-eng.zip", filetype='all')
    assert os.path.isfile('36100401.csv'), "The csv data file is not upzipped and/or has wrong file name!"
    assert os.path.isfile('36100401_MetaData.csv'), "The metadata csv is not properly unzipped!"
