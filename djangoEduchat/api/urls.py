from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet,ChatViewSet,PostViewSet,CommentViewSet

router = routers.DefaultRouter()

# router.register('__books__', BookViewSet)
# router.register('__audio__', AudioViewSet)
router.register('__user__', UserViewSet)
router.register('__user_chat__',ChatViewSet)
router.register('__user_post__',PostViewSet)
router.register('__user_post_comment__',CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    
]