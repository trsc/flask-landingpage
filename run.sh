source venv/bin/activate
export FLASK_APP=landing.py
export FLASK_DEBUG=1
export WERKZEUG_DEBUG_PIN=off
flask run --host=0.0.0.0
