import pandas as pd
import numpy as np


def gdpdescribe(df, x, y, stats=["mean", "sd", "median"], dec=2):
    """
    Calculates summary statistics for the Numeric Variable x grouping by categorical variable y.

    The function is able to calculate the following descriptive statistics:

      Mean
      Median
      Standard Deviation
      Minimum Value
      Maximum Value
      Range
      Value of 75th percentile
      Value of 25th percentile
      Interquartile range
      Number of Missing values

    Parameters
    ----------
    df: pd.Dataframe
        pandas dataframe with the variables to analyze

    x : str
        column name of a pandas dataframe used to calculate the descriptive statistics

    y: str
      column name of a grouping variable

    dec: int
       number of decimal places to return in the table

    stats: list, default ["mean", "sd", "median"]
         Descriptive statistics to calculate

    Returns
    -------
    pd.Dataframe
        Table with the summary statistics specified as arguments of the function

    Examples
    --------
    >>>gdpdescribe(df, "Value", "Location", stats=["mean", "median", "sd", "min", "max", "range_", "q75", "q25", "iqr", "nas"], dec=3)
    """
    # Avoid scientific notation in the display, use decimal points
    pd.set_option("display.float_format", "{:." f"{dec}" "f}".format)

    # validate inputs arguments of the function

    if isinstance(df, pd.core.frame.DataFrame):
        pass
    else:
        raise ValueError("df should be a pd.DataFrame")

    if x in df.columns.tolist() and y in df.columns.tolist():
        pass
    else:
        raise ValueError("Incorrect Variable names")

    if df[y].nunique() < df.shape[0]:
        pass
    else:
        raise ValueError("Variable Y has unique values in every row, cannot group")

    if df[x].dtype.type == np.float64 or df[x].dtype.type == np.int64:
        pass
    else:
        raise ValueError("Variable X is not numeric")

    if df[y].dtype.type == np.object_:
        pass
    else:
        raise ValueError("Variable Y is not categorical")

    if all(
        x
        in ["mean", "median", "sd", "min", "max", "range_", "q75", "q25", "iqr", "nas"]
        for x in stats
    ):
        pass
    else:
        raise ValueError(
            "The statistic to calculate is not correct! Please enter a valid one"
        )

    # initialize and calculate the stats

    mean = None
    mean = df[[x, y]].groupby([y], dropna=True).mean()
    mean.rename(columns={x: f"mean {x}"}, inplace=True)

    median = None
    median = df[[x, y]].groupby([y], dropna=True).median()
    median.rename(columns={x: f"Median {x}"}, inplace=True)

    sd = None
    sd = df[[x, y]].groupby([y], dropna=True).std()
    sd.rename(columns={x: f"Standard devitation {x}"}, inplace=True)

    min = None
    min = df[[x, y]].groupby([y], dropna=True).min()
    min.rename(columns={x: f"Min {x}"}, inplace=True)

    max = None
    max = df[[x, y]].groupby([y], dropna=True).max()
    max.rename(columns={x: f"Max {x}"}, inplace=True)

    range_ = None
    range_ = df[[x, y]].groupby([y], dropna=True).apply(lambda z: z.max() - z.min())
    range_.rename(columns={x: f"Range {x}"}, inplace=True)

    q75 = None
    q75 = df[[x, y]].groupby([y], dropna=True).quantile(q=0.75)
    q75.rename(columns={x: f"Quartile 75th  {x}"}, inplace=True)

    q25 = None
    q25 = df[[x, y]].groupby([y], dropna=True).quantile(q=0.25)
    q25.rename(columns={x: f"Quartile 25th  {x}"}, inplace=True)

    iqr = (
        df[[x, y]]
        .groupby([y], dropna=True)
        .apply(lambda x: x.quantile(q=0.75) - x.quantile(q=0.25))
    )
    iqr.rename(columns={x: f"IQR  {x}"}, inplace=True)

    nas = None
    nas = df[[x, y]].groupby([y], dropna=True).agg(lambda x: x.isnull().sum())
    nas.rename(columns={x: f"NAs  {x}"}, inplace=True)

    # validate stats to calculate
    out = []

    for i in stats:
        i_1 = eval(i)
        out.append(i_1)

    results = pd.concat(out, axis=1).T
    return results