from django.urls import path

from materials import views
urlpatterns = [

   # path('home', views.content2),
    path('content/', views.content),
    path('course/', views.course)
    # path('content/', views.content2)

]