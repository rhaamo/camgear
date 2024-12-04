"""
Django settings for camgear project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

ROOT_DIR = environ.Path(__file__) - 2

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-1b^capn%f+)g=)d@l%w2!&d##*hy6jdn98-!ij)26-86qk*rdx",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=False)

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0', 'localhost']
ALLOWED_HOSTS = INTERNAL_IPS + env.list("ALLOWED_HOSTS", default=[])
print(f"Allowed hosts: {ALLOWED_HOSTS}")

# Application definition

INSTALLED_APPS = [
    # Override admin
    "admin_interface",
    "colorfield",
    # Django defaults
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Other
    "django_extensions",
    # Our apps
    "gear",
    "datas",
    "files",
    "serials",
    "repairlog",
    "frontend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "camgear.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "camgear.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = env("TZ", default="UTC")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Attachments

ITEM_ATTACHMENT_ALLOWED_PICTURES_TYPES = [
    "image/gif",
    "image/jpeg",
    "image/png",
]

ITEM_ATTACHMENT_ALLOWED_OTHER_TYPES = [
    "application/pdf",
    "application/xml",
    "image/svg+xml",
    "text/html",
    "text/plain",
    "text/xml",
    "application/msword",
    "application/vnd.ms-excel",
    "application/vnd.oasis.opendocument.text",
    "application/vnd.oasis.opendocument.spreadsheet",
    "application/zip",  # excel lol
]

# 50M (50*1024*1024)
FILE_UPLOAD_MAX_MEMORY_SIZE = env("FILE_UPLOAD_MAX_MEMORY_SIZE", default=50 * 1024 * 1024)
DATA_UPLOAD_MAX_MEMORY_SIZE = FILE_UPLOAD_MAX_MEMORY_SIZE

if env("PROXIFIED_WITH_SSL", default=True):
    # This ensures that Django will be able to detect a secure connection
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

ATTACHMENTS_UNATTACHED_PRUNE_DELAY = env.int("ATTACHMENTS_UNATTACHED_PRUNE_DELAY", default=3600 * 24)
FILE_UPLOAD_PERMISSIONS = 0o644
MEDIA_ROOT = env("MEDIA_ROOT", default=str(ROOT_DIR("uploads")))
STATIC_ROOT = env("STATIC_ROOT", default=str(ROOT_DIR("static")))

MEDIA_URL = env("MEDIA_URL", default="/media/")
STATIC_URL = env("STATIC_URL", default="/static/")
