"""
<<<<<<< HEAD
Django settings for django_todo project.
Generated by 'django-admin startproject' using Django 2.2.12.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
=======
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = '8e*wtvhkfhel@(a^pi2syy(n2h-hznwj3nkb-e@!_@xsw^rhpx'
=======
SECRET_KEY = 'i35jt$pq^n@w53(l*7w^t93ndu*v8vyg%u1in++@*e_v-7@xhh'
>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
<<<<<<< HEAD
ALLOWED_HOSTS = ['localhost']
=======
ALLOWED_HOSTS = []
>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d
=======
ALLOWED_HOSTS = ['localhost']
>>>>>>> a43c8da11b7d61dc9023c4b6a2f308a734b97804


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
<<<<<<< HEAD
    'todo_app',
=======
>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d
=======
    'todo_app',
>>>>>>> a43c8da11b7d61dc9023c4b6a2f308a734b97804
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

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a43c8da11b7d61dc9023c4b6a2f308a734b97804
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
<<<<<<< HEAD
    }
}
=======
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
=======
>>>>>>> a43c8da11b7d61dc9023c4b6a2f308a734b97804
    }
}


>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

<<<<<<< HEAD
<<<<<<< HEAD
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
=======
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d
=======
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
>>>>>>> a43c8da11b7d61dc9023c4b6a2f308a734b97804

USE_I18N = True

USE_L10N = True

<<<<<<< HEAD
USE_TZ = False
=======
USE_TZ = True
>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
=======
>>>>>>> 454c13bd336f8009c8f89e1fd080d908166add3d
