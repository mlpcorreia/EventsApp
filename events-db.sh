#!/bin/sh

python3 manage.py makemigrations logic
python3 manage.py migrate

exec "$@"