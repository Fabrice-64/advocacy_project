from .base import *

DEBUG = False

ALLOWED_HOSTS = ["localhost", '207.154.202.213', "www.advocacy-project.fr", "advocacy-project.fr"]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "admin@advocacy-project.fr"
