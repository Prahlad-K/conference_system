# Generated by Django 2.0.9 on 2018-10-23 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user_details',
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
