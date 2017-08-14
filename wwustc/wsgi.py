"""
WSGI config for wwustc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/wwustc')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wwustc.settings")

application = get_wsgi_application()
