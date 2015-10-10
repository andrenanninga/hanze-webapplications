from app import app
from flask import Flask, render_template
from flask.ext.login import login_required, current_user
from app.users.models import User
from app.households.models import Household, Device

@app.route('/')
@app.route('/index')
@login_required
def main():
    print(current_user.households[0].householdDevices)
    return render_template('index.html', user=current_user)
