from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from app import main

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.households.views import mod as householdsModule
app.register_blueprint(householdsModule)

from app.measurements.views import mod as measurementsModule
app.register_blueprint(measurementsModule)