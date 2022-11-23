from django.urls import path,include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('haqimizda', views.about, name='about'),
    path('kurslar', views.courses , name='courses'),
    path('galereya', views.galery, name='galery'),
    path("ko'proq", views.more, name='more'),
    path("narxlar", views.prices, name='prices'),
    path("aloqa", views.contacts, name='conatct')
]