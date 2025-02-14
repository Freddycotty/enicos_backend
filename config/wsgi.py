"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys 

# Agrega la ruta del proyecto Django al PYTHONPATH
project_path = "/var/www/html/coresisprot.gsoft.app/sisprot-gsoft-backend"
sys.path.append(project_path)
sys.path.append("/var/www/html/coresisprot.gsoft.app/sisprot-gsoft-backend/config")

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
