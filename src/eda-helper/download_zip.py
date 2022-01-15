def download_zip(url, filename=None, filetype='csv', exclude_meta=True):
    """Download the zipped file, unzip and rename the unzipped files.

    This function downloads the zipped data from URL to the local path,
    unzips and renames the files as desired.

    Parameters
    ----------
    url : str
        URL to the zip file (ends with .zip)
    filename : str or list of str, default None
        the filename or list of filenames that the unzipped file(s) have.
        If None, 'open_canada_data1.csv', 'open_canada_data2.csv' ...  
        will be the filenames
    filetype : {'csv', 'all'}, default 'csv'
        the types of files that will be extracted. If 'csv', only csv
        files are extracted'. If 'all', files of all types are extracted
    exclude_meta : bool, default True
        If True, metadata (specific to Open Canada data) is not extracted
        and saved. Otherwise, include metadata.

    Returns
    -------
    None

    Examples
    --------
    >>> download_zip("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip")
    """