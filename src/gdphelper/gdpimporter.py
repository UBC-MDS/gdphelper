import requests, zipfile
import os
import pandas as pd

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
    filename : str
        the filename that the unzipped csv data (not the MetaData) has. 
        If None, 'open_canada_data.csv' will be the filename. 
        This argument is not useful when filetype is set to 'all'
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
    >>> gdpimporter("https://www150.statcan.gc.ca/n1/tbl/csv/36100400-eng.zip")
    """
    # Exception handling: check if the arguments are feasible
    if (filename != None) and (not isinstance(filename, str)):
        raise TypeError("'filename' should be either None (default) or a string.")
    if filetype not in ['csv', 'all']:
        raise ValueError("'filetype' should either be 'csv' (by default) or 'all'.")
    if (not isinstance(url, str)) or (not url.endswith('.zip')):
        raise ValueError("'url' should be a valid url of a zipfile that ends with '.zip'.")

    zipname = url.split("/")[-1]  ## get the name of original zipfile
    req = requests.get(url)

    with open(zipname, "wb") as code:
        code.write(req.content)
    zipdata = zipfile.ZipFile(zipname)
    zipinfos = zipdata.infolist()
    
    if filetype == "csv":
        # iterate through each file
        for zipinfo in zipinfos:
            # This will do the renaming
            if zipinfo.filename.endswith(".csv") and not zipinfo.filename.endswith("MetaData.csv"):
                if filename == None: 
                    zipinfo.filename = f"open_canada_data.csv"
                else:  ## must be a str
                    zipinfo.filename = f"{filename}.csv"
            zipdata.extract(zipinfo)
    else:
        for zipinfo in zipinfos:
            zipdata.extract(zipinfo)        
    zipdata.close()
    
    for filepath in os.listdir(): 
        if filepath == f"{zipname[:-8]}_MetaData.csv":
            metadata = pd.read_csv(filepath)
            os.remove(filepath) # Clean up the metadata
            continue
        elif filepath.endswith('.zip'):
            os.remove(filepath) # Clean up zip
            continue
        if filename == None:
            if filepath == "open_canada_data.csv":
                data = pd.read_csv(filepath)
        else:
            if filepath == f"{filename}.csv":
                data = pd.read_csv(filepath)
    return data, metadata.index[0]