# Proposal

### Motivation and Purpose

### Description of the Data

To populate our dashboard, we will be using the [Kaggle Data Scientists Salaries Around the World](https://www.kaggle.com/ikleiman/data-scientists-salaries-around-the-world) by [Iair Kleiman](https://www.kaggle.com/ikleiman). Specifically, the files `conversionRates.csv` and `multipleChoiceResponses.csv` are used in this project. The data is processed using `scripts/data_cleaning.R` to mainly remove rows that do not have salary data, and to convert all salaries to USD from the respective countries' currencies. After data wrangling, the tidy dataset contains information about data scientist salaries in USD in 2018 for 43 different countries with the following features of interest:

- **Age** - The age of data scientist (numerical).

- **Country** - The country where the data scientist works (categorical with 43 levels).

- **Gender** - The gender of the data scientists (categorical with 4 levels: (1) Male, (2) Female, (3) Non-binary, genderqueer, or gender non-conforming, and (4) A different identity).

- **FormalEducation** - The level of formal education attained (ordinal with 7 levels: (1) Doctoral degree, (2) Master's degree, (3) Bachelor's degree, (4) Professional degree, (5) Some college/university study without earning a bachelor's degree, (6) I did not complete any formal education past high school, and (7) I prefer not to answer).

- **RemoteWork** - How often the data scientist works remotely (ordinal with 6 levels: (1) Always, (2) Most of the time, (3) Sometimes, (4) Rarely, (5) Never, (6) Don't know)

To see the other features in the dataset, please see `data/schema.csv`.
### Research Questions and Usage Scenarios

#### Usage Scenario: 