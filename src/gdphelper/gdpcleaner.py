import pandas as pd
def gdpcleaner(gdpdata: pd.DataFrame):
    """
    Author: Gabe Fairbrother
    Remove spurious columns, Rename relevant columns, Remove NaNs


    Parameters
    ----------
    gdpdata: DataFrame 
    a loaded dataframe based on a downloaded Open Government GDP at basic prices dataset (https://open.canada.ca/en/open-data)


    Returns
    -------
    DataFrame:  A cleaned and simplified DataFrame of the relevant columns for summary and visualization. 
    Possible columns (dataset dependent) include:
        Date: Date of data
        Location: Province or Jurisdiction
        Scale: Scale of the Value column (Percent, Millions, etc)
        Unit: Unit of Measure
        Value: Portion of the GDP for the Location and Date
        NAICS_Class: North American Industry Classification System ID 
        Industry: Industry of Record
        Sub-sector: Non-profit sub-sector
        Special_Industry: Special Industry Aggregate

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
    cleaned_frame = gdpdata.drop(columns=['DGUID', 'UOM_ID', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 
                                          'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS', 'Value', 'Seasonal adjustment'])
 
    #Drop any rows with null value
    cleaned_frame = cleaned_frame.dropna()
    
    #Rename relevant columns
    cleaned_frame = gdpdata.rename(columns={'REF_DAT': 'Date', 'GEO': 'Location', 
                                            'SCALAR_FACTOR': 'Scale', 'VALUE': 'Value', 'UOM': 'Unit'})

    for column in gdpdata.columns():
        if 'NAICS' in column:
            gdpdata.rename({column: 'NAICS_Class'})
        if 'aggregat' in column: #Not a spelling mistake, there are two similar column headers in different datasets
            gdpdata.rename({column: 'Special_Industry'})
        