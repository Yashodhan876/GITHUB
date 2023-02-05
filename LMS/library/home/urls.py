from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('adminlogin', views.handleadminLogin, name='handleadminLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('adminlogout', views.handleadminLogout, name='handleadminLogout'),
]