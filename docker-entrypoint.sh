#!/bin/sh

echo "Waiting for postgres..."

./wait-for-it.sh db:5432 -- echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py compilemessages -l tr
python manage.py compilemessages -l en

exec "$@"
