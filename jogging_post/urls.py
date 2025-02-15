from . import views
from django.urls import path
from .views import post_detail

urlpatterns = [
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    # path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),  # noqa for flake8
    # path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),  # noqa for flake8
]
