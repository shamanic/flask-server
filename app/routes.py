from app import app, db

import os
import sys
from flask import render_template
import flask
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Flask Tutorial', flask_version=flask.__version__, flask_app=os.environ['FLASK_APP'], db_connection=app.config.get('SQLALCHEMY_DATABASE_URI'), environment=os.environ['APP_SETTINGS'], python_version=sys.version)

@app.route('/db')
def dbTest():

    users = User.query.all()
    if users:
        return render_template('db.html', users=users)
    elif any(us.name == 'daoud' for us in users):
        u = User(username='audry', email='audry@shamanic.io')
        db.session.add(u)
        db.session.commit()

        return render_template('db.html', users=users)
    else:
        u = User(username='daoud', email='daoud@shamanic.io')
        db.session.add(u)
        db.session.commit()

        return render_template('db.html', users=users)

@app.route('/react/index')
def react():
    return render_template('react/index.html')