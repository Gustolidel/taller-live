# Generated by Django 3.1.3 on 2021-06-09 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apptaller', '0003_auto_20210609_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcionista',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
