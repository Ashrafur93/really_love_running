from . import views
from django.urls import path
from .views import ProfileDetailedView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('', views.ProfileDetailedView.as_view(), name='profile'),
    path('profile/', ProfileDetailedView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='delete_profile'),
]
