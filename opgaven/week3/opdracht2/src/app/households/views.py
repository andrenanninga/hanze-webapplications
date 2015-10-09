from flask import Flask, Blueprint, g, flash, session, redirect, request, render_template
from flask.ext.login import login_required, current_user
from app import app, db
from app.households.models import Device
from app.households.forms import DeviceForm

mod = Blueprint('households', __name__, url_prefix='/households')

@mod.route('/')
@login_required
def index():
    print(current_user)
    print(current_user.households)
    print(current_user.households[0].devices)
    return render_template('households/index.html', households=current_user.households)

@mod.route('/add-device', methods=['GET', 'POST'])
@login_required
def add_device():
    form = DeviceForm(request.form)

    if form.validate_on_submit():
        device = Device(
            name=form.name.data,
            max=form.maximum.data,
            households=[current_user.households[0]]
        )

        db.session.add(device)
        db.session.commit()

        return redirect('/')

    return render_template('households/add-device.html', form=form)