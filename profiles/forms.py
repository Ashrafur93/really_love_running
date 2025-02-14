from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'name', 'birth_date', 'location', 'favourite_run', 'favourite_music', 'jogging_goals', 'bio']