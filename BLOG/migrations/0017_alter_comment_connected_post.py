# Generated by Django 3.2.8 on 2021-10-31 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0016_auto_20211031_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='connected_post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='BLOG.post'),
        ),
    ]