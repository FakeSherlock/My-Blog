from flask import render_template, Flask, request, url_for
from apps import app

from google.appengine.ext import db

@app.route('/')
@app.route('/login.html')
def index():
    return render_template("login.html")