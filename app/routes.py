from app import app

import os
import sys
from flask import render_template
import flask

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Flask Tutorial', flask_version=flask.__version__, flask_app=os.environ['FLASK_APP'], db_connection=os.environ['DATABASE_URL'], environment=os.environ['APP_SETTINGS'], python_version=sys.version)