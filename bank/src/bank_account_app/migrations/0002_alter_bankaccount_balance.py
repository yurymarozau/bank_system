# Generated by Django 4.0.1 on 2022-02-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=21, verbose_name='Balance'),
        ),
    ]
