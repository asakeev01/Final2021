heroku config:set DISABLE_COLLECTSTATIC=1
python manage.py collectstatic
web: gunicorn shop.shop.wsgi --log-file -