from . import views
from django.urls import path
from .views import gallery

urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('gallery/', gallery , name='gallery'),
    ]