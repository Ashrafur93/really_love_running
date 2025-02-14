from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('jogging_post/', views.PostList.as_view(), name='jogging_post'),
    path('<slug:slug>/', views.PostList, name='jogging_post'),
    # path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    # path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]