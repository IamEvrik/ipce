"""
WSGI config for ipce project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipce.settings')

application = get_wsgi_application()
