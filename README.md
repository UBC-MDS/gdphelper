# gdphelper

This package is designed to take the url of any of the several dozen GDP-related csv datasets from the [Canadian Government Open Data Portal](https://open.canada.ca/en/open-data) and download, clean load, summarize and visualize the data contained within.  

It contains 4 functions:
(TODO proper names)


gdpimporter: Downloads the zipped data, extracts, renames the appropriate csv, and returns a dataframe along with the title from the meta data.    
gdpcleaner: Loads the data, removes spurious columns, renames used columns, scrubs and data issues. Returns a basic data frame and some category flags.   
Function #3: Evaluates the data category and generates summary statistics by year, region, industry, etc.  
line_plot: Generates a set of visualizations of the data set according to the user's choices.

## Installation

```bash
$ pip install gdphelper
```

## Usage

- TODO

## Contributors

- Aldo Barros          aldosaltao@gmail.com
- Gabe Fairbrother     gfairbrother@gmail.com
- Wanying Ye           wanying.ye2020@gmail.com
- Ramiro Mejia         ramiromejiap@gmail.com

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/Group_03_GOV_CA_GDP_HELPER/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/Group_03_GOV_CA_GDP_HELPER/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`gdphelper` was created by Aldo Barros, Gabriel Fairbrother, Ramiro Mejia, Wanying Ye. It is licensed under the terms of the MIT license.

## Credits

`gdphelper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
