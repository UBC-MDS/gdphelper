from gdphelper.gdpimporter import gdpimporter
import os
import pandas as pd
import pytest

def test_gdp_importer_return_type():
    """Test the return type of gdpimporter."""
    out_df, out_str = gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip")
    assert isinstance(out_df, pd.core.frame.DataFrame), "The first element of the returned tuple is not a pandas dataframe!"
    assert out_str == 'Gross domestic product (GDP) at basic prices, by industry, provinces and territories, percentage share', "The title information from MetaData is not correctly extracted!"

def test_gdp_importer_download_data():
    """Test if gdpimporter unzips the file and rename the csv as expected."""
    # if filename is not specified
    gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip")
    assert os.path.isfile('open_canada_data.csv'), "The csv data file is not upzipped and/or renamed correctly!"
    # if filename is specified
    gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100401-eng.zip", filename='gdp_census')
    assert os.path.isfile('gdp_census.csv'), "The csv data file is not upzipped and/or renamed correctly!"

def test_gdp_importer_unzip_all():
    """Test if gdpimporter unzips files without further renaming them."""
    gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100401-eng.zip", filetype='all')
    assert os.path.isfile('36100401.csv'), "The csv data file is not upzipped and/or has wrong file name!"


def test_gdp_importer_filename_error():
    """Check TypeError raised when 'filename' is not None (default) or a string."""
    with pytest.raises(TypeError):
        gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip", filename=['gdp2021_data'])


def test_gdp_importer_filetype_error():
    """Check ValueError raised when 'filetype' is not 'csv' or 'all'."""
    with pytest.raises(ValueError):
        gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip", filetype='dat')


def test_gdp_importer_url_error():
    """Check ValueError raised when 'url' is not valid."""
    with pytest.raises(ValueError):
        gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.csv", filename='gdp2021_data')
           