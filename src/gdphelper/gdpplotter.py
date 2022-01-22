import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def gdpplotter(cleaned_Dataframe):
    """
    Author: Aldo Saltao Barros
    
    Plot a line chart of periods and the selected feature.
    
    Parameters
    ----------
    cleaned_Dataframe : pandas.DataFrame
        This is the name of the dataset that you want to draw a chart. It is an output from the function gdpcleaner
    
    Returns
    -------
        chart of GDP by the Region according to the information within the DataFrame

    Examples
    >>> url = "https://www150.statcan.gc.ca/n1/tbl/csv/36100408-eng.zip"
    >>> df, x = gdpimporter(url)
    >>> cleaned_df = gdpcleaner(df)
    >>> gdpplotter(cleaned_df)
    

    """
    # check for DataFrame input argument
    if (type(cleaned_Dataframe) != pd.DataFrame):
         raise TypeError("Argument must be a specific Pandas DataFrame, use the 'gpdcleaner' to create this dataFrame")
    
    # reading the database
    df = cleaned_Dataframe

    #cheking units in Scale
    units_type = df['Scale'].unique()

    # using the same unit for the charts
    if 'millions' in units_type:
        df_filtered = df[df['Scale'] == 'millions']
    elif 'units' in units_type:
        df_filtered = df[df['Scale'] == 'units']
    elif 'units ' in units_type:
        df_filtered = df[df['Scale'] == 'units ']
    else:
        raise TypeError("This dataframe don't have the GDP's units 'millions' or 'units ' or 'units' which are allowed for this analysis. Please check your DataFrame")


    # grouping relevant information
    df_grouped_region = df_filtered.groupby(['Date','Location']).agg(
    Value = ('Value', 'sum')
    ).reset_index()

    # pivoting
    df_grouped_region_pivoted = pd.pivot_table(df_grouped_region, index=['Date'],
                                               values=['Value'], columns=['Location'],fill_value=0, aggfunc=np.sum).reset_index()
    # fixing columns
    df_grouped_region_pivoted.columns = ['_'.join(col).strip() for col in df_grouped_region_pivoted.columns.values]

    # selecting the province names
    provinces = list(df_grouped_region_pivoted.columns)
    year = df['Date'].nunique()

    if "Value_Canada" in provinces and year > 1:
        # Draw a vertical bar chart
        df_grouped_region_pivoted.plot(x='Date_', y='Value_Canada')
        # place legend in center right of plot
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title("GDP (CAD$ millions) VS Years", loc='center')
        plt.show()

    if "Value_Canada" in provinces and year == 1:
        df_grouped_region_pivoted.plot.bar(x="Date_", y="Value_Canada", rot=70)
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title(f"GDP (CAD$ millions) VS Year - {year}", loc='center')
        plt.show(block=True)

    if "Value_Canada" not in provinces and year > 1 :
        provinces.remove('Date_')
        df_grouped_region_pivoted.plot(x='Date_', y=provinces)
        #place legend in center right of plot
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title("GDP (CAD$ millions) VS Years", loc='center')
        plt.show()

    if "Value_Canada" not in provinces and year == 1 :
        provinces.remove('Date_')
        df_grouped_region_pivoted.plot.bar(x="Date_", y=provinces, rot=70)
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title(f"GDP (CAD$ millions) VS Year - {year}", loc='center')
        plt.show(block=True)
