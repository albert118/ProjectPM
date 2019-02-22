"""
Devlopment settings extension (with some alterations), see original at:
https://github.com/arocks/edge/blob/master/src/project_name/settings/development.py

This is the default settings extension. If not,
reset the environment variable like this:
DJANGO_SETTINGS_MODULE=wwwProjectPM.settings.development
"""

from .base import *
import sys
from pathlib import Path
import logging.config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]["OPTIONS"].update({"debug": True})

# Turn off debug while imported by Celery with a workaround
# See http://stackoverflow.com/a/4806384
if "celery" in sys.argv[0]:
    DEBUG = False

# Less strict password authentication and validation
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = []

# Django Debug Toolbar
INSTALLED_APPS += ("debug_toolbar",)

# Additional middleware introduced by debug toolbar
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Show emails to console in DEBUG mode.
# Re-enable if running an email service. Mine weren't, so this was for convienience.
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Show thumbnail generation errors
THUMBNAIL_DEBUG = True

# Allow internal IPs for debugging & convenience
ALLOWED_HOSTS += ["127.0.0.1", "127.0.1.1"]

# logs are above BASE_DIR for ease of access when their needed, 
# to avoid cd'ing to the project dir
LOGFILE_ROOT = Path(BASE_DIR.parent, "logs")

# Reset logging
# (see http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)
# TLDR: easier to do it from scratch. Disable logging, then redo with Python API's.
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
        "django_log_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": Path(LOGFILE_ROOT, "django.log"),
            "formatter": "verbose",
        },
        "proj_log_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": Path(LOGFILE_ROOT, "project.log"),
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["django_log_file"],
            "propagate": True,
            "level": "DEBUG",
        },
        "project": {"handlers": ["proj_log_file"], "level": "DEBUG"},
    },
}

logging.config.dictConfig(LOGGING)