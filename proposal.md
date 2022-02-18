# Proposal

### Motivation and Purpose

### Description of the Data

To populate our dashboard, we will be using the [Kaggle Data Scientists Salaries Around the World](https://www.kaggle.com/ikleiman/data-scientists-salaries-around-the-world) by [Iair Kleiman](https://www.kaggle.com/ikleiman). Specifically, the files `conversionRates.csv` and `multipleChoiceResponses.csv` are used in this project. The data is processed using `scripts/data_cleaning.R` to mainly remove rows that do not have salary data, and to convert all salaries to USD from the respective countries' currencies. After data wrangling, the tidy dataset contains information about data scientist salaries in USD in 2018 for 43 different countries with the following features of interest:

- **Age** - The age of data scientist (numerical).

- **Country** - The country where the data scientist works (categorical with 43 levels).

- **Gender** - The gender of the data scientists (categorical with 4 levels: (1) Male, (2) Female, (3) Non-binary, genderqueer, or gender non-conforming, and (4) A different identity).

- **FormalEducation** - The level of formal education attained (ordinal with 7 levels: (1) Doctoral degree, (2) Master's degree, (3) Bachelor's degree, (4) Professional degree, (5) Some college/university study without earning a bachelor's degree, (6) I did not complete any formal education past high school, and (7) I prefer not to answer).

To see the other features in the dataset, please see.
### Research Questions and Usage Scenarios

Our app will provide answers to two research questions:

- How are Data Science jobs distributed around the world in the past year?
- What Data Science related job titles are more popular in each country and how much they pay on average?
- Data Science professionals in which countries are paid the highest?
- What is the age and gender distribution of Data Science related jobs in each country and around the world?

#### Usage Scenario

Heroku is a UBC Master of Data Science student who will be graduating in July and will be starting his job hunt next month. He is overwhelmed by the options that he has in front of him and wants to [compare] salaries in his home country to Canada to decide whether he should rather be focusing his energy on finding job in Canada or The States. He is mostly concerned with the range of salary that he should be expecting in a certain country and wants to [explore] salary expectations for new graduates. His priority is to work remotely, but he is afraid he might need to be asking for less salary if he is working remotely. He needs to know how remote Data Science jobs [compare] to in-person jobs. Using the Data Science Salaries dashboard, he will be able to filter in specific countries to [identify] the ratio of different data science job titles globally and within each country. He would also be able to [explore] salary ranges per age and gender. If not happy with the salary ranges, he has the option [explore] if doing a PHD will increase his salary and [compare] job opportunities for a Master's degree versus a PHD.
