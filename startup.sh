#!/bin/bash
# start-server
while ! MIGRATIONS=$(/app/web/manage.py showmigrations --plan 2>&1); do
  sleep 5
done
set +e # grep returns an exit code if nothing is found
PENDING_MIGRATIONS=$(echo $MIGRATIONS | grep '\[ \]')
set -e
if [ ! -z "$PENDING_MIGRATIONS" ]
then
  while ! /app/web/manage.py makemigrations 2>&1; do
      sleep 5
  done
  while ! /app/web/manage.py migrate 2>&1; do
      sleep 5
  done
  while ! /app/web/manage.py loaddata datadump 2>&1; do
      sleep 5
  done
fi

cd /app/web
(gunicorn quantummanagement.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"
# /app/.local/bin/gunicorn -b 0:8000 -w 3 --reload c3.wsgi
