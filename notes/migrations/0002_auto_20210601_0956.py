# Generated by Django 3.1.6 on 2021-06-01 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='created_on',
            field=models.DateField(default=datetime.date(2021, 6, 1)),
        ),
        migrations.AddField(
            model_name='notes',
            name='last_updated',
            field=models.DateField(default=datetime.date(2021, 6, 1)),
        ),
    ]
