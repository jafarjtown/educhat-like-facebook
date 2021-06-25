from django.shortcuts import render
from django.http import HttpResponse
from user_profile.models import User
from .models import Chat, Messages
import json
# Create your views here.

def SendMessage(request):
	json_data = json.loads(request.body)
	receiver_id = json_data['receiver_id']
	sender_id = json_data['sender_id']
	text_message = json_data['text']
	receiver = User.objects.get(id=receiver_id)
	sender = User.objects.get(id=sender_id)

	# Creating Message
	message = Messages.objects.create(sender=sender,receiver=receiver,text=text_message)
	message.save()

	# Geting users ChatBox
	try:
		sender_chat = Chat.objects.get(user=sender)
	except:
		sender_chat = Chat.objects.create(user=sender)
	try:
		receiver_chat = Chat.objects.get(user=receiver)
	except:
		receiver_chat = Chat.objects.create(user=receiver)
	
	# Sending messages to each user chatbox
	sender_chat.messages.add(message)
	receiver_chat.messages.add(message)


	print(receiver.age)
	return HttpResponse('message received')