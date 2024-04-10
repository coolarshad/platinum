from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2ob+qr3+fjhaww=kds0*__=-=rt=s+!lp)@sb4og&g3qaibna!"

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ["platinum-my.com","97.74.82.132"]
ALLOWED_HOSTS = []
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
