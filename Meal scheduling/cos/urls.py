from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('shedule',views.shedule,name='shedule'),
    path('shedulemeal',views.shedulemeal,name='shedulemeal'),
    path('home',views.home,name='home'),
    path('menucard',views.menucard,name='menucard'),
    path('info',views.info,name='info'),
    path('info1',views.info1,name='info1'),
    path('shedule1',views.shedule1,name='shedule1'),
    path('order',views.order,name='order'),
    path('just',views.just,name='just'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('menucard1',views.menucard1,name='menucard1'),
    path('adminportal',views.adminportal,name='adminportal'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('add',views.add,name="add"),
    path("gotoadd",views.gotoadd,name="gotoadd"),
    path("gotodelete",views.gotodelete,name="gotodelete"),
    path("deteteitem",views.deteteitem,name="deteteitem")
]