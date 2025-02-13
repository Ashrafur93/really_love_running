from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin

# class ProfileAdmin(admin.ModelAdmin):
#     filter_horizontal = ('jogging_events',)

@admin.register(Profile)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# admin.site.unregister(User)
# admin.site.register(User)
# admin.site.register(Profile, ProfileAdmin)