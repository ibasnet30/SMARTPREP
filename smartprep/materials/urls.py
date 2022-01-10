from django.urls import path

from materials import views
urlpatterns = [

   # path('home', views.content2),
    path('home/', views.home),
    path('courses/', views.course),
    path('get_course_category/<int:categories_id>', views.get_course_category)
    # path('content/', views.content2)

]