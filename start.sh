#!/bin/bash

python manage.py makemigrations
python manage.py migrate
#uwsgi --http :8000 --module lion.wsgi --enable-threads
python manage.py runserver 0.0.0.0:8000