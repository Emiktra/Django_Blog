# Generated by Django 3.2.8 on 2021-10-31 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0019_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('1', 'Draft'), ('2', 'Published')], default=('3', 'Drafto'), max_length=30),
        ),
    ]
