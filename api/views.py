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
from rest_framework.parsers import MultiPartParser, FormParser
"""
User serializer
"""
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        depth = 2
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['username']
    search_fields = ['@title']

"""
Audio serialzer
"""

# class AudioSerializer(ModelSerializer):
#     class Meta:
#         model = Audio
#         fields = '__all__'

# class AudioViewSet(viewsets.ModelViewSet):
#     queryset = Audio.objects.all()
#     serializer_class = AudioSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filterset_fields = ['title']
#     search_fields = ['@title']

# """
# book serializer
# """
# # books
# class BookSerializer(ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

    
#     def get_context_data(self, **kwargs):
#         context = super(BookViewSet, self).get_context_data(**kwargs)
#         return context
        
#     def get_queryset(self):
#         queryset = super(BookViewSet, self).get_queryset()
#         queryset = queryset # TODO
#         return queryset




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
        depth = 2
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
    user = UserSerializer()
    # comment_set = CommentSerializer()
    class Meta:
        model = Post
        fields = ['id','user','text','timestamp','files','comment_set']
        depth = 2
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-timestamp')
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser,FormParser)
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
        files = validated_data.data.get('files')
        user = User.objects.get(id=user_id)
        p = Post.objects.create(user=user,text=text,files=files)
        p.save()
        return HttpResponse(p)
