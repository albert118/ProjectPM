"""
Django settings for wwwProjectPM project.
Base settings (with some alterations), see original at:
https://github.com/arocks/edge/blob/master/src/project_name/settings/base.py

For more information on django-settings files, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/

Before deployment, always double check:
See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
"""
from django.urls import reverse_lazy
from pathlib import Path
import environ
import os

################################################################################
# Use Twelve-Factor system. Read more: https://12factor.net/
# Allows all credentials to be read from environment variables. Increasing stability
# and security.
################################################################################

env = environ.Env()

env_file = Path(__file__).resolve().parent / "local.env"
if env_file.exists():
    environ.Env.read_env(str(env_file))

################################################################################
# Uses pathlib for concrete path instantiation. Read more:
# https://docs.python.org/3/library/pathlib.html?highlight=pathlib%20path#module-pathlib
# Build paths inside the project like this: BASE_DIR / "directory"
# BASE_DIR is set to wwwProjectPM, by default this is 'myproject'.
# UPDATE: uses environ.Path functionality to read BASE_DIR
################################################################################

# BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = "/var/www/ProjectPM/src"
SITE_ROOT = "/var/www/"

################################################################################
# Static & media file configuration (CSS, JavaScript, Images).
# add non-app-specific STATICFILES_DIRS here.
# https://docs.djangoproject.com/en/dev/howto/static-files/
################################################################################

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # LAMP server static directory added by default.
    # insert more static file directories here
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, "static")
MEDIA_ROOT = os.path.join(SITE_ROOT, "media")
MEDIA_URL = "/media/"
PUBLIC_ROOT = os.path.join(SITE_ROOT, "public")
PUBLIC_URL = "/public/"

# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")

#CACHES = {
 #   'default': env.cache(),
  #  'redis': env.cache('REDIS_URL', default='Redis: rediscache://')
#}

################################################################################
# Use Django templates using the new Django 1.8 TEMPLATES settings
# see https://docs.djangoproject.com/en/dev/ref/settings/#templates for more info
################################################################################

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # str(BASE_DIR / "templates"),
            # LAMP server top-level templates for easy access
            # to base templates. Add this directory or remove this option.
            os.path.join(BASE_DIR, 'templates')
            # insert more TEMPLATE_DIRS here
        ],
        # load template folder within app directories
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Application definition
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "easy_thumbnails",
    "authtools",
    "crispy_forms",
    "profiles",
    "accounts",
    "BetterResume",
    # add more apps here
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# wwwProjectPM's base url configuration.
# https://docs.djangoproject.com/en/2.1/ref/settings/#root-urlconf
ROOT_URLCONF = "wwwProjectPM.urls"

WSGI_APPLICATION = "wwwProjectPM.wsgi.application"

################################################################################
# # Database configuration settings
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Gets NAME, USER & PASSWORD from env var's. Make sure to create
# a user in MySQL before attempting to make migrations! Add the username and 
# password in the appropriate fields within the local.env file. 
################################################################################

DATABASES = {
    'default': env.db(),
    'extra': env.db('DATABASE_URL')
    # no default assigned. This will throw an error if it
    # can't read/access the database!
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = "en-au"

TIME_ZONE = "AET"

USE_I18N = True

USE_L10N = True

USE_TZ = True

################################################################################
# Allowed hosts are defined custom per run, only in the development settings is
# a default added. Ideally, these hosts should be added in either of the settings 
# extension files (production or development), but this will globally define them
# for the project.
################################################################################

ALLOWED_HOSTS = ['10.42.0.199']

# Authentication Settings
AUTH_USER_MODEL = "authtools.User"
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = "png"  # Default thumbnail extension.

# Define the importable names for use in .development & .production.
__all__ = [
    "ALLOWED_HOSTS",
    "STATICFILES_DIRS",
    "SITE_ROOT",
    "MEDIA_ROOT",
    "PUBLIC_ROOT",
    "MEDIA_URL",
    "STATIC_URL",
    "INSTALLED_APPS",
    "TEMPLATES",
    "ROOT_URLCONF",
    "WSGI_APPLICATION",
    "SECRET_KEY",
    "MIDDLEWARE",
    "BASE_DIR",
    "AUTH_USER_MODEL",
    "DATABASES",
]

