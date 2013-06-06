#!/usr/bin/env python

from sentry.conf.server import *

import os
import dj_database_url
from urlparse import urlparse

DATABASES = {'default': dj_database_url.config(default='sqlite:///' +
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db.sqlite') )}

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))
SENTRY_WEB_OPTIONS = {
    'workers': 3,  
    'worker_class': 'gevent',
}


SENTRY_PUBLIC = False
SENTRY_KEY = os.environ.get('SENTRY_KEY')

if 'MAIL_TO' in os.environ:
    ADMINS = [('J. Doe', os.environ['MAIL_TO'])]
    SENTRY_ADMINS = [os.environ['MAIL_TO']]

SERVER_EMAIL = os.environ.get('SENDGRID_USERNAME')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
