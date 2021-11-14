# Generated by Django 3.2.8 on 2021-11-14 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0036_auto_20211109_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publisher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]