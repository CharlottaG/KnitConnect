# Generated by Django 5.0.4 on 2024-04-09 20:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0004_remove_pattern_updated_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pattern',
            name='status',
        ),
        migrations.AlterField(
            model_name='pattern',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]