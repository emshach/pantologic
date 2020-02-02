"""
Django settings for pantologic project.

Generated by 'django-admin startproject' using Django 1.11.18.

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
SECRET_KEY = 'dqp%l_+ot3wz-l=jhh*iy-0@sdr5$9ziuiz!$e+u0!e@b&1@za'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [ 'app.sandbox0.com' ]


# Application definition

INSTALLED_APPS = [
    'aries',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',
    'crispy_forms',
    'guardian',
    'rest_framework',
    'friede',
    # 'allauth',
    # 'allauth.social',
    # # 'allauth.socialaccount.providers.agave',
    # # 'allauth.socialaccount.providers.amazon',
    # # 'allauth.socialaccount.providers.angellist',
    # # 'allauth.socialaccount.providers.asana',
    # 'allauth.socialaccount.providers.auth0',
    # # 'allauth.socialaccount.providers.authentiq',
    # # 'allauth.socialaccount.providers.baidu',
    # # 'allauth.socialaccount.providers.basecamp',
    # # 'allauth.socialaccount.providers.bitbucket',
    # # 'allauth.socialaccount.providers.bitbucket_oauth2',
    # # 'allauth.socialaccount.providers.bitly',
    # # 'allauth.socialaccount.providers.cern',
    # # 'allauth.socialaccount.providers.coinbase',
    # # 'allauth.socialaccount.providers.dataporten',
    # # 'allauth.socialaccount.providers.daum',
    # # 'allauth.socialaccount.providers.digitalocean',
    # # 'allauth.socialaccount.providers.discord',
    # # 'allauth.socialaccount.providers.disqus',
    # # 'allauth.socialaccount.providers.douban',
    # # 'allauth.socialaccount.providers.draugiem',
    # # 'allauth.socialaccount.providers.dropbox',
    # # 'allauth.socialaccount.providers.dwolla',
    # # 'allauth.socialaccount.providers.edmodo',
    # # 'allauth.socialaccount.providers.eveonline',
    # # 'allauth.socialaccount.providers.evernote',
    # 'allauth.socialaccount.providers.facebook',
    # # 'allauth.socialaccount.providers.feedly',
    # # 'allauth.socialaccount.providers.fivehundredpx',
    # # 'allauth.socialaccount.providers.flickr',
    # # 'allauth.socialaccount.providers.foursquare',
    # # 'allauth.socialaccount.providers.fxa',
    # # 'allauth.socialaccount.providers.github',
    # # 'allauth.socialaccount.providers.gitlab',
    # 'allauth.socialaccount.providers.google',
    # # 'allauth.socialaccount.providers.hubic',
    # # 'allauth.socialaccount.providers.instagram',
    # # 'allauth.socialaccount.providers.jupyterhub',
    # # 'allauth.socialaccount.providers.kakao',
    # # 'allauth.socialaccount.providers.line',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # # 'allauth.socialaccount.providers.mailru',
    # # 'allauth.socialaccount.providers.mailchimp',
    # # 'allauth.socialaccount.providers.meetup',
    # # 'allauth.socialaccount.providers.naver',
    # # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.openid',
    # # 'allauth.socialaccount.providers.orcid',
    # # 'allauth.socialaccount.providers.paypal',
    # # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.pinterest',
    # 'allauth.socialaccount.providers.reddit',
    # # 'allauth.socialaccount.providers.robinhood',
    # # 'allauth.socialaccount.providers.shopify',
    # 'allauth.socialaccount.providers.slack',
    # # 'allauth.socialaccount.providers.soundcloud',
    # # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.stackexchange',
    # # 'allauth.socialaccount.providers.steam',
    # # 'allauth.socialaccount.providers.stripe',
    # # 'allauth.socialaccount.providers.trello',
    # # 'allauth.socialaccount.providers.tumblr',
    # # 'allauth.socialaccount.providers.twentythreeandme',
    # # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # # 'allauth.socialaccount.providers.untappd',
    # # 'allauth.socialaccount.providers.vimeo',
    # # 'allauth.socialaccount.providers.vimeo_oauth2',
    # # 'allauth.socialaccount.providers.vk',
    # # 'allauth.socialaccount.providers.weibo',
    # # 'allauth.socialaccount.providers.weixin',
    # 'allauth.socialaccount.providers.windowslive',
    # # 'allauth.socialaccount.providers.xing',
    'intrepid',
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

ROOT_URLCONF = 'pantologic.urls'

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

WSGI_APPLICATION = 'pantologic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.postgresql',
        'NAME'     : 'pantologic',
    },
    # 'fallback': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
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

AUTHENTICATION_BACKENDS = [
    'aries.auth.AnonymousAuthBackend',
    'django.contrib.auth.backends.ModelBackend', # default
    # 'allauth.account.auth_backends.AuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = '/usr/local/share/pantologic/app/static/'
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}
SITE_ID = 1

# Custom user model
AUTH_USER_MODEL = 'aries.User'
