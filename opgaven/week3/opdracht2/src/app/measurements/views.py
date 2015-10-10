from flask import Flask, Blueprint, Response, request, render_template
from flask.ext.login import login_required, current_user
from app import app, db
from app.households.models import HouseholdDevice, Device
from operator import attrgetter
import json

mod = Blueprint('measurements', __name__, url_prefix='/measurements')

@mod.route('/')
@login_required
def index():
    householdDevices = current_user.households[0].householdDevices

    for householdDevice in householdDevices:
        householdDevice.name = householdDevice.device.name

    return render_template('measurements/index.html', devices=householdDevices)

@mod.route('/average-per-type')
@login_required
def average_per_type():
    device_id = request.args.get('device')
    area = request.args.get('area') or 'local'

    if device_id is None:
        return 'device parameter must be set', 400

    householdDevice = HouseholdDevice.query.get(device_id)

    # Get the definition of a device
    device = Device.query.filter_by(id=householdDevice.device.id).first()

    # Get the id of every device installed in a household
    ids = map(attrgetter('id'), device.householdDevices)
    # Convert list to string
    ids = ','.join(str(id) for id in ids)

    average = []
    single = []

    # Get the average measurement for each hour
    query = """
        SELECT app_hh, AVG(waarde) AS average, tijd AS time
        FROM meting 
        WHERE app_hh IN ({ids})
        GROUP BY tijd;
    """

    # Get the averages of the all devices
    results = db.engine.execute(query.format(ids=ids))
    for measurement in results:
        average.append({
            'time': str(measurement.time),
            'average': float(measurement.average)
        })

    # Get the average of the housholddevice
    results = db.engine.execute(query.format(ids=householdDevice.id))
    for measurement in results:
        single.append({
            'time': str(measurement.time),
            'average': float(measurement.average)
        })

    response = {
        'name': householdDevice.device.name,
        'max': householdDevice.device.max,
        'measurements': {
            'single': single,
            'average': average
        }
    }


    # Return json with measurements
    return Response(json.dumps(response), status=200, mimetype='application/json')

@mod.route('/average-per-kind')
@login_required
def average_per_kind():


    return
