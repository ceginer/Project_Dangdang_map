from django.urls import path 

from . import views

app_name = "dang"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('logout/', views.logout, name='logout'),
]