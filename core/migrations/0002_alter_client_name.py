# Generated by Django 4.0.4 on 2022-05-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Имя'),
        ),
    ]
