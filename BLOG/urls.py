from django.urls import path
from .views import Userlogout, about, home, Userregister, Userlogin, profile, reset_password, edit_profile, create_post, post_detail, edit_post, delete_post
from django.contrib.auth import views

urlpatterns = [
  path("", home, name="home"),
  path("register/", Userregister, name="register"),
  path("login/", Userlogin, name="login"),
  path("logout/", Userlogout, name="logout"),
  path("profile/", profile, name="profile"),
  path("about/", about, name="about"),
  path('edit_profile/<int:id>/', edit_profile, name="edit_profile"),
  path('post_detail/<int:id>/', post_detail, name="post_detail"),
  path('create_post/', create_post, name="create_post"),
  path('delete_post/<int:id>', delete_post, name="delete_post"),
  path('edit_post/<int:id>', edit_post, name="edit_post"),

  # password reset
  path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='BLOG/password_reset_templates/password_reset_done.html'), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="BLOG/password_reset_templates/password_reset_confirm.html"), name='password_reset_confirm'),
  path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='BLOG/password_reset_templates/password_reset_complete.html'), name='password_reset_complete'),
  path('password_reset/', reset_password, name="password_reset"),
]