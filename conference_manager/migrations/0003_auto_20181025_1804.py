# Generated by Django 2.0.9 on 2018-10-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_manager', '0002_track_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='report_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='track',
            name='report_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
