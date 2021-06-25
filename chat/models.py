from django.db import models

# Create your models here.
class Messages(models.Model):
    sender = models.ForeignKey('user_profile.User',null=True, on_delete=models.SET_NULL, related_name='sender')
    receiver = models.ForeignKey('user_profile.User',null=True, on_delete=models.SET_NULL, related_name='receiver')
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, blank=True, null=True)
    messages = models.ManyToManyField(Messages)