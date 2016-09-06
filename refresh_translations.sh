#!/bin/bash
# Script to find export new translations

. venv/bin/activate
pybabel extract --project landing-page --version 1 -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
pybabel compile -d translations
