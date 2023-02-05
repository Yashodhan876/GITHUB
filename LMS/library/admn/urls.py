from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('AdmnUser', views.AdmnUser, name='AdmnUser'),
    path('Records', views.Records, name='Records'),
    path('AdmnBooks', views.AdmnBooks, name='AdmnBooks'),
    path('AddBook', views.AddBook, name='AddBook'),
    path('added', views.added, name='added'),
    path('Sanction/<str:slug>', views.Sanction, name='Sanction'),
    path('Reject/<str:slug>', views.Reject, name='Reject'),
    path('Return/<str:slug>', views.Return, name='Return'),
    path('delete/<str:slug>', views.delete, name='delete'),
    
]