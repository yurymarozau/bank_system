# Generated by Django 4.0.1 on 2022-02-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit_app', '0004_depositcontract_special_bank_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositcontract',
            name='is_ended',
            field=models.BooleanField(default=False, verbose_name='Is deposit ended'),
        ),
    ]