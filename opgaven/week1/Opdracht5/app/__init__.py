from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import views