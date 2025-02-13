from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    
    def __str__(self):
        return self.title
    
@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    
    def __str__(self):
        return self.title