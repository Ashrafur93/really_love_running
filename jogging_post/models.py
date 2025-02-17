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
    enabled = models.BooleanField(default=True)
    title = models.CharField(max_length=100, default='Jogging Event')
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Urban')
    distance = models.FloatField(default=0.0)
    distance_unit = models.CharField(max_length=2, choices=DISTANCE_CHOICES, default='KM')
    time = models.TimeField(default=None, null=True)
    day = models.CharField(choices=DAY_CHOICES, default='Monday')
    day_int = models.IntegerField(default=0)
    location_short = models.CharField(max_length=100, default='Birmingham')
    location = models.CharField(max_length=100, default='Birmingham, City Centre, B1 1AA')
    location_url = models.URLField(max_length=1000, blank=True)
    body = models.TextField()
    background_image = CloudinaryField('image', default='placeholder')
    icon = models.TextField(max_length=300, default='fa-solid fa-city')
    banner_image = CloudinaryField('image', default='placeholder')
    # partisipant_list = models.ManyToManyField('Profile', related_name='jogging_events', blank=True)

    def save(self, *args, **kwargs):
        day_mapping = {
            'Monday': 0,
            'Tuesday': 1,
            'Wednesday': 2,
            'Thursday': 3,
            'Friday': 4,
            'Saturday': 5,
            'Sunday': 6,
        }

        if self.type == 'Urban':
            self.icon = 'fa-solid fa-city'
        elif self.type == 'Trail':
            self.icon = 'fa-solid fa-tree'
        elif self.type == 'Track':
            self.icon = 'fa-solid fa-flag-checkered'
        elif self.type == 'Canals':
            self.icon = 'fa-solid fa-ship'
        elif self.type == 'Coffee':
            self.icon = 'fa-solid fa-mug-hot'

        if self.type == 'Urban':
            self.background_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739548545/wx8v7eobfqnybfqv1qe6.jpg'
            self.banner_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739554324/msatdulhap7usflyew1h.jpg'
        elif self.type == 'Trail':
            self.background_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739548560/wdet326lfb3kxhg7e4zi.jpg'
            self.banner_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739554879/noxbbt4p8rcbeucaw4ll.webp'
        elif self.type == 'Track':
            self.background_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739548567/bfxyszqdwht1yzgs4zqd.jpg'
            self.banner_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739554368/kp9wpvtezagqchlihbid.webp'
        elif self.type == 'Canals':
            self.background_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739548574/e3tjck3dxm5loyllyrqw.jpg'
            self.banner_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739554376/xdw41j4m7a4cq6xrfsbk.jpg'
        elif self.type == 'Coffee':
            self.background_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739548580/eiw4yycwosrmizpvovgl.jpg'
            self.banner_image = 'https://res.cloudinary.com/didwpm5uk/image/upload/v1739554383/utc1xbhssud4rr2vundk.webp'

        self.title = f"Jogging Event {self.type}"
        self.day_int = day_mapping.get(self.day, 0)  # Default to 0 if day is not found
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} | {self.location} | {self.day} | {self.time} | Enabled = {self.enabled}"

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['day_int', 'icon', 'title', 'slug']
        return []


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.body.replace('<p>', '').replace('</p>', '')[:30]} | {self.created_at}"
