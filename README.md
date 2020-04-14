# sqlalchemy-challenge

## Climate Analysis and Exploration
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
