from django.urls import path

from .views import CommentListView

urlpatterns = [
    path('listing/', CommentListView.as_view(), name='comments-listing'),
]
