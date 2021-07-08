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

def LikeComment(request):
    print(request.body)
    json_load = json.loads(request.body)
    post_id = json_load['post_id']
    user_id = json_load['user_id']
    user = User.objects.get(id=user_id)
    post = Post.objects.get(id=post_id)

    if user in post.likes.all():
        post.likes.remove(user)
        return HttpResponse(f'post dislike')
    else:
        post.likes.add(user)
        return HttpResponse(f'post like')
    print(f'{post_id} {user_id}')
    return HttpResponse(request.body)
