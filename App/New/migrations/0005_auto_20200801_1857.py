# Generated by Django 3.0.7 on 2020-08-01 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('New', '0004_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Owner',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
