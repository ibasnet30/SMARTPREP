from django.urls import path
from .import views

urlpatterns=[
    path('', views.homepage),
    path('LoginForm', views.loginpage)


]