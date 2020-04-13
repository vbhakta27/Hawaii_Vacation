import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from datetime import datetime
import dateutil.relativedelta

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>Returns a JSON list of precipitation data for last year of the data set<br/><br/>"
        f"/api/v1.0/stations<br/>Return a JSON list of stations<br/><br/>"
        f"/api/v1.0/tobs<br/>Return a JSON list of temperature observations (TOBS) for the previous year from station USC00519281 (most active station)<br/><br/>"
        f"/api/v1.0/(start)<br/>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date (date format: m-d-y) <br/><br/>"
        f"/api/v1.0/(start)/(end)<br/>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range (date format: m-d-y; max end is 8/23/17)<br/><br/>"
    )

##################################################################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Query to retrieve the last 12 months of precipitation data"""
    # Get last date from database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date

    # Convert latest date into datetime format so we can subtract a year from it to get filter date
    formatted_last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    filter_date = formatted_last_date - dateutil.relativedelta.relativedelta(months=12)
 
    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= filter_date).all()
 
    session.close()

    # Create a dictionary from the row data and append to a list of rain_data
    rain_data = []
    precipitation_dict = {}
    for date, prcp in results:

        precipitation_dict = {}
        precipitation_dict[date]=prcp
        rain_data.append(precipitation_dict)

    return jsonify(rain_data)

##################################################################################################

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Query to retrieve station and their names"""
    results = session.query(Station.station,Station.name).all()
    session.close()

    # Create list to store station and their names 
    station_names = []
    for station in results:
        station_dict={}
        station_dict[station[0]]=station[1]
        station_names.append(station_dict)

    return jsonify(station_names)

##################################################################################################

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Get last date from database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date

    # Convert latest date into datetime format so we can subtract a year from it to get filter date
    formatted_last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    filter_date = formatted_last_date - dateutil.relativedelta.relativedelta(months=12)

    """Query to retrieve dates and temps for station USC00519281"""
    results = session.query(Measurement.date,Measurement.tobs).order_by(Measurement.date).filter(Measurement.station == "USC00519281").filter(Measurement.date >= filter_date).all()

    session.close()

    # Create list to store station names and their data count
    date_tobs = []
    for date, temp_obs in results:
        tobs_dict={}
        tobs_dict[date]=temp_obs
        date_tobs.append(tobs_dict)

    return jsonify(date_tobs) 

##################################################################################################

@app.route("/api/v1.0/<start>")
def get_temp_start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Get start date into datetime format
    date_object = datetime.strptime(start, '%m-%d-%y')
    
    # Query for all dates greater than start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= date_object).all()

    session.close()

    stats_dict = {"Minimum Temp":results[0][0],"Average Temp":results[0][1],"Maximum Temp":results[0][2]}
    
    return jsonify(stats_dict)

##################################################################################################

@app.route("/api/v1.0/<start>/<end>")
def get_temp_start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Get start date into datetime format
    start_date = datetime.strptime(start, '%m-%d-%y')
    end_date = datetime.strptime(end, '%m-%d-%y')
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    stats_dict = {"Minimum Temp":results[0][0],"Average Temp":results[0][1],"Maximum Temp":results[0][2]}
    
    return jsonify(stats_dict)

if __name__ == '__main__':
    app.run(debug=True)
