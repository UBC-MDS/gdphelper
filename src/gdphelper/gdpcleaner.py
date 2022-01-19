import pandas as pd
def gdpcleaner(gdpdata: pd.DataFrame):
    """Remove spurious columns, Rename relevant columns, Scrub any string artifacts (eg [T008])


    Parameters
    ----------
    gdpdata: DataFrame 
    a loaded dataframe based on a downloaded Open Government GDP at basic prices dataset (https://open.canada.ca/en/open-data)


    Returns
    -------
    DataFrame:  A cleaned and simplified DataFrame of the relevant columns for summary and visualization


    Examples
    --------
    #>>> result = gdpcleaner(example_data)
    """
    cleaned_frame = gdpdata['REF_DAT', 'GEO', 'Prices', 'SCALAR_FACTOR', 'VALUE']

    cleaned_frame = gdpdata.rename(columns={'REF_DAT': 'Date', 'GEO': 'Location', 'SCALAR_FACTOR': 'Scale', 'VALUE': 'Value'})