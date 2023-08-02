import os
import environ
import dj_database_url
from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront3',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'Sh278137'
#     }
# }


env = environ.Env()

environ.Env.read_env()




DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}