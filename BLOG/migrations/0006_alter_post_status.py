# Generated by Django 3.2.8 on 2021-10-31 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0005_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Draft', 'Published')], max_length=30),
        ),
    ]
