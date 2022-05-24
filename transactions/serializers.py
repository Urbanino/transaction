from rest_framework import serializers

from core.models import Client, BankAccount, Transaction


class ClientSerializer(serializers.ModelSerializer):
    """Сериалайзер для объектов клиент"""

    class Meta:
        model = Client
        fields = ('id', 'name')
        read_only_fields = ('id',)


class BankAccountSerializer(serializers.ModelSerializer):
    """Сериалайзер для объектов счетов"""

    class Meta:
        model = BankAccount
        fields = ('id', 'value', 'fk_client')
        read_only_fields = ('id',)


class TransactionSerializer(serializers.ModelSerializer):
    """Сериалайзер для объектов транзакций"""

    class Meta:
        model = Transaction
        fields = ('id', 'fk_from', 'fk_to', 'amount')
        read_only_fields = ('id',)
