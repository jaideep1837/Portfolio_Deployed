#!/bin/bash
python manage.py collectstatic --noinput
gunicorn aichatbot.wsgi:application --bind 0.0.0.0:8000