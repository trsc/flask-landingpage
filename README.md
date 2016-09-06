# Flask Landing page
A very lightweight landing page with email signup and i18n. It uses Python Flask and sqlite.

This project was originally created for [hellobudget.co](http://hellobudget.co)

# Setup
1. Install packages `sudo apt install python-pip python-virtualenv python-dev`
2. Create a python virtual environment: `virtualenv venv`
3. Enter virtual environment: `. venv/bin/activate`
3. Install python packages `pip install -r requirements.txt`
4. Initialize database: `export FLASK_APP=landing.py && flask initdb`
5. Run app in debug mode locally using `run.sh`

Also See here: http://flask.pocoo.org/docs/0.11/installation/#installation
Leave virtual environment with `$ deactivate`

# Translate
To initialise, do this:

1. Extract texts:  `pybabel extract --project landing-page --version 1 -F babel.cfg -o messages.pot .`
2. Init German translation (*only run this once*): `pybabel init -i messages.pot -d translations -l de`

If texts in source language have been changed or added:

1. `pybabel extract --project landing-page --version 1 -F babel.cfg -o messages.pot .`
4. Do translations
2. Continue as below

If translations have been changed:

3. Update `pybabel update -i messages.pot -d translations`
4. Compile: `pybabel compile -d translations`


# Installing a new package via pip
1. Install: `pip install peewee`
2. Save to requirements `pip freeze > requirements.txt`

# Production Notes for Apache
* [Here's a good tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps).
* Check Apache error log if you see a 500 error
* Make sure the following files and directories are universally writable. They will need be written to by the `www-data` user
   * `signups.db`
   * `/static/.webassets-cache/`
   * `/static/gen`
