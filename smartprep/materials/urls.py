from django.urls import path

from materials import views

urlpatterns = [
    path('home', views.home)

]