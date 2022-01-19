from gdphelper.gdpplotter import gdpplotter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def test_gdpplotter():

    data = pd.read_csv("36100408.csv")
    x = "VALUE"
    y = "GEO"
    data_name=36100408
    aggregation = "canada"
    gdpplotter(data_name, aggregation)

    #checking if a plot was drawn
    num_figures = plt.gcf().number
    assert num_figures > 0, "None chart was created"
    print("Passed!")

    #checking the column types
    assert data[x].dtype.type == np.float64, "Not valid data type, should be numeric"
    print("Passed!")
    
    #checking the column types
    assert data[y].dtype.type == np.object_ , "Not valid data type, should be categorical"
    print("Passed!")