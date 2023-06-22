import os
import sys
sys.path.append('/opt/bitnami/projects/UtilityWareHouse')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/UtilityWareHouse/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UtilityWareHouse.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
