# Generated by Django 4.0.1 on 2022-02-14 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account_app', '0003_alter_bankaccount_client'),
        ('client_app', '0005_alter_client_passport_number_and_more'),
        ('deposit_app', '0006_alter_deposittype_max_downpayment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositcontract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='deposit_contracts', to='client_app.client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='depositcontract',
            name='deposit_bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='deposit_contracts_deposit', to='bank_account_app.bankaccount', verbose_name='Deposit bank account'),
        ),
        migrations.AlterField(
            model_name='depositcontract',
            name='main_bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='deposit_contracts_main', to='bank_account_app.bankaccount', verbose_name='Main bank account'),
        ),
        migrations.AlterField(
            model_name='depositcontract',
            name='special_bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='deposit_contracts_special', to='bank_account_app.bankaccount', verbose_name='Special bank account'),
        ),
    ]
