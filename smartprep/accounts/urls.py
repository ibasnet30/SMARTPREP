from django.urls import path
from .import views

urlpatterns=[
    path('', views.homepage),

    path('contact/', views.contact),
    path('about/', views.about),
    path('LoginForm/', views.loginpage),
    path('RegisterForm/', views.Registerpage),





]