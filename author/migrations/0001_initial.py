# Generated by Django 2.1.2 on 2018-10-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('gist', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('LAB', 'labor'), ('CAR', 'cars'), ('TRU', 'trucks'), ('WRI', 'writing')], max_length=3)),
                ('location', models.CharField(choices=[('BRO', 'Bronx'), ('BRK', 'Brooklyn'), ('QNS', 'Queens'), ('MAN', 'Manhattan'), ('STN', 'Staten Island')], max_length=3)),
                ('description', models.TextField(max_length=300)),
                ('expire', models.DateField()),
            ],
        ),
    ]
