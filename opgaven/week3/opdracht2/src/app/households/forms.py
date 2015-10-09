from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required

class DeviceForm(Form):
    name = TextField('Naam', [Required()])
    maximum = TextField('Max', [Required()])
