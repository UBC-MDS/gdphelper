import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def gdpplotter(cleaned_Dataframe, aggregation):
    """
    Author: Aldo Saltao Barros
    
    Plot a line chart of periods and the selected feature.
    
    Parameters
    ----------
    cleaned_Dataframe : pandas.DataFrame
        This is the name of the dataset that you want to draw a chart. It is an output from the function gdpcleaner
    aggregation : string
        There are two types of aggregation, "canada" and "province".
        The first one will give the GDP by total Canada.
        The first one will give the GDP by province.
        
    Returns
    -------
        line chart of GDP by the Region VS periods.

    Examples
    
    >>>df = pd.read_csv("36100408.csv")
    >>>aggregation = "canada"
    >>>cleaned_df = gdpcleaner(df)
    >>>gdpplotter(cleaned_df, aggregation)

    """
    # check for DataFrame input argument
    if (type(cleaned_frame) != pd.DataFrame):
         raise TypeError("Argument must be a specific Pandas DataFrame, use the 'gpdcleaner' to create this dataFrame")
    
    # checking the inputs of the function: aggregation
    if aggregation in ["canada", "province"]:
        pass
    else:
        raise ValueError(
            'The aggragation should be "canada" or "province".'
        )

    # reading the database
    df = cleaned_Dataframe
    
    # transforming the database to fit on matplolib's data structure.
    
    # using the same unit for the charts: millions
    unit= ['millions']
    df_filtered = df[df['Scale'].isin(unit)]
    
    # grouping relevant information
    df_grouped_region = df_filtered.groupby(['Date','Location']).agg(
    Value = ('Value', 'sum')
    ).reset_index()

    # pivoting
    df_grouped_region_pivoted = pd.pivot_table(df_grouped_region, index=['Date'],
                                               values=['Value'], columns=['Location'],fill_value=0, aggfunc=np.sum).reset_index()
    # fixing columns
    df_grouped_region_pivoted.columns = ['_'.join(col).strip() for col in df_grouped_region_pivoted.columns.values]
    print("database was transformed")

    # selecting the province names
    provinces = list(df_grouped_region_pivoted.columns)
    provinces.remove('Date_')
    provinces.remove('Value_Canada')
    provinces
    # checking the provinces whitin the dataFrame
    if provinces == []:
        print("WARNING: checking province names: there aren't provinces in this database")
        print("therefore, use only option 'canada' for 'aggragation'.")
    else:
        print("checking province names: we have all provinces in this dataset")

    # drawing charts according to the selected option
    if aggregation == "province":
        #chart 01
        df_grouped_region_pivoted.plot(x='Date_', y=provinces)
        #place legend in center right of plot
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title("GDP (CAD$ millions) VS Years", loc='center')
        plt.show()

    if aggregation == "canada":
        # chart 02
        df_grouped_region_pivoted.plot(x='Date_', y='Value_Canada')
        # place legend in center right of plot
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title("GDP (CAD$ millions) VS Years", loc='center')
        plt.show()

