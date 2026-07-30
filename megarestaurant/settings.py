"""
Django settings for megarestaurant project.
"""
from dotenv import load_dotenv
import os
from pathlib import Path
from django.contrib.messages import constants as messages
import dj_database_url
import environ

load_dotenv()  

env = environ.Env()
environ.Env.read_env()  

# Unificamos la lectura del Hostname
HEROKU_HOSTNAME = os.environ.get('HEROKU_HOSTNAME', env('HEROKU_HOSTNAME', default=None))

SECRET_KEY = os.environ.get('SECRET_KEY', os.getenv('SECRET_KEY'))

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

DEBUG = True

# UN SOLO bloque de ALLOWED_HOSTS definitivo
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'megarestaurant.onrender.com',
]

if HEROKU_HOSTNAME:
    # Quitamos el https:// si viene en la variable para que Django no falle
    clean_host = HEROKU_HOSTNAME.replace('https://', '').replace('/', '')
    if clean_host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(clean_host)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'bookatable',
    'home_page',
    'contact_us',
    'menu_app',
    'crispy_bootstrap5',
]

SITE_ID = 1

LOGIN_REDIRECT_URl = '/'
LOGOUT_REDIRECT_URl = '/'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ACCOUNT_EMAIL_VERIFICATION = 'none'

CSRF_TRUSTED_ORIGINS = [
    'https://8000-zeststudio-p04restauran-lrz9o8qq380.ws-eu106.gitpod.io'
    'https://megarestaurant-20c7141b277b.herokuapp.com/',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'megarestaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'megarestaurant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3")

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
