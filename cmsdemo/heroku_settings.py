import os
from settings import *
import re

INSTALLED_APPS = list(INSTALLED_APPS)

INSTALLED_APPS.append('gunicorn')

if 'MAILGUN_SMTP_LOGIN' in os.environ:
    EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
    EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
    EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
    EMAIL_PORT = int(os.environ['MAILGUN_SMTP_PORT'])

PROJECT_NAME = 'cmsdemo'

if 'S3_KEY' in os.environ:
    AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET']

    DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
    AWS_STORAGE_BUCKET_NAME = "%s-media" % PROJECT_NAME

    STATICFILES_STORAGE="storage.StaticS3FileStorage"
    AWS_STATIC_STORAGE_BUCKET_NAME = '%s-static' % PROJECT_NAME
    STATIC_URL = "https://s3.amazonaws.com/%s/" % AWS_STATIC_STORAGE_BUCKET_NAME
    ADMIN_MEDIA_PREFIX = '%sadmin/'%STATIC_URL



if 'REDISTOGO_URL' in os.environ:
    pattern = re.compile(r'^redis://redistogo:(?P<password>[\w\d]+)@(?P<location>.+)/$')
    match = pattern.match(os.environ['REDISTOGO_URL'])
    if match:
        params = match.groupdict()

        CACHES = {
            'default': {
                'BACKEND': 'redis_cache.RedisCache',
                'LOCATION': params['location'],
                'OPTIONS': {
                    'DB': 0,
                    'PASSWORD': params['password'],
                },
            },
        }

if 'MONGOLAB_URI' in os.environ:
    pattern = re.compile(r'^mongodb://(?P<username>[\w\d]+):(?P<password>[\w\d]+)@(?P<host>.+):(?P<port>\d+)/(?P<database>[\w\d]+)'
    match = pattern.match(os.environ['MONGOLAB_URI'])
    if match:
        MONGO_HOST = params['host']
        MONGO_USERNAME = params['username']
        MONGO_PASSWORD = params['password']
        MONGO_PORT = params['port']
        MONGO_DB = params['database']

