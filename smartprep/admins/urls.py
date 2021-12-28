from django.urls import path

from admins import views

urlpatterns = [
    path('dashboard', views.admin_dashboard)

]