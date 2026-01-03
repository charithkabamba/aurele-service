#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput
# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear
python manage.py makemessages -a
# Compile message files
echo "Compiling message files..."
python manage.py compilemessages


# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn principal.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --timeout 120 \
    --preload
