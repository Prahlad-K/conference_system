# Generated by Django 2.0.9 on 2018-11-21 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_customuser_validated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
