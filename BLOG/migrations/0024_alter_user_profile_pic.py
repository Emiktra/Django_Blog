# Generated by Django 3.2.8 on 2021-11-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0023_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile.jpg', upload_to='profile_pics'),
        ),
    ]