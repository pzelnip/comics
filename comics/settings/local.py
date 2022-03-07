# pylint: disable=wildcard-import,unused-wildcard-import
from .prod import *

DEBUG = True

SECRET_KEY = "1l2k3jlkfadsjlkfdsaj"

DJANGO_ADMIN_PASSWORD = "admin"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
