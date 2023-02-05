from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.frontpage, name='frontpage'),
    path('userpage', views.userpage, name='userpage'),
    path('AllBooks',views.AllBooks, name='AllBooks'),
    path('category/<str:slug>',views.cat, name='cat'),
    path('search',views.search, name='search'),
    path('Apply/<str:slug>',views.Apply, name='Apply'),
]