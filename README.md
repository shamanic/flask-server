# flask-server
Here's a Flask web server written in Python with these additional libraries: 
SQLAlchemy (db backend orm)
Flask-SQLAlchemy (add'l support for flask)
flask-marshmallow (layer for flask and object (de-)serialization)
## setup
get a python (I'm on 3.7.4) and get pip3 - with homebrew this appears to be trivial (use the `brew install python3` command).
## environments
I have set up a DevelopmentConfig, StagingConfig and ProductionConfig that we can switch between. We can eventually push things out to Heroku which will be where the Prod environment will be hosted, and use its Postgres credentials, etc.
## models
There is a user model, now - but we will need to build out game settings models that will fill JSON objects (or just one?) and then be configurable. I imagine the "game" model and "state" model could be two JSONB columns in the Postgres DB.

A quick first pass for models: Users, Locations, Devices, GameObjects, Admin. All may also have their own [TableName]_Flags tables for more admin and setting stuff like "IsActive" or "IsAppleDevice" etc.
## todo
 I'd like to get facility with multiple projects on the same Heroku dyno, so small machine-learning and data crunching tasks can spin while the Flask server is serving requests.