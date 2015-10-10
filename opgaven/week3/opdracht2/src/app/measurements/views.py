from flask import Flask, Blueprint, Response
from flask.ext.login import login_required, current_user
from app import app, db
from app.households.models import Device
from operator import attrgetter
import json

mod = Blueprint('measurements', __name__, url_prefix='/measurements')

@mod.route('/average-per-type')
@login_required
def average_per_type():
    # Get the definition of a device
    device = Device.query.filter_by(name='windmolen op dak').first()

    # Get the id of every device installed in a household
    ids = map(attrgetter('id'), device.householdDevices)
    # Convert list to string
    ids = ','.join(str(id) for id in ids)

    # Get the average measurement for each hour
    query = """
        SELECT AVG(waarde) AS average, tijd AS time
        FROM meting 
        WHERE app_hh IN ({ids})
        GROUP BY tijd;
    """.format(ids=ids)

    results = db.engine.execute(query)
    measurements = []

    # Map the result to dict measurements
    for measurement in results:
        measurements.append({
            'time': str(measurement.time),
            'average': str(measurement.average)
        })

    response = {
        'name': device.name,
        'max': device.max,
        'measurements': measurements
    }

    # Return json with measurements
    return Response(json.dumps(response), status=200, mimetype='application/json')

@mod.route('/average-per-kind')
@login_required
def average_per_kind():


    return
