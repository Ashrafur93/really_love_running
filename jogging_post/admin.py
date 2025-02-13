from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'