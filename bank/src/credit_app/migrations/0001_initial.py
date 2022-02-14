# Generated by Django 4.0.1 on 2022-02-14 12:21

import base_app.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_app', '0005_alter_client_passport_number_and_more'),
        ('bank_account_app', '0003_alter_bankaccount_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('percent', models.FloatField(verbose_name='Percent')),
                ('credit_term', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Credit term')),
                ('currency', models.CharField(choices=[('BYN', 'BYN'), ('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=5, verbose_name='Currency')),
                ('min_downpayment', models.DecimalField(decimal_places=2, max_digits=21, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Minimal downpayment')),
                ('max_downpayment', models.DecimalField(decimal_places=2, max_digits=21, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Maximum downpayment')),
                ('is_annuity_payment', models.BooleanField(verbose_name='Is annuity payment')),
            ],
            options={
                'verbose_name': 'Credit type',
                'verbose_name_plural': 'Credit types',
                'ordering': ['percent'],
            },
        ),
        migrations.CreateModel(
            name='CreditContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_at', models.DateField(validators=[base_app.validators.validate_date_on_future], verbose_name='Start date')),
                ('ends_at', models.DateField(validators=[base_app.validators.validate_date_on_future], verbose_name='End date')),
                ('is_ended', models.BooleanField(default=False, verbose_name='Is credit ended')),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=21, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Credit amount')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='credit_contracts', to='client_app.client', verbose_name='Client')),
                ('credit_bank_account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='credit_contracts_credit', to='bank_account_app.bankaccount', verbose_name='Credit bank account')),
                ('credit_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='contracts', to='credit_app.credittype', verbose_name='Credit type')),
                ('main_bank_account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='credit_contracts_main', to='bank_account_app.bankaccount', verbose_name='Main bank account')),
                ('special_bank_account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='credit_contracts_special', to='bank_account_app.bankaccount', verbose_name='Special bank account')),
            ],
            options={
                'verbose_name': 'Credit contract',
                'verbose_name_plural': 'Credit contract',
                'ordering': ['starts_at'],
            },
        ),
    ]
