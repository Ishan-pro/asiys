import os
from whitenoise.django import DjangoWhitenoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asiys.settings')

application = get_wsgi_application()

application = DjangoWhiteNoise(application)
