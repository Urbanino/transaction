from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', unique=True)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    fk_client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    value = models.DecimalField(verbose_name='Баланс счета', decimal_places=2, max_digits=15)

    def __str__(self):
        return f'{self.fk_client}, {self.pk} - {self.value}'


class Transaction(models.Model):
    fk_from = models.ForeignKey(BankAccount, on_delete=models.CASCADE, verbose_name='От', related_name='sender')
    fk_to = models.ForeignKey(BankAccount, on_delete=models.CASCADE, verbose_name='Кому', related_name='receiver')
    amount = models.DecimalField(verbose_name='Cумма перевода', decimal_places=2, max_digits=15)
    status = models.CharField(max_length=50, verbose_name='Статус', default='Не прошел')

    def __str__(self):
        return f'От {self.fk_from} - {self.fk_to} - перевод: {self.amount}'
