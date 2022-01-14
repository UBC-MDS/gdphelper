def gdpcleaner(gdpdata: DataFrame):
     """Load downloaded data, Remove spurious columns, Rename relevant columns, 
        Scrub any string artifacts (eg [T008]), Identify category 


    Parameters
    ----------
    gdpdata: DataFrame 
        a loaded dataframe based on a downloaded Open Government GDP at basic prices dataset (https://open.canada.ca/en/open-data)


    Returns
    -------
    (DataFrame, string):  A cleaned and simplified DataFrame of the relevant columns for summary and visualization, a string indicating category (such as percentage, industry, NAICS)


    Examples
    --------
    >>> gdpcleaner(example_data)
    """