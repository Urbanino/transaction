import os
import sys
from django.conf import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_Transactions.settings')

app = Celery('django_Transactions')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# settings.configure()



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


