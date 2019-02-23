# Generated by Django 2.1.7 on 2019-02-23 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution_details',
            name='name',
        ),
        migrations.AddField(
            model_name='institution_details',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
