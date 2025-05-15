import os
from pathlib import Path
from mongoengine import connect

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'samandagangoalb'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # Required for static files
    'rest_framework',              # Django REST framework
    'corsheaders',                 # CORS headers for cross-origin requests
    'products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",  # Allow requests from the frontend
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'petstore.urls'

WSGI_APPLICATION = 'petstore.wsgi.application'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL prefix for static files

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Path to your static files directory
]

# Optional: For production, define STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Where static files are collected

# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for development

# MongoDB Configuration
MONGODB_DATABASE = 'petstore'
MONGODB_HOST = 'mongodb://localhost:27017/'

connect(
    db=MONGODB_DATABASE,
    host=MONGODB_HOST,
    alias='default'  # Explicitly set the default connection alias
)