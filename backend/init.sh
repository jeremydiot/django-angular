#!/bin/bash

ENV_PATH="env/"
# DB_PATH="db.sqlite3"

# deactivate
# [ -f $DB_PATH ] && rm $DB_PATH
[ ! -d $ENV_PATH ] && python3 -m venv env

source env/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements/common.txt
python3 -m pip install -r requirements/development.txt