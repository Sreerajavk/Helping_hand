# Generated by Django 2.1.7 on 2019-02-23 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_auto_20190223_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
