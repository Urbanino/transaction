from django_Transactions.celeryapp import app
from core.models import Transaction, BankAccount
from rest_framework import serializers
from django_Transactions.celeryapp import app
from celery import shared_task
from celery.contrib import rdb


@shared_task()
def make_transaction(data):
    print(data)
    rdb.set_trace()
    _from = BankAccount.objects.get(id = data['from'])
    _to = BankAccount.objects.get(id = data['to'])
    _amount = float(data['amount'])
    if _from.id == _to.id:
        msg = 'Нельзя перевести средства на тот же счёт'
        raise serializers.ValidationError(msg, code='validation')
    if _from.value - _amount < 0:
        msg = 'Недостаточно средств'
        raise serializers.ValidationError(msg, code='validation')
    _from.value -= _amount
    _to.value += _amount

    _from.save()
    _to.save()

    log_transaction = Transaction()
    log_transaction.fk_to = _to
    log_transaction.fk_from = _from
    log_transaction.amount = _amount
    log_transaction.status = 'Успешно'
    log_transaction.save()
    return log_transaction
