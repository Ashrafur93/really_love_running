from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProfileDetailedView.as_view(), name='profile'),
]