# Generated by Django 2.0.9 on 2018-10-22 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='id',
            new_name='role',
        ),
    ]