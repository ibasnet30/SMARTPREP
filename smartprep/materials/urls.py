from django.urls import path
from .import views
from materials import views
urlpatterns = [

   # path('home', views.content2),
    path('home/', views.home),
    path('courses/', views.course),
    path('get_course_category/<int:categories_id>', views.get_course_category),
    # path('content/', views.content2),
    path('courseDetail/<int:courses_id>', views.courseDetail),
    path('', views.home,name='home'),



]