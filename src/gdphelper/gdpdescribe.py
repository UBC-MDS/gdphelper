import pandas as pd
import numpy as np

def gdpdescribe(x="GDP", y="year"):
    """
    calculates summary statistics for numeric variable x by categorical variable y

    Parameters
    ----------
    x : str
        column name of a pandas dataframe used to calculate mean, standard deviation,
        min, max values

    y: str
      column name of a grouping variable  categorical from pandas dataframe 
    
    Returns
    -------
    pd.Dataframe
        Table with the summary statistics.

    Examples
    --------
    >>>gdpdescribe(GDP, "year")
    """