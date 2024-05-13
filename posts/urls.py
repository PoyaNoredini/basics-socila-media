from django.urls import path

from .views import PostView ,PostListView

urlpatterns = [
    
    path('post/' , PostView.as_view()),
    path('post/<int:post_pk>/' , PostView.as_view()),
    path('postlist/' , PostListView.as_view()),
]
