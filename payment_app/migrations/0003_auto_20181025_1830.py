# Generated by Django 2.1.2 on 2018-10-25 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0002_auto_20181025_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2018, 10, 25, 18, 30, 21, 965951), verbose_name='expiration date'),
        ),
    ]
