from django.db import models

# Create your models here.

class File(models.Model):
    owner = models.ForeignKey('user_profile.User', related_name='pictures', on_delete=models.CASCADE)
    file = models.FileField()