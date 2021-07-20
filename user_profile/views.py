from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import User
# Create your views here.


def FollowUnFollow(request):
	json_load = json.loads(request.body)
	sender_id = json_load['sender_id']
	receiver_id = json_load['receiver_id']
	user_1 = User.objects.get(id=sender_id)
	user_2 = User.objects.get(id=receiver_id)
	if user_2 in user_1.following.all():
		user_1.following.remove(user_2)
		user_2.followers.remove(user_1)
	else:
		user_1.following.add(user_2)
		user_2.followers.add(user_1)
	return HttpResponse(f'{sender_id}-{receiver_id}')

def HomeView(request):
	return render(request, 'profile/profile.html')