from django.db import models

# Create your models here.

class PostNotification(models.Model):
    user = models.ForeignKey('user_profile.User', related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    post = models.ForeignKey('post.Post', on_delete=models.SET_NULL, null=True)
