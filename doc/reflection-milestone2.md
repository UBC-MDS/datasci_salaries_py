# Reflection

## What has been implemented

The dashboard features 7 plots which describe the distribution of data science salaries for the features country, gender, education level, age, tenure, and a scatter plot of all the data science salaries. The dashboard is split into two parts: the left side shows country-specific salary distributions while the right side (marked by a darker background) shows the global salary trends. The global salary trends are colored based on the data scientist's tenure, and interactivity is provided to filter based on tenure.

The user is able to select a specific country by using a dropdown menu (top left) and country-specific plots will be updated to reflect salaries corresponding to the chosen country. A slider is also provided to shift the focus of the country-specific plots depending on what salary range the user is interested in exploring. For instance, the user may be very new to data science, and wants to visualize the lower end of the salary distribution to see what proportion of data scientist's have a bachelor's degree.

## What has not been implemented

To visualize country-specific trends, a dropdown menu is used. However, we believe that the dashboard will be more engaging if the user is able to click on a country on the world map to update the country-specific plots. This will also allow the dashboard to appear more seamless and well-connected.

Furthermore, the stacked histogram is currently stacked based on the formal education level. To answer our research question in the proposal, a dropdown menu containing other categorical features such as how often the data scientist works remotely can be included so that the user is able to explore more of the data set.

## Effective components of current dashboard

The world map is effective in giving a high level overview of how data science salaries are distributed across the world. In addition, the country-specific plots describe the salary distributions clearly for many different features. The global trends are always shown on the right side of the dashboard to provide a comparison of country-specific trends to the broader context.

The dropdown menu allows users to explore country-specific trends, and the slider also provides users with more flexibility in exploring the data set.

## Limitations of current dashboard

One limitation with the current dashboard is that not enough feedback has been gathered about its effectiveness and ease of use. For instance, some users may feel like there are too many plots shown in the dashboard which can be overwhelming at first glance. Another limitation is that the dashboard's layout is not consistent for different screen sizes which could cause the dashboard to appear very messy.

## Future improvements

To summarize, improvements that can be made to the dashboard are: (1) Click on world map to select country, (2) Dropdown menu to change what the histograms stacking encodes, (3) Gather feedback about UI/UX, (4) Improve dashboard layout to be consistent across multiple devices.