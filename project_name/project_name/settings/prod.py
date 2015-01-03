from .base import *  # noqa

DEBUG = False
TEMPLATE_DEBUG = DEBUG

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

ALLOWED_HOSTS = ['*']
