# Generated by Django 2.0.3 on 2018-03-14 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature_request_app', '0004_auto_20180314_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature_requests',
            name='client_priority',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
