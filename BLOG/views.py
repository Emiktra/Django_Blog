from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.http.response import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import UserCreationForm, UserEditForm, PostBlogForm, CommentForm
from django.db.models.query_utils import Q
from .models import User, Post, Comment
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages


# Create your views here.
def home(request):
  posts=Post.objects.all().filter(status="2")
  context={ "posts":posts }
  if not request.user.is_anonymous:
    drafts=Post.objects.all().filter(publisher=request.user).filter(status="1")
    context["drafts"]=drafts
  return render(request, "BLOG/home.html", context)

def Userregister(request):
  form=UserCreationForm()
  if request.method == "POST":
    form = UserCreationForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password1"]
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect("home")
  
  context={
    "form_user":form,
  }
  return render(request, 'BLOG/register.html', context)

def Userlogin(request):
  form =AuthenticationForm()
  if request.method == "POST":
    form=AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      if user:
        login(request, user)
        return redirect("home")
  return render(request, 'BLOG/login.html', context={"form":form})

def Userlogout(request):
  logout(request)
  return redirect('home')

def profile(request):
  data={
    "user": request.user
  }
  return render(request, 'BLOG/profile.html', context=data)

def about(request):
  return render(request, 'BLOG/about.html',)

def reset_password(request):
  form=PasswordResetForm(request.POST)
  if request.method == "POST":
    form=PasswordResetForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data['email']
      users = User.objects.filter((Q(email=data)))
      if users.exists():
        for user in users:
          subject = "Password Reset Requested"
          email_template = "BLOG/password_reset_templates/password_reset_email.txt"
          c={
            "email":user.email,
					  'domain':'127.0.0.1:8000',
					  'site_name': 'Djangalactic Blog',
					  "uid": urlsafe_base64_encode(force_bytes(user.pk)),
					  "user": user,
					  'token': default_token_generator.make_token(user),
					  'protocol': 'http',
          }
          email=render_to_string(email_template, c)
          try:
            send_mail(subject, email, "DjangalacticTeam@gmail.com", [user.email],fail_silently=False)
          except BadHeaderError:
            return HttpResponse('Invalid header found')
          messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
          return redirect("done/")
      else:
        messages.error(request, "This email doesn't exist")
  context ={ "form":form }
  return render(request, 'BLOG/password_reset_templates/password_reset.html',context)

def edit_profile(request, id):
  user=User.objects.get(id=request.user.id)
  form = UserEditForm(instance=user)
  if request.method == "POST":
    form = UserEditForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
      form.save()
      return redirect("profile")
  context={
    "form":form,
  }
  return render(request, "BLOG/edit_profile.html", context)

def create_post(request):
  form=PostBlogForm()
  if request.method=="POST":
    form = PostBlogForm(request.POST, request.FILES)
    if form.is_valid():
      post=form.save(commit=False)
      post.publisher=request.user
      post.save()
      return redirect("home")
  context={
    "form":form,
  }
  return render(request, 'BLOG/create_post.html', context)

def post_detail(request, id):
  form=CommentForm()
  post=Post.objects.get(id=id)

  #increases view count
  if request.method=="GET":
    post.views=post.views+1
    post.save()
  #handles comments
  if request.method=="POST" and 'commentBtn' in request.POST:
    form=CommentForm(request.POST)
    if form.is_valid():
      comment=form.save(commit=False)
      comment.connected_post=post
      comment.publisher=request.user
      comment.save()
  #likes
  if request.method=="POST" and 'likeBtn' in request.POST:
    try:
      post.likes.get(id=request.user.id) # user in database?
      post.likes.remove(request.user) # remove user
    except:
      post.likes.add(request.user) # else add user to likes list

  context={
    "post":post,
    "form":form,
  }
  return render(request,'BLOG/post_detail.html', context)

def delete_post(request,id):
  post=Post.objects.get(id=id)
  if request.method == "POST":
    post.delete()
    return redirect('home')
  context={
    "post":post,
  }
  return render(request, "BLOG/delete_post.html",context)

def edit_post(request,id):
  post=Post.objects.get(id=id)
  form=PostBlogForm(instance=post)
  if request.method=="POST":
    form=PostBlogForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return redirect(f"/post_detail/{id}")
  context={
    "form":form,
    "post":post,
  }
  return render(request, "BLOG/edit_post.html",context)