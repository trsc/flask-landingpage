# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, make_response
from model import db, initdb, Signup
from flask_babel import Babel, gettext
from flask_assets import Environment, Bundle
from datetime import datetime
from peewee import IntegrityError
import config

app = Flask(__name__)
babel = Babel(app)

assets = Environment(app)
scss = Bundle('styles.scss', filters='pyscss', output='gen/styles.css')
assets.register('scss_all', scss)

# Load default config and override config from an environment variable
app.config.from_object('config.DevelopmentConfig')
app.config.from_envvar('FLASK_SETTINGS', silent=True)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

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

@app.route('/',methods=['GET', 'POST'])
def show_landing():
    if request.method == 'POST':
        email = request.form['email']
        #app.logger.debug(email)
        signup = Signup(email = email, signup_date = datetime.now())
        try:
            signup.save()
        except IntegrityError:
            pass
        return render_template('success.html')
    else:
        return render_template('landing.html')

if __name__ == '__main__':
    app.run()
