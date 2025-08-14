"""
WSGI config for tuelinh_real_estate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuelinh_real_estate.settings')

application = get_wsgi_application()

app = application  # For compatibility with Vercel and other platforms that expect 'app' as the WSGI callable