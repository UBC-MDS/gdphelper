import matplotlib.pyplot as plt


def line_plot(type_chart, type_feature):
    """Plot a line chart of periods and the selected feature.
    
    Parameters
    ----------
    type_chart : string
        There are two types of chart, "all_together" or "split_charts".
        The first type will bring up all sub-features in the same plot
        The second type will bring up all one chart for each sub-feature.
    type_feature : string
        There are two types of features, "region" and "industry".
        The first one will break down the GDP by each reageion.
        The second one will break down the GDP by each industry.

    Returns
    -------
        line chart of GDP by the periods within the dataset.

    Examples
    --------
    >>> xxxxx

    """