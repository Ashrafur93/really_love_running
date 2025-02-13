from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField

TYPE_CHOICES = [
        ('Urban', 'Urban'),
        ('Trail', 'Trail'),
        ('Track', 'Track'),
        ('Canals', 'Canals'),
        ('Coffee', 'Coffee'),
    ]

DISTANCE_CHOICES = [
        ('KM', 'Kilometers'),
        ('MI', 'Miles'),
    ]


class Post(models.Model):
    title = models.CharField(max_length=100, default='Jogging Event')
    # slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Urban')
    distance = models.FloatField(default=0.0)
    distance_unit = models.CharField(max_length=2, choices=DISTANCE_CHOICES, default='KM')
    day_and_time = models.DateTimeField(default=None)
    location = models.CharField(max_length=100, default='Birmingham, City Centre, B1 1AA')
    location_url = models.URLField(max_length=200, blank=True)
    body = models.TextField(max_length=300)
    # partisipant_list = models.ManyToManyField('Profile', related_name='jogging_events', blank=True)

    def __str__(self):
        return f"{self.title} | {self.location} | {self.day_and_time}"


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.body.replace('<p>', '').replace('</p>', '')[:30]} | {self.created_at}"
