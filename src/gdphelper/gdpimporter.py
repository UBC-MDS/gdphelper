def gdpimporter(url, filename=None, filetype='csv'):
    """Download the zipped file, unzip, rename the unzipped files, and
    outputs a dataframe along with the title from meta data.

    This function downloads the zipped data from URL to the local path,
    unzips and renames the files as desired. It then returns the data
    frame along with the title as a tuple.

    Parameters
    ----------
    url : str
        URL to the zip file (ends with .zip)
    filename : str or list of str, default None
        The filename or list of filenames that the unzipped file(s) have.
        If None, 'open_canada_data1.csv', 'open_canada_data2.csv' ...  
        will be the filenames
    filetype : {'csv', 'all'}, default 'csv'
        the types of files that will be extracted. If 'csv', only csv
        files are extracted'. If 'all', files of all types are extracted

    Returns
    -------
    (DataFrame, str) : 
        A tuple containing the dataframe and the title of the data extracted
        from the meta data.


    Examples
    --------
    >>> download_zip("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip")
    """
