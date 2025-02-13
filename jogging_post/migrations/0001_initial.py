# Generated by Django 4.2.18 on 2025-02-13 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Jogging Event', max_length=100)),
                ('type', models.CharField(choices=[('Urban', 'Urban'), ('Trail', 'Trail'), ('Track', 'Track'), ('Canals', 'Canals'), ('Coffee', 'Coffee')], default='Urban', max_length=6)),
                ('distance', models.FloatField(default=0.0)),
                ('distance_unit', models.CharField(choices=[('KM', 'Kilometers'), ('MI', 'Miles')], default='KM', max_length=2)),
                ('day_and_time', models.DateTimeField(default=None)),
                ('location', models.CharField(default='Birmingham, City Centre, B1 1AA', max_length=100)),
                ('location_url', models.URLField(blank=True)),
                ('body', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
