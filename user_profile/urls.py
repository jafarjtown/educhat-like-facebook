from django.urls import path
from .views import FollowUnFollow
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
		path('follow-onfollow',csrf_exempt(FollowUnFollow))
]