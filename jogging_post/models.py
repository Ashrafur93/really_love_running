from django.db import models
from django.conf import settings
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

DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]


class Post(models.Model):
    title = models.CharField(max_length=100, default='Jogging Event')
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Urban')  # noqa for flake8
    distance = models.FloatField(default=0.0)
    distance_unit = models.CharField(max_length=2, choices=DISTANCE_CHOICES, default='KM')  # noqa for flake8
    time = models.TimeField(default=None, null=True)
    day = models.CharField(choices=DAY_CHOICES, default='Monday')
    location_short = models.CharField(max_length=100, default='Birmingham')
    location = models.CharField(max_length=100, default='Birmingham, City Centre, B1 1AA')  # noqa for flake8
    location_url = models.URLField(max_length=200, blank=True, default='https://maps.app.goo.gl/j4xrUjyJCYmN6guS9')  # noqa for flake8
    body = models.TextField()
    background_image = CloudinaryField('image', default='placeholder')
    icon = models.TextField(max_length=300, default='fa-solid fa-city')
    banner_image = CloudinaryField('image', default='placeholder')
    # partisipant_list = models.ManyToManyField('Profile', related_name='jogging_events', blank=True)  # noqa for flake8

    def __str__(self):
        return f"{self.title} | {self.location} | {self.day} | {self.time}"


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # noqa for flake8
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.body.replace('<p>', '').replace('</p>', '')[:30]} | {self.created_at}"  # noqa for flake8
