# Generated by Django 5.0.4 on 2024-04-09 13:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0002_alter_pattern_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='pattern_name', unique=True),
        ),
    ]
