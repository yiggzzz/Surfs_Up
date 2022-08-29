# Surfs Up with Advanced Data Storage and Retrieval

### Description
Using new tools such as SQLite, SQLAlchemy, and Flask to build on our knowledge of SQL database structures and querying methods.
In addition, writing and executing Python code in a Jupyter lab while creating graphs using matplotlib.

### Challenge Overview
Run analytics on a weather data set of locations to present to potential investors in a "Surf n Shake" shop.
Use Jupyter Notebook for our precipitation and station analysis and use VS Code in this module to create our Flask application.

### Approach
Determine key statistical data about the month of June and the month of December. Compare your findings between the month of June and December and then make 2 or 3 recommendations for further analysis.

### Results
* Compare your findings between the month of June and December for all locations for all years.                                         

|June Precipitation  |           | tobs   |
| ------------- |:-------------:| -----:|
|count   |	1574.000000	     |1700.000000  |
  | mean	 |  0.136360	       | 74.944118   |
  | std    | 	0.335731	       | 3.257417    |
  | min	   |  0.000000	       | 64.000000   |
  | 25%	   |  0.000000	       | 73.000000   |
  | 50%	   |  0.020000	       | 75.000000   |
  | 75%    |  0.120000    	   | 77.000000   |
  | max	   |  4.430000         | 85.000000   |




|December Precipitation   |           | tobs   |
| ------------- |:-------------:| -----:|
|count   |	 1405.000000	     | 1517.000000  |
  | mean	 |   0.216819	  	       |  71.041529  |
  | std    |  0.541399	       |  3.745920  |
  | min	   |  0.000000	       |  56.000000  |
  | 25%	   |  0.000000	       |  69.000000  |
  | 50%	   |  0.030000		       |  71.000000  |
  | 75%    |  0.150000  	   | 74.000000  |
  | max	   |  6.420000	        |  83.000000  |



* June statistics for all stations, for all years had more precipitation amount than its equivalent in December.
But the mean, std, and max values were lower in June for all stations, for all years than in December's eqivalent in spite of the precipitation count for June.

* For all the percentiles, but for the 25% values  which is zero for both months for all stations for all years, the 50% and
75% percentiles however were high for Dec than in June.
Both months had no min values.

* When it comes to the temperature observations (tobs) count, min, 25%, 50%,75% and max data, June saw the highest values than in Dec.
It is only in the std statistic data that we see Dec values greater than that of June's.

### Summary 
Based on the results we can see a 30 degree range from the weather between June and Dec. This would allow for the weather temperature to not get in the way of the ice cream and surf business. It would be helpful to run a query on weather trends for rain storms and percipitation.

### Things Learned
* The structures, interactions, and types of data of a provided dataset.
* Differentiating between SQLite and PostgreSQL databases.
* Using SQLAlchemy to connect to and query a SQLite database.
* Using statistics like minimum, maximum, and average to analyze data.
* Designing a Flask application using data.

### Recommendations for further analysis
1) Calculate daily normals, ie. the average daily maximum (tmax) and minimum (tmin) temperatures for specific month & day.
2) Calculate rainfall per weather station for specific dates using the previous year's matching dates.
   And list the station, name, latitude, longitude, and elevation; sort desc order by precipitation amount. 
3) Do a temperature analysis by creating a function that will accept a start and end dates in the 
   format %Y-%m-%d and return the minimum, average, and maximum temperatures for that range of dates.
 
### SOFTWARE/TOOLS/LIBRARIES
SQLite, Flask, Python, Jupyter lab, SQLAlchemy, NumPy, Pandas, Matplotlib, Datetime
