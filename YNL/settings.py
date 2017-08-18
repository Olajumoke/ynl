"""
Django settings for YNL project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from config import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '2q_*um)ya-(3y1f6d^anann5y#f0y!3xs1+o!3i*y35bi7_u75'

# SECURITY WARNING: don't run with debug turned on in production!

if os.environ.get('RDS_DB_NAME', ''):
    DEBUG = False
else:
    DEBUG = True

DEFAULT_FROM_EMAIL  = 'yesornolive <olaoguns@zoho.com>'


if os.environ.get('RDS_DB_NAME'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],

            # 'OPTIONS': {
            #      "init_command": "SET foreign_key_checks = 0;",
            # },
        }
    }

    AWS_ACCESS_KEY_ID           = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY       = os.environ['AWS_SECRET_KEY']

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    # STATIC_ROOT = os.path.join(
    #  os.path.dirname(
    #   os.path.dirname(
    #    os.path.abspath(__file__))), 'static')

    STATIC_PATH = os.path.join(BASE_DIR, 'static')

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_STORAGE_BUCKET_NAME = 'yesnolive'

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATICFILES_LOCATION = 'static'

    #STATIC_URL  = "https://%s/%s/" %(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    STATIC_URL  = "https://%s/" %AWS_S3_CUSTOM_DOMAIN

    #STATIC_ROOT = "https://%s/%s/" %(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    # STATIC_ROOT = "https://s3-eu-west-1.amazonaws.com/zaposta/static/"

    # Example: "http://media.lawrence.com/static/"
    #STATIC_URL = 'https://zaposta-live.s3.amazonaws.com/static/'
    #STATIC_URL = 'https://zaposta.com.s3.amazonaws.com/static/'
    #STATIC_URL = 'https://s3-eu-west-1.amazonaws.com/%s/static/' %AWS_STORAGE_BUCKET_NAME

    # Additional locations of static files
    STATICFILES_DIRS = (
        STATIC_PATH,
    )

    #MEDIA_ROOT = 'media' #os.path.join(BASE_DIR, "media")
    #MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    #MEDIA_URL = 'https://s3-eu-west-1.amazonaws.com/zaposta-live/'
    MEDIA_LOCATION = 'media'
    #MEDIA_URL = "https://%s/%s/" %(AWS_S3_CUSTOM_DOMAIN, MEDIA_LOCATION)
    MEDIA_ROOT = MEDIA_URL = "https://%s/" %AWS_S3_CUSTOM_DOMAIN
    #STATIC_URL  = "https://%s/%s/" %(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    #AWS_QUERYSTRING_AUTH = False

    BROKER_TRANSPORT = 'sqs'
    BROKER_TRANSPORT_OPTIONS = {
        'region': 'eu-west-1a',
    }
    BROKER_USER = AWS_ACCESS_KEY_ID
    BROKER_PASSWORD = AWS_SECRET_ACCESS_KEY

    SERVER_EMAIL = DEFAULT_FROM_EMAIL

    # EMAIL_USE_TLS = True
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = ''
    # EMAIL_HOST_PASSWORD = '' #my gmail password
    # EMAIL_HOST_USER = '' #my gmail username
    # EMAIL_PORT =
    # DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

    ADMINS = (
    #('Abiodun Ajibike', 'ajibike.ca@gmail.com'),
    ('Isaiah Iyede', 'isaiahiyede.ca@gmail.com'),
    ('Olajumoke Ogundeko', 'olajumoke.ca@gmail.com'),
    )

    #CACHES = {
    #    'default': {
    #        'BACKEND': 'django_elasticache.memcached.ElastiCache',
    #        'LOCATION': 'ca-cluster.dnntu4.cfg.euw1.cache.amazonaws.com:11211',
    #        'TIMEOUT': 60*5,
    #    }
    #}


    # #SSL Security
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    os.environ['wsgi.url_scheme'] = 'https'
    
    SESSION_SECURITY_WARN_AFTER = 60 * 60 #1hour
    SESSION_SECURITY_EXPIRE_AFTER = 60 * 60 + 10 #1hour 10 mins

# elif os.environ.get('yesnolive$yesornolive', ''):
#     DEBUG = False
# 

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'ynl_db',
            'USER': 'root',                      # Not used with sqlite3.
            'PASSWORD': 'root',                  # Not used with sqlite3.
            'HOST': '127.0.0.1',                 # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',

            # 'OPTIONS': {
            #      "init_command": "SET foreign_key_checks = 0;",
            # },                  # Set to empty string for default. Not used with sqlite3.
            },
    }

    STATIC_ROOT = '' #os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        'static',
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    MEDIA_ROOT = 'media' #os.path.join(PROJECT_PATH, "media")

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    #MEDIA_URL = 'http://127.0.0.1:9002/media/'
    MEDIA_URL = '/media/'


    ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    )

    EMAIL_USE_TLS = True
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.zoho.com'
    EMAIL_HOST_PASSWORD = '6xqnap01d0i2' #my gmail password
    EMAIL_HOST_USER = 'olaoguns@zoho.com' #my gmail username
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

    INTERNAL_IPS = ('127.0.0.1',)

    SECRET_KEY = '2q_*um)ya-(3y1f6d^anann5y#f0y!3xs1+o!3i*y35bi7_u75'

    FLUTTERWAVE_API_KEY         = "tk_WfDHIy0sdRozMqtLUBvE"
    FLUTTERWAVE_MERCHANT_KEY    = "tk_eLBuQpHtNr"

    SESSION_SECURITY_WARN_AFTER = 60 * 60 * 24 * 2 #2days
    SESSION_SECURITY_EXPIRE_AFTER = 60 * 60 * 24 * 2 #2days


SITE_ID = 1


ALLOWED_HOSTS = [
    'localhost',
    'yesnolive.pythonanywhere.com',
    '.yesornolive.com',
]


SESSION_EXPIRE_AT_BROWSER_CLOSE = True


TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
         TEMPLATE_PATH,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',
            ],
            'debug': DEBUG,
        },
    },
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    # 'backends.EmailAuthBackEnd',
    # 'backends.UsernameAuthBackEnd',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
    'YNL.pipeline.save_profile',
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

LOGIN_URL = '/login/Page/'
LOGOUT_URL = '/user-logout/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'YNL.wsgi.application'

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
)


YNL_APPS= (
    'general',
    'wallet',
    'ynladmin',
    'gameplay',
    'django.contrib.admin',
    'social_django',
    'tinymce',
)


INSTALLED_APPS = DJANGO_APPS + YNL_APPS

if not os.environ.get('RDS_DB_NAME'):
    YNL_APPS+=('debug_toolbar',)
 
    
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]    

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

ROOT_URLCONF = 'YNL.urls'

WSGI_APPLICATION = 'YNL.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Lagos'

USE_L10N = True

USE_TZ = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


TMP_ROOT = os.path.join(os.path.dirname(__file__), '../static/tmp')
FILES_ROOT = os.path.join(os.path.dirname(__file__), '../static/files')


FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)


from django.http import UnreadablePostError
def skip_unreadable_post_error(record):
    if record.exc_info:
        exc_type, exc_value = record.exc_info[:2]
        if isinstance(exc_value, UnreadablePostError):
            return False
    return True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'skip_unreadable_posts':{
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_unreadable_post_error,
        },

    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'skip_unreadable_posts'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        # 'null':{
        #         'class': 'django.utils.log.NullHandler',
        # }
        'null':{
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        }
    }
}








