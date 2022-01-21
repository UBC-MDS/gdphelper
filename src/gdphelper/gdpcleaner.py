import pandas as pd
def gdpcleaner(gdpdata: pd.DataFrame):
    """
    Author: Gabe Fairbrother
    Remove spurious columns, Rename relevant columns, Scrub any string artifacts (eg [T008])


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
    #Check for DataFrame input argument
    if (type(gdpdata == None)):
        raise ValueError("Must specify a Pandas DataFrame")

    if (type(gdpdata) != pd.DataFrame):
        raise TypeError("Argument must be a Pandas DataFrame")

    #Remove spurious columns
    cleaned_frame = gdpdata.drop(columns=['DGUID', 'UOM', 'UOM_ID', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'])
 
    #Drop any rows with null value
    cleaned_frame = cleaned_frame.dropna()
    
    cleaned_frame = gdpdata.rename(columns={'REF_DAT': 'Date', 'GEO': 'Location', 'SCALAR_FACTOR': 'Scale', 'VALUE': 'Value', 'UOM': 'Unit'})
