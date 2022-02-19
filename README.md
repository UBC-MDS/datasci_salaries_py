# Data Science Salaries Dashboard
## About

This project aims to build a dashboard to visualize data science salaries across the world. Further details can be found in our proposal [here](https://github.com/UBC-MDS/datasci_salaries_py/blob/main/proposal.md).

## Description and sketch

The dashboard shows a world map with the median data science salary of a country encoded in the colour channel. By selecting a country to focus on, a histogram showing the distribution of salaries, a boxplot showing the distribution of salaries per gender, and a 2D-histogram showing the distribution of salaries by age are updated for the specified country. For both the histogram and 2D-histogram plots, x-axis sliders are provided so that users can zoom in on regions of the x-axes that they are interested in. Furthermore, a scatter plot of the salaries for each country is shown on the right.

![app-sketch](https://github.com/UBC-MDS/datasci_salaries_py/blob/main/media/app-sketch.png)

## Data

To populate our dashboard, the [Kaggle Data Scientists Salaries Around the World](https://www.kaggle.com/ikleiman/data-scientists-salaries-around-the-world) dataset by [Iair Kleiman](https://www.kaggle.com/ikleiman). Specifically, the files `conversionRates.csv` and `multipleChoiceResponses.csv` are used in this project. The data is processed using `scripts/data_cleaning.R` to mainly remove rows that do not have salary data, and to convert all salaries to USD from the respective countries' currencies.
## Contributing

Contributors: Artan Zandian, Joshua Sia, Siqi Tao, Wenjia Zhu (DSCI_532_GROUP19).

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/datasci_salaries_py/blob/main/CONTRIBUTING.md). 

Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

This dashboard was created by Artan Zandian, Joshua Sia, Siqi Tao, Wenjia Zhu (DSCI_532_GROUP19). It is licensed under the terms of the MIT license.