from app.households.models import Device
from flask.ext.wtf import Form
from wtforms import RadioField
from wtforms.validators import Required

def deviceChoices():
    devices = Device.query.order_by(Device.name).all()
    choices = []

    for device in devices:
        choices.append((str(device.id), device.name))

    return choices

class DeviceForm(Form):
    device = RadioField('Type', [Required()], choices=deviceChoices())
