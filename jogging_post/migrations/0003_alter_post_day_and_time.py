# Generated by Django 4.2.18 on 2025-02-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogging_post', '0002_remove_post_day_remove_post_notifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='day_and_time',
            field=models.DateTimeField(default=None),
        ),
    ]
