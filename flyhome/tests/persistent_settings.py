from .test_settings import *  # NOQA

EXTERNAL_APPS += []

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}