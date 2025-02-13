from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from posts.models import Post

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # role = models.CharField(max_length=100, blank=True)
    profile_image = CloudinaryField('image', default='placeholder')
    name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    favourite_run = models.CharField(max_length=100, blank=True)
    favourite_music = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    jogging_goals = models.CharField(max_length=100, blank=True)
    # jogging_events = models.ManyToManyField(Post, related_name='purchased_games', blank=True)

    

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.profile_image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_image.path)