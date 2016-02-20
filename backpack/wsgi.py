"""
WSGI config for backpack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/Users/leguan/workspace/backpack/backpack/lib/python2.7/site-packages")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backpack.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
