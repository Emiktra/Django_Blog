# Generated by Django 3.2.8 on 2021-11-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0022_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default_profile.png', upload_to='profile_pics'),
        ),
    ]
