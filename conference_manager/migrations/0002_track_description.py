# Generated by Django 2.0.9 on 2018-10-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]