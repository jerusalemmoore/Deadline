from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class User(models.User):
#     first_name = User.firstname(blank=False)
class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(default="N/A")
