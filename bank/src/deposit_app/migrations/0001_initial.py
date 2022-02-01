# Generated by Django 4.0.1 on 2022-02-01 19:45

import client_app.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_app', '0004_alter_client_monthly_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('percent', models.FloatField(verbose_name='Percent')),
                ('deposit_term', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Deposit term')),
                ('currency', models.CharField(choices=[('BYN', 'BYN'), ('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=5, verbose_name='Currency')),
                ('min_downpayment', models.DecimalField(decimal_places=2, max_digits=13, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Minimal downpayment')),
                ('max_downpayment', models.DecimalField(decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Maximum downpayment')),
                ('is_revocable', models.BooleanField(verbose_name='Is revocable')),
            ],
            options={
                'verbose_name': 'Deposit type',
                'verbose_name_plural': 'Deposit types',
                'ordering': ['-percent'],
            },
        ),
        migrations.CreateModel(
            name='DepositContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_at', models.DateField(validators=[client_app.validators.validate_date], verbose_name='Start date')),
                ('ends_at', models.DateField(validators=[client_app.validators.validate_date], verbose_name='End date')),
                ('deposit_amount', models.DecimalField(decimal_places=2, max_digits=13, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Deposit amount')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='contracts', to='client_app.client', verbose_name='Client')),
                ('deposit_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='contracts', to='deposit_app.deposittype', verbose_name='Deposit type')),
            ],
            options={
                'verbose_name': 'Deposit contract',
                'verbose_name_plural': 'Deposit contract',
                'ordering': ['starts_at'],
            },
        ),
    ]
