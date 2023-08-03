from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about',views.about,name='about'),
    path('cycle',views.cycle,name='cycle'),
    path('news',views.newsv,name='news'),
    path('contact',views.contacts,name='contact'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
]