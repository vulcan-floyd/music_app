from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.LogIn.as_view(), name='login'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('logout', views.Logout, name='logout'),
]