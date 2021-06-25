from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    files = models.FileField(null=True, blank=True)

    def __str__(self):
    	return f'{self.user}----{self.id}----{self.timestamp}'

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	files = models.FileField(null=True, blank=True)

	def __str__(self):
		return f'{self.user}----{self.post.id}----{self.timestamp}'