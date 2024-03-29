
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("register/", views.register, name="register"),
    path('logout/', views.logout_view, name='logout'),
]
