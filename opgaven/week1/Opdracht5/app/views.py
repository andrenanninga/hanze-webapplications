from flask import render_template, session
from app import app
from .forms import SessionForm
from datetime import timedelta

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SessionForm()

    # session.permanent = True    
    # app.permanent_session_lifetime = timedelta(seconds=30)

    if form.validate_on_submit():
        session[form.key.data] = form.value.data

    return render_template('index.html',
                            form=form,
                            session=session)