from django.contrib import admin
from .models import Profile, CustomUser
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin

# class ProfileAdmin(admin.ModelAdmin):
#     filter_horizontal = ('jogging_events',)


@admin.register(Profile)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(CustomUser, UserAdmin)
# admin.site.register(Profile)
# admin.site.unregister(User)
