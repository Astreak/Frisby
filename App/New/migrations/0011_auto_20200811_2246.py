# Generated by Django 3.0.7 on 2020-08-11 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New', '0010_auto_20200811_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 11, 22, 46, 27, 74943), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 11, 22, 46, 27, 75939), verbose_name='Date'),
        ),
    ]
