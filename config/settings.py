
import os
from pathlib import Path

# ==================================================
# BASE DIRECTORY
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# SECURITY
# ==================================================

SECRET_KEY = "CHANGE-THIS-TO-A-LONG-RANDOM-SECRET-KEY"

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "jp3dhub-v2.vercel.app",
    "jp3dhub-v2-q7dupcnr3-elango0246.vercel.app",
]


# ==================================================
# APPLICATIONS
# ==================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "website",
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# URL CONFIGURATION
# ==================================================

ROOT_URLCONF = "config.urls"


# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates"
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ==================================================
# WSGI / ASGI
# ==================================================

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


# ==================================================
# DATABASE - SUPABASE POSTGRESQL
# ==================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",

        "NAME": "postgres",

        "USER": "postgres.qzbxsxziyvxajfymkoyi",

        # PUT YOUR NEW SUPABASE PASSWORD HERE
        "PASSWORD": "elango@AI@0246",

        "HOST": "aws-0-ap-northeast-1.pooler.supabase.com",

        "PORT": "6543",

        "CONN_MAX_AGE": 0,

        "OPTIONS": {
            "sslmode": "require",
            "connect_timeout": 10,
        },
    }
}


# ==================================================
# PASSWORD VALIDATION
# ==================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator",
    },
]


# ==================================================
# INTERNATIONALIZATION
# ==================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True
USE_TZ = True


# ==================================================
# STATIC FILES
# ==================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# ==================================================
# MEDIA FILES
# ==================================================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==================================================
# FILE UPLOAD LIMITS
# ==================================================

FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024


# ==================================================
# DEFAULT PRIMARY KEY
# ==================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
