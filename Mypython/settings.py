"""
Django settings for Mypython project.

Generated by 'django-admin startproject' using Django 1.11.9.

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
SECRET_KEY = '$jh$#!!dk@d2zrs6h8i6ue3ppaf%(-$l49cou70bkvw#k6x45$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','172.23.23.222','192.168.1.12']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    #'xadmin',
    #'crispy_forms',
    #'reversion',
    'Myuser',
   # 'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DEBUG_TOOLBAR_PANELS = [
 'debug_toolbar.panels.versions.VersionsPanel',
 'debug_toolbar.panels.timer.TimerPanel',
 'debug_toolbar.panels.settings.SettingsPanel',
 'debug_toolbar.panels.headers.HeadersPanel',
 'debug_toolbar.panels.request.RequestPanel',
 'debug_toolbar.panels.sql.SQLPanel',
 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
 'debug_toolbar.panels.templates.TemplatesPanel',
 'debug_toolbar.panels.cache.CachePanel',
 'debug_toolbar.panels.signals.SignalsPanel',
 'debug_toolbar.panels.logging.LoggingPanel',
 'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
# debug toolbar只会在你设置的IP上显示，这是一个元组，可以添加多个
INTERNAL_IPS = ('127.0.0.1','172.23.23.222' )

# debug toolbar需要jQuery的支持，默认会去搜Google的jQuery，但是不会找到的
# 所有我们需要设置本地的jQuery给他使用
# 在当前的项目目录下新建static目录，然后将下载好的jQuery文件放进去
DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': r"https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js",
                        }

ROOT_URLCONF = 'Mypython.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Mypython\\templates')],
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

WSGI_APPLICATION = 'Mypython.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'zh-HANS'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = "/Myuser/login"