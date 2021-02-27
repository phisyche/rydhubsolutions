
web: gunicorn djangobase.wsgi:application --log-file - --log-level debug
python src/manage.py collectstatic --noinput
python src/manage.py migrate