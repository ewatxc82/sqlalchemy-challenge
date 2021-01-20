import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    precip_list = []
    
    for date, prcp in results:
        for_dict = {}
        for_dict_date = prcp
        prcip_list.append(for_dict)

    return jsonify(all_names)

@app.route("/api/v1.0/precipitation")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    stations = {}


    results = session.query(Station.station, Station.name).all()
    for station, name in results:
        station_name = name

    session.close()

    return jsonify(stations)
    
    for date, prcp in results:
        for_dict = {}
        for_dict_date = prcp
        prcip_list.append(for_dict)

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    last_date = session.query(Measurement.date).order_by(Measurement.date).first()
    last_year_date = (dt.datetime.strptime(last_date[0], '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= last_year_date).order_by(Measurement.date).all()
    
    tobs_date_list = []
    
    for date, tobs in results:
        for_dict = {}
        for_dict[date] = tobs
        tobs_date_list.append(for_dict)
    
    session.close()
    
    return jsonify(tobs_date_list)