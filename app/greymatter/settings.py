import os
import json
from pathlib import Path

#with open ('/etc/greymatter-store-config.json') as config_file:
#    config = json.load(config_file)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o0br^cv6#og6gyby0e5@i19fb4#rxn2bp00qf8es#8@(+vim^i'
#SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['172.233.128.129', 'localhost']

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'
# STRIPE_API_KEY_PUBLISHABLE = 'pk_live_51NrHiyKt8JHfvphAxjojBVdDvWAogS8NgPZHIsAyib7S9C2n2bkXgE44Roq88zcqBBtpFnMCSpxIEdJ8foV40gSa00gns0N9d9'
# STRIPE_API_KEY_HIDDEN = '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'
STRIPE_API_KEY_PUBLISHABLE = 'pk_test_51NrHiyKt8JHfvphA6AW5lzeLBc4GKMtvD80imzLjmogNxX1Ygu9IsnBLJRyxFkZpxmW3aXDpjVEERorwuchnPblu00ncdlgnlu'
STRIPE_API_KEY_HIDDEN = 'sk_test_51NrHiyKt8JHfvphA6u0um2wjj1M8M4YIlKWOWNFjLiEw7N93DvlHyJAUxvF8xqrD6iXRBV01JLGPYVuLAL9ocYOf00iX531o3G'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cart',
    'core',
    'product',
    'order',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'greymatter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'greymatter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
