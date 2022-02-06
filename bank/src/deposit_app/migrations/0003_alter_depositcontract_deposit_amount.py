# Generated by Django 4.0.1 on 2022-02-06 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit_app', '0002_depositcontract_deposit_bank_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositcontract',
            name='deposit_amount',
            field=models.DecimalField(decimal_places=2, max_digits=21, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Deposit amount'),
        ),
    ]
