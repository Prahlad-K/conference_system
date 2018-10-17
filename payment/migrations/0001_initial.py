# Generated by Django 2.0.9 on 2018-10-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentDetails', models.CharField(max_length=200)),
                ('payment_date', models.DateTimeField(verbose_name='Date paid')),
            ],
        ),
    ]
