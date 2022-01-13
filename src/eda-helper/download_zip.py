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
        If None, 'data1.csv', 'data2.csv' ...  will be the filenames
    filetype : str, default 'csv'
        the types of files that will be extracted. If 'csv', only csv
        files are extracted'. If 'all', files of all types are extracted
    exclude_meta : bool, default True
        If True, metadata (specific to Open Canada data) is not extracted
        and saved. Otherwise, include metadata.

    Returns
    -------
    collections.Counter
        dict-like object where keys are words and values are counts.

    Examples
    --------
    >>> count_words("text.txt")
    """
