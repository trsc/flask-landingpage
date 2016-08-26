# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, make_response
from model import db, initdb, Signup

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
))
app.config.from_envvar('LANDING_SETTINGS', silent=True)

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database using the command line."""
    # TODO: prevent this from being done on production
    initdb()
    print 'Initialized the database.'

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.route('/')
def show_landing():
    return render_template('landing.html')
