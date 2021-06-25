from django.urls import path
from .views import GetUserFeedPost, AddNewPost
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',csrf_exempt(AddNewPost)),
    path('get/<int:pk>',GetUserFeedPost)
]