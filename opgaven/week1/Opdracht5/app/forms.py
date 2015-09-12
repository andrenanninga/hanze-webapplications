from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SessionForm(Form):
    key = StringField('key', validators=[DataRequired()])
    value = StringField('value', validators=[DataRequired()])