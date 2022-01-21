from gdphelper.gdpimporter import gdpimporter
from gdphelper.gdpcleaner import gdpcleaner
import pandas as pd


def test_integration():
    urls = pd.read_csv('docs/Data_Sources.csv')
    urls = urls["URL"]
    for url in urls:
        table, title = gdpimporter(url)
        results = gdpcleaner(table)
