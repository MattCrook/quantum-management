#!/bin/bash
# start-server
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)

fi
(gunicorn quantummanagement.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"









# set -e
# Check for migrations
# while ! MIGRATIONS=$(/app/manage.py showmigrations --plan 2>&1); do
#   sleep 5
# done
# #set +e # grep returns an exit code if nothing is found
# PENDING_MIGRATIONS=$(echo $MIGRATIONS | grep '\[ \]')
# # set -e
# if [ ! -z "$PENDING_MIGRATIONS" ]
# then
#   while ! manage.py makemigrations 2>&1; do
#       sleep 5
#   done
#   while ! manage.py migrate 2>&1; do
#       sleep 5
#   done
#   while ! manage.py loaddata datadump.json 2>&1; do
#       sleep 5
#   done
# fi
# # /app/manage.py collectstatic -v 3 --noinput
# # cd /app
# # /app/.local/bin/gunicorn -b 0:8000 -w 3 --reload c3.wsgi
# fi
# (gunicorn quantummanagement.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
# nginx -g "daemon off;"
