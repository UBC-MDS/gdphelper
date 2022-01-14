import pandas as pd
import numpy as np

def descriptive_summary(x="GDP", y="year"):
    """
    calculates summary statistics for numeric variable x by categorical variable y

    Parameters
    ----------
    x : str
        name of a pd.series of type float used to calculate mean, standard deviation,
        min, max values

    y: str
       name of pd.series categorical grouping variable 

    Returns
    -------
    pd.Dataframe
        Table with the summary statistics.

    Examples
    --------
    >>>descriptive_summary(GDP, "year")
    """