from django.urls import path
from .import views

urlpatterns=[
    path('', views.homepage),

    path('contact/', views.contact),
    path('about/', views.about),
    path('LoginForm/', views.loginpage),
    path('RegisterForm/', views.Registerpage),

    path('LoginForm', views.loginpage),
    path('register_page', views.register_user),

    path('login_page', views.login_page),
    path('logout', views.logout_user)



]