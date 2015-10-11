from flask import Flask, Blueprint, Response, request, render_template
from flask.ext.login import login_required, current_user
from app import app, db
from app.households.models import HouseholdDevice, Household, Device
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

@mod.route('/averages/<device_id>/', defaults={'comparison': 'type', 'area': 'global'})
@mod.route('/averages/<device_id>/<any("type", "category"):comparison>/', defaults={'area': 'global'})
@mod.route('/averages/<device_id>/<any("type", "category"):comparison>/<any("local", "global"):area>/')
@login_required
def average(device_id, comparison, area):
    # get the device as installed in a household
    houshold_device = HouseholdDevice.query.get(device_id)

    if comparison == 'type':
        # get the device(s) with the same id as the `household_device`
        comparison_devices = Device.query.filter_by(id=houshold_device.device.id).all()
    elif comparison == 'category':
        # get the devices of the same category
        comparison_devices = Device.query.filter_by(category=houshold_device.device.category).all()

    comparison_devices_ids = [d.id for d in comparison_devices]

    if area == 'global':
        # get the installed devices with the above comparison globally
        houshold_devices = (HouseholdDevice.query
                                           .filter(HouseholdDevice.device_id.in_(comparison_devices_ids))
                                           .all())
    elif area == 'local':
        # get the installed devices with the above comparison in the local area
        # local area is defined by the 4 numbers in the postcode
        local_area = houshold_device.household.postcode[:4] + '%'
        houshold_devices = (HouseholdDevice.query
                                           .filter(HouseholdDevice.device_id.in_(comparison_devices_ids))
                                           .filter(HouseholdDevice.household.has(Household.postcode.like(local_area)))
                                           .all())

    response = {
        'measurements': {
            'single': averages_by_ids([houshold_device.id]),
            'average': averages_by_ids([hd.id for hd in houshold_devices])
        }
    }

    # Return json with measurements
    return Response(json.dumps(response), status=200, mimetype='application/json')

def averages_by_ids(ids):
    # query to select the average `meting` of the given householdDevices
    query = """
        SELECT app_hh, AVG(waarde) AS average, tijd AS time
        FROM meting 
        WHERE app_hh IN ({ids})
        GROUP BY tijd;
    """.format(ids=','.join(str(id) for id in ids))

    results = db.engine.execute(query)
    averages = []
    for measurement in results:
        averages.append({
            'time': str(measurement.time),
            'average': float(measurement.average)
        })

    return averages

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

    for d in device.householdDevices:
        print(d.household)

    test = [d for d in device.householdDevices if d.household.postcode[:4] == '9902']
    print(test)

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

def local(deviceHousehold, area='global', postcode=None):
    if area == 'global':
        return True
    else:
        return deviceHousehold.household.postcode[:4] == postcode[:4]

