# Generated by Django 2.0.9 on 2018-10-25 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0004_merge_20181025_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2018, 10, 25, 19, 3, 31, 651097), verbose_name='expiration date'),
        ),
    ]