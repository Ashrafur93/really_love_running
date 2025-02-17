from django.contrib import admin
from .models import Profile, User
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(User, UserAdmin)
