from django.urls import path

from admins import views

urlpatterns = [
    path('dashboard', views.admin_dashboard),
    path('category_form/', views.categories_form),
    path('get_category/', views.get_category),




]