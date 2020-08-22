# Generated by Django 3.0.7 on 2020-08-12 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New', '0016_auto_20200812_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 13, 46, 54, 47042), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='music',
            name='urls',
            field=models.URLField(default='https://www.google.com'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 13, 46, 54, 48039), verbose_name='Date'),
        ),
    ]