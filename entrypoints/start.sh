#!/bin/bash

python /app/manage.py migrate
python manage.py runserver 0.0.0.0:8000