# Generated by Django 4.2.18 on 2025-02-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogging_post', '0005_alter_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(default='Birmingham, City Centre, B1 1AA', max_length=100),
        ),
    ]
