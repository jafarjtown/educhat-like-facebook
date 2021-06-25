from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'

class User(AbstractUser):
    age = models.DateField(auto_now=True, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    avatar = models.ImageField(blank=True)
    cover = models.ImageField(blank=True)
    bio = models.TextField()
    # school = models.OneToOneField('school.School', blank=True, null=True, on_delete=models.SET_NULL, related_name='school')
    followers = models.ManyToManyField('User', related_name='user_followers', blank = True,)
    following = models.ManyToManyField('User', related_name='user_followings', blank = True,)
    address = models.OneToOneField('Address',on_delete=models.SET_NULL, null=True,blank=True)

class Address(models.Model):
    Country = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    providence = models.CharField(max_length=100)
    town = models.CharField(max_length=20)