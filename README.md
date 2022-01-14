# gdphelper

This package is designed to take the url of any of the several dozen GDP-related csv datasets from the [Canadian Government Open Data Portal](https://open.canada.ca/en/open-data) and download, clean load, summarize and visualize the data contained within.  

It contains 4 functions:
(TODO proper names)

- `download_zip`: Downloads the zipped data, extracts and renames the appropriate csv.  
- Function #2: Loads the data, removes spurious columns, renames used columns, scrubs and data issues. Returns a basic data frame and some category flags.
- Function #3: Evaluates the data category and generates summary statistics by year, region, industry, etc.  
- Function #4: Generates a set of visualizations of the data set.

This package is built upon a bunch of popular packages in Python ecosystem, including
`zipfile`, ... What makes this package unique is that it incorporates the common functionalities and streamlines the workflow from downloading the data to performing simple EDA, specifically for the GDP-related data from the Canadian Government Open Data Portal.

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
