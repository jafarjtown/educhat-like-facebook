from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet,ChatViewSet,PostViewSet,CommentViewSet

router = routers.DefaultRouter()

# router.register('__books__', BookViewSet)
# router.register('__audio__', AudioViewSet)
router.register('user', UserViewSet)
router.register('chatbox',ChatViewSet)
router.register('post',PostViewSet)
router.register('comment',CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]