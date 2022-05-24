from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('clients', views.ClientViewSet)
router.register('bank_accounts', views.BankAccountViewSet)
router.register('transfer', views.TransactionViewSet)

app_name = 'transactions'

urlpatterns = [
    path('', include(router.urls)),
]
