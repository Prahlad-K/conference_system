# Generated by Django 2.0.9 on 2018-10-30 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference_manager', '0006_track_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='report',
        ),
    ]
