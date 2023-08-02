release: python manage.py migrate
wb: gunicorn storefront.wsgi
worker: celery -A storefront worker