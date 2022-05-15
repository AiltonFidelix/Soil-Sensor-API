#!/usr/bin/env bash

if [ ! -f db.sqlite3 ]; then
    python manage.py migrate
fi

gunicorn --bind 0.0.0.0:5000 setup.wsgi