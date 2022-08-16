# Set Up the Flask Weather App

#################
#  Import Python Dependencies
#################
import datetime as dt
import numpy as np
import pandas as pd

################
# Dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database.
################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

################
# Add the code to import the dependencies that we need for Flask
################
from flask import Flask, jsonify

#################
# Set Up the Database engine for the Flask application
#################
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes.
Base = automap_base()

# Use Base.prepare() function to reflect the tables into SQLAlchemy.
Base.prepare(engine, reflect=True)

# Save references to each table
# Create a variable for each of the classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

################
# Set Up Flask.
################
# Define our app for our Flask application.
# This will create a Flask application called “app.”
app = Flask(__name__)

#################
# Flask Routes
#################
# Define the welcome route using the code below:
@app.route("/")

# Create a function welcome() with a return statement. Our return statement will have f-strings as a reference to all of the other routes.
#  Add the routing information for each of the other routes
def welcome():
	return(
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
	)
                                                ## Precipitation Route ##
# Create a GET route for the Precipitation for the last year
@app.route("/api/v1.0/precipitation")

# First, create the precipitation() function.
def precipitation():
        # Secondly, calculates the date one year ago from the most recent date in the database. Add code to function
        prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        # Thirdly, write a query to get the date and precipitation for the previous year
        precipitation = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >= prev_year).all()
        # Finally, create a dictionary with the date as the key and the precipitation as the value
        # Use Jsonify() function to convert the dictionary to a JSON file.
        precip = {date: prcp for date, prcp in precipitation}
        return jsonify(precip)


                                               ## Stations Route ##
# Create the Stations Route. Define the route and route name.
@app.route("/api/v1.0/stations")

# First, create the stations() function.
def stations():
        # Create a query that will allow us to get all of the stations in our database.
        results = session.query(Station.station).all()
        # Unravel results into a one-dimensional array. Use the function np.ravel(), with results as our parameter.
        # Next, convert our unraveled results into a list by using a list() function
        stations = list(np.ravel(results))
        # Use Jsonify() function to convert the dictionary to a JSON file.
        return jsonify(stations)

                                                 ## Monthly Temperature Route ##
# Goal is to return the temperature observations for the previous year.
# Define the route
@app.route("/api/v1.0/tobs")

# Next, create a function called temp_monthly()
def temp_monthly():
        # Calculate the date one year ago from the last date in the database.
        prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        # Next step is to query the primary station for all the temperature observations from the previous year.
        results = session.query(Measurement.tobs).\
                filter(Measurement.station == 'USC00519281').\
                filter(Measurement.date >= prev_year).all()
        # Finally, unravel the results into a one-dimensional array and convert that array into a list.
        temps = list(np.ravel(results))
                # jsonify our temps list, and then return it.
        return jsonify(temps)


                                                    ## Statistics Route ##
# Define routes with both the starting and ending dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Next, create a function called stats()
# We need to add parameters to our stats() function: a start parameter and an end parameter.
def stats(start=None, end=None):
        
        # Create a query to select the minimum, average, and maximum temperatures from our SQLite database
        sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

        # Since we need to determine the starting and ending date, add an if-not statement to our code
        if not end:
                results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
                temps = list(np.ravel(results))
                return jsonify(temps)
        results = session.query(*sel).\
                        filter(Measurement.date >= start).\
                        filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

        # Calculate TMIN, TAVG, TMAX with start and stop
        results = session.query(*sel).\
                        filter(Measurement.date >= start).\
                        filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

if __name__  == "__main__":
        app.run(debug=True)