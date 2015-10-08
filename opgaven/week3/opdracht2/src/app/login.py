from flask import Blueprint
from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

__author__ = 'Lasse'

login = Blueprint('login', __name__)

@login.route("/login")
def login():
    return "login"
