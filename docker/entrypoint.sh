#!/bin/bash

python manage.py compilemessages 
python manage.py collectstatic --no-input  
python manage.py migrate --database=db_owner

rm -rf /srv/armatus/static

echo "Running command '$*'"
exec /bin/bash -c "$*"
