from rest_framework import viewsets, mixins

from core.models import Client, BankAccount, Transaction

from . import serializers

from .tasks import make_transaction
# from celery import shared_task






class ClientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Управление данными клиентов в базе данных"""
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer


class BankAccountViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Управление данными клиентов в базе данных"""
    queryset = BankAccount.objects.all()
    serializer_class = serializers.BankAccountSerializer


class TransactionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Управление транзакциями клиентов в базе данных"""
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

    def perform_create(self, serializer):
        """Создание новой транзакции"""

        result = make_transaction.delay(serializer.data)
        return result