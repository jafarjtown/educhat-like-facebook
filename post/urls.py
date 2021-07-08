from django.urls import path
from .views import GetUserFeedPost, LikeComment
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('like',csrf_exempt(LikeComment)),
    path('get/<int:pk>',GetUserFeedPost)
]