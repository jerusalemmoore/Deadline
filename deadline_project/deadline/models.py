from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class User(models.User):
#     first_name = User.firstname(blank=False)
class User(AbstractUser):
    password = models.CharField(max_length=255,)

    email = models.EmailField(max_length=254)
