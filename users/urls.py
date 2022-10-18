from django import views
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserLogin.as_view(), name="user-login"),
    path('registration', views.UserRegistration.as_view(), name="user-registration"),
]