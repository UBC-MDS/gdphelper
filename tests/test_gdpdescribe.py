from gdphelper.gdpdescribe import gdpdescribe
import pandas as pd
import numpy as np

def test_gdpdescribe():


    data = pd.read_csv('tests/test_13100347.csv')

    x = "VALUE"
    y = "GEO"
    stats = ["mean", "median"]

    assert isinstance(data, pd.core.frame.DataFrame), "The dataset is not a pd.DataFrame object"
    print("Passed!")

    assert all(
        x
        in ["mean", "median", "sd", "min", "max", "range_", "q75", "q25", "iqr", "nas"]
        for x in stats
    ), "Not valid descriptive function"
    print("Passed!")

    assert data[x].dtype.type == np.float64, "Not valid data type, should be numeric"
    print("Passed!")

    assert data[y].dtype.type == np.object_ , "Not valid data type, should be categorical"
    print("Passed!")

    test_df = pd.DataFrame(
        {
            "col1": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "col2": ["F", "F", "F", "F", "F", "M", "M", "M", "M", "M"],
        }
    )
    results = gdpdescribe(
        test_df, x="col1", y="col2", dec=0, stats=["min", "max", "mean"]
    )
    assert results["F"].iloc[1] == 1, "Incorrect value"
    assert results["M"].iloc[2] == 2, "Incorrect value"

    assert results['F'].iloc[2] == 1, "Incorrect value"
    assert results['M'].iloc[2] == 2, "Incorrect value"
    print("Passed!")

    assert (data[y].nunique() < data.shape[0]), 'Variable Y has unique values in every row'
    print("Passed!")

    assert (x in data.columns.tolist() and y in data.columns.tolist()), 'Variables are not in the dataset'
    print("Passed!")