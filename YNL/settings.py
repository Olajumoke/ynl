"""
Django settings for YNL project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2q_*um)ya-(3y1f6d^anann5y#f0y!3xs1+o!3i*y35bi7_u75'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




ROOT_URLCONF = 'YNL.urls'

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
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'YNL.wsgi.application'

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


YNL_APPS= (
    'general',
    'wallet',
    'ynladmin',
    'gameplay',
    'django.contrib.admin',
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
]    

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

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


EMAIL_USE_TLS = True
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_PASSWORD = '6xqnap01d0i2' #my gmail password
EMAIL_HOST_USER = 'olaoguns@zoho.com' #my gmail username
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
        'static',
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

MEDIA_ROOT = 'media'

MEDIA_URL = '/media/'
