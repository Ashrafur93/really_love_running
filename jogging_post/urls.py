from . import views
from django.urls import path
from .views import post_detail

urlpatterns = [
    # path('jogging_post/', views.PostList, name='jogging_post'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    # path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    # path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]