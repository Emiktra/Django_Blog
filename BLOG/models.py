from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  profile_pic =models.ImageField(upload_to="profile_pics", default="profile_pics/default_profile.png", blank=True)
  date_joined = models.DateTimeField(auto_now_add=True)
  bio = models.TextField(max_length=2000, default="My bio")

  def __str__(self):
    return self.username

class Post(models.Model):
  title=models.CharField(max_length=75)
  content=models.TextField(max_length=10000)
  image=models.ImageField(upload_to="post_pics", blank=True, default="post_pics/default_post.png")
  post_date=models.DateTimeField(auto_now_add=True)
  views=models.IntegerField(default=0)
  likes=models.ManyToManyField(User)
  publisher = models.ForeignKey(User,on_delete=models.CASCADE, default=None, related_name="publisher")
  status=models.CharField(max_length=30, choices=(("1","Draft"),("2","Published")),default=("1","Draft"))
  category=models.CharField(max_length=30,choices=(("1","Software Engineering"),("2","Comedy"),("3","News"),("4","Informative")), default=("5","Personal"))
  def __str__(self):
    return self.title

class Comment(models.Model):
  publisher=models.ForeignKey(User,on_delete=models.CASCADE, default=None, related_name="comments")
  connected_post=models.ForeignKey(Post,on_delete=models.CASCADE, default=None, related_name="comments")
  content=models.TextField(max_length=2000)
  post_date=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.publisher