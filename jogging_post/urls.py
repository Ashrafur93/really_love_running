from . import views
from django.urls import path
from .views import post_detail
from profiles.views import ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    # path('<slug:slug>/edit_comment/<int:comment_id>', views.ProfileUpdateView, name='comment_edit'),
    # path('<slug:slug>/delete_comment/<int:comment_id>', views.ProfileDeleteView, name='comment_delete'),
]