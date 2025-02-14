# Generated by Django 4.2.18 on 2025-02-14 16:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogging_post', '0004_post_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
