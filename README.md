# Hawaii Vacation

## Background
I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning, I need to do some climate analysis on the area. The following outlines is what I did.

## Climate Analysis and Exploration
Used Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. I used the provided starter notebook and hawaii.sqlite files to complete my climate analysis and data exploration.

- Used SQLAlchemy create_engine to connect to my sqlite database.
- Used SQLAlchemy automap_base() to reflect my tables into classes and save a reference to those classes called Station and Measurement.
- Designed a query to retrieve the last 12 months of precipitation data.
- Loaded the query results into a Pandas DataFrame and set the index to the date column while sorting the DataFrame values by date.
- Used Pandas to print the summary statistics for the precipitation data.

Plot of Hawaii precipitation data for the last year of the data set.

![](/Output/Hawaii_Precipitation.png)

Summary statistics table for the precipitation data.

![](/Output/Summary_Statistics_Table.png)

## Station Analysis
- Designed a query to calculate the total number of stations.
- Design a query to find the most active stations.
- Listed the stations and observation counts in descending order.
- Design a query to retrieve the last 12 months of temperature observation data (TOBS).
- Filter by the station with the highest number of observations.

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

### Routes
 `/`
- Home page.
- List all routes that are available.

`/api/v1.0/precipitation`
- Converts the query results to a dictionary using `date` as the key and `prcp` as the value.
- Returns the JSON representation of my dictionary.

`/api/v1.0/stations`
- Returns a JSON list of stations from the dataset.

`/api/v1.0/tobs`
- Queries the dates and temperature observations of the most active station for the last year of data.
- Returns a JSON list of temperature observations (TOBS) for the previous year.

`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
- Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
- When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
- When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

All code and outputs can be viewed using app.py.


## Bonus
## Temperature Analysis I

Null hypothesis: There is very little to no statistical difference of the average temperaures of June and Decemeber. 

A unpaired t-test must be performed due to the two sets of data having no relationship. The t-test reulsted in  a p value = 6.62 e-178 which is < 0.05 so we can reject the null hypothesis and conclude that there is a statistical difference between the mean temperatures of the months June and December.
