from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserCreationForm


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

def Userlogin(request): # not done
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