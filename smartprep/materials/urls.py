from django.urls import path

from materials import views
urlpatterns = [

   # path('home', views.content2),
    path('content/', views.content),
    path('courses/', views.courses),
    path('categories/', views.categories)
    # path('content/', views.content2)

]