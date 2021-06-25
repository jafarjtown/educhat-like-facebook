from django.urls import path
from .views import SendMessage
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', csrf_exempt(SendMessage))
]