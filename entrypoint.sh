# preciser le shell
#!/bin/sh
set -e
# lancer le serveur

source /app/venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py makemessages -a
python manage.py compilemessages

if [ "$DJANGO_ENV" = "production" ]; then
    exec gunicorn principal.wsgi:application --bind 0.0.0:8000
else
    exec python manage.py runserver 0.0.0:8000
fi

