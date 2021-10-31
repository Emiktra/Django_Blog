# Generated by Django 3.2.8 on 2021-10-31 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0014_post_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
