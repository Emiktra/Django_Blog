from django.contrib.auth import login
from django.urls import path
from .views import Userlogout, home, Userregister, Userlogin

#paths


urlpatterns = [
  path("", home, name="home"),
  path("register/", Userregister, name="register"),
  path("login/", Userlogin, name="login"),
  path("logout/", Userlogout, name="logout"),
]