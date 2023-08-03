import os
import dj_database_url
import environ
from .common import *


env = environ.Env()

environ.Env.read_env()


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}

REDIS_URL = os.environ['REDIS_URL']


CELERY_BROKER_URL = REDIS_URL

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}