# -*- coding: utf-8 -*-

"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from typing import Tuple

from server.settings.components import BASE_DIR, config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

SECRET_KEY = config('DJANGO_SECRET_KEY')

# Application definition:
SHARED_APPS: Tuple[str, ...] = (
    'tenant_schemas',  # mandatory, should always be before any django app

    'django.contrib.auth',  # Defined in both shared apps and tenant apps
    'django.contrib.contenttypes',  # Defined in both shared apps and tenant apps
    'tenant_users.permissions',  # Defined in both shared apps and tenant apps
    'tenant_users.tenants',  # defined only in shared apps

    'server.tenants',  # Custom defined app that contains the TenantModel. Must NOT exist in TENANT_APPS
    'server.accounts',  # Custom app that contains the new User Model (see below). Must NOT exist in TENANT_APPS

    'django.contrib.sessions',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Security:
    'axes',

    # REST
    'rest_framework',   # Defined in both shared apps and tenant apps
    # REST authentication
    'rest_framework.authtoken',
    'rest_auth',
)

TENANT_APPS: Tuple[str, ...] = (
    'django.contrib.auth',  # Defined in both shared apps and tenant apps
    'django.contrib.contenttypes',  # Defined in both shared apps and tenant apps
    'tenant_users.permissions',  # Defined in both shared apps and tenant apps

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Security:
    'axes',

    # REST
    'rest_framework',   # Defined in both shared apps and tenant apps

    # Your apps go here:
    'server.pages',
)

INSTALLED_APPS: Tuple[str, ...] = (
    # Default django apps:
    'tenant_schemas',  # mandatory, should always be before any django app

    'server.tenants',  # Custom defined app that contains the TenantModel. Must NOT exist in TENANT_APPS
    'server.accounts',  # Custom app that contains the new User Model (see below). Must NOT exist in TENANT_APPS

    'tenant_users.permissions',  # Defined in both shared apps and tenant apps
    'tenant_users.tenants',  # defined only in shared apps

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Security:
    'axes',

    # Your apps go here:
    'server.main_app',
    'server.pages',

    # REST
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',
)

MIDDLEWARE: Tuple[str, ...] = (
    'corsheaders.middleware.CorsMiddleware',
    # Content Security Policy:
    'csp.middleware.CSPMiddleware',

    # Referrer Policy:
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware',

    # Django:
    'tenant_schemas.middleware.TenantMiddleware',   # DTS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        # Choices are: postgresql_psycopg2, mysql, sqlite3, oracle
        'ENGINE': 'tenant_schemas.postgresql_backend',

        # Database name or filepath if using 'sqlite3':
        'NAME': config('POSTGRES_DB'),

        # You don't need these settings if using 'sqlite3':
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DJANGO_DATABASE_HOST'),
        'PORT': config('DJANGO_DATABASE_PORT', cast=int),
        'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
    },
}


DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',  # DTS
)

# Tenant Users
AUTH_USER_MODEL = 'accounts.TenantUser'

# Tenant Schemas
TENANT_MODEL = 'tenants.Client'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ('en', 'English'),
    ('th', 'Thai'),
)

LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'

STATIC_URL = '/static/'
MEDIA_ROOT = '/data/media'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Templates
# https://docs.djangoproject.com/en/1.11/ref/templates/api

TEMPLATES = [{
    'APP_DIRS': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # Contains plain text templates, like `robots.txt`:
        BASE_DIR.joinpath('server', 'templates'),
    ],
    'OPTIONS': {
        'context_processors': [
            # default template context processors
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },

}]

# Media files
# Media-root is commonly changed in production
# (see development.py and production.py).

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Django authentication system
# https://docs.djangoproject.com/en/1.11/topics/auth/

AUTHENTICATION_BACKENDS = (
    #  'django.contrib.auth.backends.ModelBackend',
    'tenant_users.permissions.backend.UserBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Security
# https://docs.djangoproject.com/en/1.11/topics/security/
ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
    'edutech.fastpages.code',
    '.fastpages.code',
]

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

CORS_ORIGIN_ALLOW_ALL=True
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(http?://)?(\w+\.)?fastpages.code$',
)

X_FRAME_OPTIONS = 'DENY'

# https://django-referrer-policy.readthedocs.io/
REFERRER_POLICY = 'no-referrer'
