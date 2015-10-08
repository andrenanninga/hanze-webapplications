from flask import Flask, Blueprint, g, flash, session, redirect, request, render_template
from flask.ext.login import login_user, logout_user, current_user
from werkzeug import check_password_hash, generate_password_hash
from app import app, db, login_manager
from app.users.forms import LoginForm, RegisterForm
from app.users.models import User

mod = Blueprint('users', __name__, url_prefix='/users')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in', 'success')
            return redirect('/')

        flash('Wrong email or password', 'danger')

    return render_template('users/login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
            phonenumber=form.phonenumber.data
        )

        print(generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        flash('Thanks for registering', 'success')
        return redirect('/')

    return render_template('users/register.html', form=form)