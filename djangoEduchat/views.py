from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework import viewsets, generics
from django.http import HttpResponse
# from resources.models import Book,Audio,Video
import django_filters.rest_framework
# from django.contrib.auth.models import User
from user_profile.models import User
from chat.models import Chat
from post.models import Post, Comment
from Image.models import File
from rest_framework.parsers import MultiPartParser, FormParser
from Activity.Notifications import Post_Notification
"""
User serializer
"""
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # exclude = ['password']
        fields = ['fullName','username','first_name','last_name','profile_pics','cover_pics','followers','following','id']
        depth = 1
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['username']
    search_fields = ['@title']

"""
Audio serialzer
"""


"""
Messages serializer
"""

class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

        depth = 3

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user__id']
    search_fields = ['@user__id']

    
    def get_context_data(self, **kwargs):
        context = super(ChatViewSet, self).get_context_data(**kwargs)
        return context
        
    def get_queryset(self):
        queryset = super(ChatViewSet, self).get_queryset()
        queryset = queryset # TODO
        return queryset

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post']
        # fields = '__all__'
        depth = 1
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


    
    def create(self, validated_data):
        user_id = validated_data.data.get('user_id')
        post_id = validated_data.data.get('post_id')
        text = validated_data.data.get('text')
        files = validated_data.data.get('files')
        user = User.objects.get(id=user_id)
        p = Post.objects.get(id=post_id)
        c = Comment.objects.create(post=p, user=user, text=text,files=files)
        c.save()
        return HttpResponse(p)




class PostSerializer(ModelSerializer):
    # user = UserSerializer()
    # comment_set = CommentSerializer()
    class Meta:
        model = Post
        fields = '__all__'

        depth = 2
    # def create(self, validated_data):
    #     print('here')
    #     return Post.objects.create(**validated_data)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-timestamp').select_related('user').prefetch_related('files')
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser,FormParser,)
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['user__id']
    # search_fields = ['@user__id']

    
    def get_context_data(self, **kwargs):
        context = super(PostViewSet, self).get_context_data(**kwargs)
        return context
        
    def get_queryset(self):
        queryset = super(PostViewSet, self).get_queryset()
        queryset = queryset # TODO
        return queryset
    
    def create(self, validated_data):
        user_id = validated_data.data.get('id')
        text = validated_data.data.get('text')
        files_raw = validated_data.data.get('files')
        user = User.objects.get(id=user_id)
        p = Post.objects.create(user=user, text=text)
        if files_raw:
            files = dict((validated_data.data).lists())['files']
            for img in files:
                file = File.objects.create(owner=user, file=img)
                file.save()
                p.files.add(file)
        Post_Notification(user=user,post=p).CreateNotification()
        p.save()
        return HttpResponse('nice')

