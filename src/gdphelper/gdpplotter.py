import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def gdpplotter(data_name, aggregation):
    """Plot a line chart of periods and the selected feature.
    
    Parameters
    ----------
    data_name : string
        This is the name of the dataset that you want to draw a chart.
    aggregation : string
        There are two types of aggregation, "canada" and "province".
        The first one will give the GDP by total Canada.
        The first one will give the GDP by province.
        
    Returns
    -------
        line chart of GDP by the periods.

    Examples
    --------
    >>>
    """
    # Checking the inputs of the function: data_name
    if type(data_name) == int:
        pass
    else:
        raise ValueError("data_name should be the NUMBER of your downloaded databese")
    
    # Checking the inputs of the function: aggregation
    if aggregation in ["canada", "province"]:
        pass
    else:
        raise ValueError(
            'The aggragation should be "canada" or "province".'
        )


    #reading the database within the function
    file = f"{data_name}.csv"
    df = pd.read_csv(file)
    print("database loaded")
    
    #transforming the database to fit on matplolib's data structure.
    #grouping by region
    df_grouped_region = df.groupby(['REF_DATE','GEO']).agg(VALUE = ('VALUE', 'sum')).reset_index()
    #pivoting
    df_grouped_region_pivoted = pd.pivot_table(df_grouped_region, index=['REF_DATE'], values=['VALUE'], columns=['GEO'],
                                               fill_value=0, aggfunc=np.sum).reset_index()
    #fixing columns
    df_grouped_region_pivoted.columns = ['_'.join(col).strip() for col in df_grouped_region_pivoted.columns.values]
    print("database was transformed")
    
    #selecting the province names
    provinces = list(df_grouped_region_pivoted.columns)
    provinces.remove('REF_DATE_')
    provinces.remove('VALUE_Canada')
    provinces
    if provinces == []:
        print("WARNING: checking province names: there aren't provinces in this database")
        print("therefore, use only option 'canada' for 'aggragation'.")
    else:
        print("checking province names: we have provinces in this dataset")
    
    #drawing charst according to the selected option
    if aggregation == "province":
        #chart 01
        df_grouped_region_pivoted.plot(x='REF_DATE_', y=provinces)
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title("GDP (CAD$ millions) VS Years", loc='center')
        plt.show()

    if aggregation == "canada":
        #chart 02
        df_grouped_region_pivoted.plot(x='REF_DATE_', y='VALUE_Canada')
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.ylabel("GPD (CAD$ - millions)")
        plt.xlabel("Years")
        plt.title("GDP (CAD$ millions) VS Years", loc='center')
        plt.show()

