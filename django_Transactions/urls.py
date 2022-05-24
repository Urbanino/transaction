"""django_Transactions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/transactions/', include('transactions.urls')),
]

# import os
# from django.conf import settings
# from celery import Celery
# from pathlib import Path
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# app = Celery('transactions')
#              # , broker_url = 'pyamqp://localhost:5672',
#              # result_backend = 'db+postgresql://admin:password@localhost:5433/django_transactions')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_Transactions.settings')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
# settings.configure()
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
#
