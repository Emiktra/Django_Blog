from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  email = models.EmailField()
  username = models.CharField(max_length=30)
  profilw_pic =models.ImageField(upload_to="")