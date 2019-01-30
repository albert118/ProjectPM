"""
Production settings extension (with some alterations), see original at:
https://github.com/arocks/edge/blob/master/src/project_name/settings/development.py

In production set the environment variable like this:
DJANGO_SETTINGS_MODULE=Devise.settings.production
""" 
#    
from .base import *
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = env('DEBUG')
TEMPLATE_DEBUG = False

# Strict password authentication and validation
# To use this setting, install the Argon2 password hashing algorithm.
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Must mention ALLOWED_HOSTS in production!
# ALLOWED_HOSTS = ["Devise.com"]

# Cache the templates in memory to improve performance
loaders = [
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

TEMPLATES[0]["OPTIONS"].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# logs are above BASE_DIR for ease of access when their needed, 
# to avoid cd'ing to the project dir
LOGFILE_ROOT = os.path.dirname("logs")

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "proj_log_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGFILE_ROOT, "project.log"),
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {"project": {"handlers": ["proj_log_file"], "level": "DEBUG"}},
}

logging.config.dictConfig(LOGGING)