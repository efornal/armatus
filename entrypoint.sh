#!/bin/bash

#python manage.py migrate --database=db_owner
python manage.py compilemessages
python manage.py collectstatic --noinput

echo "Running command '$*'"
exec /bin/bash -c "$*"
