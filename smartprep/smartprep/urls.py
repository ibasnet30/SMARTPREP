from django.urls import path, include
from django.contrib import  admin

urlpatterns = [
    path('materials/', include('materials.urls')),
    # path('admins/', include('admins.urls')),
    path('', include('accounts.urls')),
    path('quiz', include('quiz.urls')),
    path('admin', admin.site.urls)

]
