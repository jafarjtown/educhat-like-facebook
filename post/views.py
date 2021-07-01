from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from user_profile.models import User
from .models import Post
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.views import PostSerializer
from Image.models import File
# Create your views here.
@api_view(['GET'])
def GetUserFeedPost(request, pk):
    user = User.objects.get(id=pk)
    userPost = Post.objects.filter(user=user)
    post = []
    from itertools import chain
    if len(user.following.all()) > 0:
        for x in user.following.all():
            post.append(x.id)  
        p = Post.objects.filter(user__id__in=post)     
        posts = list(chain(userPost,p))
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    serializer = PostSerializer(userPost, many=True)
    return Response(serializer.data)

def AddNewPost(request):
    print(request.body)
    # json_data = json.loads(request.body['files'])
    print(request.body['files'])
    # user = User.objects.get(id=json_data['id'])
    # text = json_data['text']
    # files = json_data['files'] 
    # print(files)
    # p = Post.objects.create(user=user,text=text)
    # for img in files:
    #     print(img)
    #     file = File.objects.create(file=img, owner=user)
    #     p.files.add(file)
    # p.save()
    return HttpResponse('post save')
