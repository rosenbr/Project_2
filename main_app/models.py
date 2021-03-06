from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    name = models.CharField(max_length=100)
    currentcity = models.CharField(max_length=500)
    join_date = models.DateField(default=date.today())
    image = models.CharField(max_length=500)
    # for user for login 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Posts(models.Model):

    title= models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    comments = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title
