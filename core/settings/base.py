"""
Django settings for wf_website project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

import dj_database_url
from braintree import Configuration as BraintreeConfiguration
from braintree import Environment as BraintreeEnvironment
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

default_allowed_hosts = "127.0.0.1,localhost,westernfriend.ngrok.io"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", default_allowed_hosts).split(",")

default_csrf_trusted_origins = "http://127.0.0.1,https://127.0.0.1,http://localhost,https://localhost,https://westernfriend.ngrok.io"

CSRF_TRUSTED_ORIGINS = os.getenv(
    "DJANGO_CSRF_TRUSTED_ORIGINS", default_csrf_trusted_origins
).split(",")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECURE_REFERRER_POLICY = "strict-origin"

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

DEBUG = os.getenv("DEBUG", "False") == "True"

# Settings related to DigitalOcean Spaces
# Note: for now, we are using the AWS naming-convention from Boto3
USE_SPACES = os.getenv("USE_SPACES", "False") == "True"
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "sfo3")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_LOCATION = os.getenv("AWS_LOCATION", "static")
PUBLIC_MEDIA_LOCATION = os.getenv("PUBLIC_MEDIA_LOCATION", "media")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

AUTH_USER_MODEL = "accounts.User"

CART_SESSION_ID = "cart"

# Braintree settings
BRAINTREE_MERCHANT_ID = os.getenv("BRAINTREE_MERCHANT_ID")
BRAINTREE_PUBLIC_KEY = os.getenv("BRAINTREE_PUBLIC_KEY")
BRAINTREE_PRIVATE_KEY = os.getenv("BRAINTREE_PRIVATE_KEY")

BraintreeConfiguration.configure(
    BraintreeEnvironment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY,
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "accounts",
    "addresses",
    "cart",
    "community",
    "contact",
    "content_migration",
    "documents",
    "donations",
    "events",
    "facets",
    "forms",
    "home",
    "library",
    "memorials",
    "navigation",
    "news",
    "orders",
    "payment.apps.PaymentConfig",
    "search",
    "store",
    "subscription",
    "magazine",
    "blocks",
    "wf_pages",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "wagtail.contrib.styleguide",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "crispy_forms",
    "flatpickr",
    "storages",
    "wagtail_color_panel",
    "wagtailfontawesome",
    "wagtailmedia",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

X_FRAME_OPTIONS = "SAMEORIGIN"

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ]
        },
    }
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASE_URL = os.getenv("DATABASE_URL")

NOT_COLLECTING_STATICFILES = len(sys.argv) > 0 and sys.argv[1] != "collectstatic"

if DATABASE_URL:
    DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}
else:
    if NOT_COLLECTING_STATICFILES:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        }


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

if USE_SPACES:
    STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{ AWS_STORAGE_BUCKET_NAME }/{AWS_LOCATION}/"
    STATICFILES_STORAGE = "core.storage_backends.StaticStorage"

    MEDIA_URL = (
        f"{AWS_S3_ENDPOINT_URL}/{ AWS_STORAGE_BUCKET_NAME }/{PUBLIC_MEDIA_LOCATION}/"
    )
    DEFAULT_FILE_STORAGE = "core.storage_backends.MediaStorage"

    # Prevent setting URL querystring parameters
    # which are causing 403 errors on DigitalOcean Spaces
    AWS_QUERYSTRING_AUTH = False
else:
    STATIC_URL = "/static/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "Western Friend"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "http://example.com"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAILADMIN_BASE_URL = "/admin"
