# Generated by Django 3.1.6 on 2021-06-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20210601_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='created_on',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='notes',
            name='last_updated',
            field=models.DateField(),
        ),
    ]