from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post, Comment)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

    def __str__(self):
        return self.title
