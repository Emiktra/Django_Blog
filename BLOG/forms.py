from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, Post, Comment

class UserCreationForm(UserCreationForm):
  class Meta:
    model= User
    fields=('username', 'email', 'password1', 'password2', 'profile_pic',)

class UserEditForm(forms.ModelForm):
  class Meta:
    model= User
    fields=('username', 'email','first_name', 'last_name', 'profile_pic', 'bio')

class PostBlogForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=('title', 'content', 'image','category', 'status')

class CommentForm(forms.ModelForm):
  class Meta:
    model=Comment
    fields=('content',)