from gdphelper.gdpplotter import gdpplotter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def test_gdpplotter():
    
    # importing toydata from test/
    data = pd.read_csv('tests/test_13100347.csv')
    #data = pd.read_csv('36100408.csv')
    # changing column names manually (simulating outputs from gdpcleaner)
    renamed_data = data.rename(columns={'REF_DATE': 'Date', 'GEO': 'Location',
                                        'VALUE': 'Value', 'SCALAR_FACTOR': 'Scale'})
    # defining columns to check
    x = "Location"
    y = "Scale"
    z = "Value"

    # starting the function gpdplotter
    gdpplotter(renamed_data)

    # checking if a plot was drawn by the function
    num_figures = plt.gcf().number
    assert num_figures > 0, "None chart was created"
    print("Passed!")

    # checking the column types x
    assert renamed_data[x].dtype.type == np.object_ , "Not valid data type, should be categorical"
    print("Passed!")
    
    # checking the column types y
    assert renamed_data[y].dtype.type == np.object_ , "Not valid data type, should be categorical"
    print("Passed!")
    
    # checking the column types z
    assert renamed_data[z].dtype.type == np.float64, "Not valid data type, should be numeric"
    print("Passed!")
    
    #cheecking the DataFrame structure
    assert isinstance(renamed_data, pd.core.frame.DataFrame), "The dataset is not a pd.DataFrame object, please use gpdcleaner to get the right DataFrame"
    print("Passed!")
