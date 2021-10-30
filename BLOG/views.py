from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.http.response import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import UserCreationForm
from django.db.models.query_utils import Q
from .models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages


# Create your views here.
def home(request):
  return render(request, "BLOG/home.html")

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
    "data": request.user
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
      messages.error(request, 'An invalid email has been entered.')
  context ={
    "form":form
  }
  return render(request, 'BLOG/password_reset_templates/password_reset.html',context)