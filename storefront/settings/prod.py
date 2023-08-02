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