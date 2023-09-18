# wsgi.py
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add your project's root directory to the Python path
sys.path.append('/home/greymatter/greymatter-store/app')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greymatter.settings')
application = get_wsgi_application()

