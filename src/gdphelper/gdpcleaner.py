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
    if (isinstance(gdpdata, pd.core.frame.DataFrame)):
        pass
    else:
        raise TypeError("Argument must be a Pandas DataFrame")

    cleaned_frame = gdpdata

    #Remove spurious columns
    spurious = ['DGUID', 'UOM_ID', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 
                                          'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS', 'Value', 'Seasonal adjustment']
    for column in cleaned_frame.columns :
        if column in spurious:
            cleaned_frame = cleaned_frame.drop(columns=column)


    #Drop any rows with null value
    cleaned_frame = cleaned_frame.dropna()
    
    #Rename relevant columns
    cleaned_frame = cleaned_frame.rename(columns={'REF_DATE': 'Date', 'GEO': 'Location', 
                                            'SCALAR_FACTOR': 'Scale', 'VALUE': 'Value', 'UOM': 'Unit'})

    for column in cleaned_frame.columns:
        if 'NAICS' in column:

            cleaned_frame = cleaned_frame.rename(columns={column: 'NAICS_Class'})
        if 'aggregat' in column: #Not a spelling mistake, there are multiple similar column headers in different datasets
            cleaned_frame = cleaned_frame.rename(columns={column: 'Special_Industry'})

    return cleaned_frame        

