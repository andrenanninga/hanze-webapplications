from flask import render_template, session
from app import app
from .forms import SessionForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SessionForm()

    if form.validate_on_submit():
        session[form.key.data] = form.value.data

    print(session)

    return render_template('index.html',
                            form=form,
                            session=session)