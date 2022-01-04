from django.urls import path
from .import views

urlpatterns=[
    path('', views.homepage),
    path('course/',views.course),
    path('contact/', views.contact),
    path('about/', views.about),
    path('login/', views.login_page),
    path('RegisterForm/', views.register_user),
    path('logout', views.logout_user),





]