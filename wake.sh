#!/bin/bash
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py flush --noinput
python manage.py createsuperuser --noinput
gunicorn --config gunicorn-cfg.py -k uvicorn.workers.UvicornWorker core.asgi
