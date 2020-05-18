# Hawaii Climate Analysis and Exploration

## Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## Climate Analysis and Exploration
Used Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. I used the provided starter notebook and hawaii.sqlite files to complete my climate analysis and data exploration.

- Used SQLAlchemy create_engine to connect to your sqlite database.
- Used SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
- Designed a query to retrieve the last 12 months of precipitation data.
- Loaded the query results into a Pandas DataFrame and set the index to the date column while sorting the DataFrame values by date.
- Used Pandas to print the summary statistics for the precipitation data.

Plot of Hawaii precipitation data for the last year of the data set.

![](/Output/Hawaii_Precipitation.png)

Summary statistics table for the precipitation data.

![](/Output/Summary_Statistics_Table.png)

## Station Analysis
There are a total of 9 stations.

USC00519281 is the most active station with 2772 records.
USC00519397 has 2724 records.
USC00513117 has 2709 records.
USC00519523 has 2669 records.
USC00516128 has 2612 records.
USC00514830 has 2202 records.
USC00511918 has 1979 records.
USC00517948 has 1372 records.
USC00518838 has 511 records.

Histogram plot of the last 12 months of temperature observation data (TOBS) from station USC00519281.
![](/Output/Temperature_Histogram.png)

## Climate App
All code and outputs can be viewed using app.py.


## Bonus
## Temperature Analysis I

Null hypothesis: There is very little to no statistical difference of the average temperaures of June and Decemeber. 

A unpaired t-test must be performed due to the two sets of data having no relationship. The t-test reulsted in  a p value = 6.62 e-178 which is < 0.05 so we can reject the null hypothesis and conclude that there is a statistical difference between the mean temperatures of the months June and December.
