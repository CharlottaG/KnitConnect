# Generated by Django 5.0.4 on 2024-04-09 18:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dehwhmatn/image/upload/v1712673845/placeholder_palitb', max_length=255, verbose_name='image'),
        ),
    ]
