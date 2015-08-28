# -*- coding: utf-8 -*-
import os

# Use the ABS path for the project
_basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = True

ADMINS = frozenset(['youremail@yourdomain.com'])
CSRF_ENABLED = True
SECRET_KEY = '123456'


# Flask-Mail SMTP Setting
MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'notice@bearnote.com'
MAIL_PASSWORD = 'pass4bearnote'


# Mongodb Setting / MongoEngine
MONGODB_DB = MONGODB_INSTANCE_NAME
MONGODB_HOST = MONGODB_PORT_27017_TCP_ADDR
MONGODB_PORT = MONGODB_PORT_27017_TCP_PORT
MONGODB_USERNAME = MONGODB_USERNAME
MONGODB_PASSWORD = MONGODB_PASSWORD


# Unkown What it is.
THREADS_PER_PAGE = 8

# CSRF
CSRF_ENABLED = True
CSRF_SESSION_KEY = "123456"


# Unkown What it is.
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}