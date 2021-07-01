

from .models import PostNotification
class Post_Notification:
    def __init__(self,user,post):
        self.user = user
        self.post = post
    
    def CreateNotification(self):
        for user in self.user.followers.all():
            notification = PostNotification.objects.create(user=user, post=self.post, message=f'Dear {user.username}, your friend {self.user.username} have a new status...')
            notification.save()