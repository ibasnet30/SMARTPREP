from django.urls import path, include

urlpatterns = [
    path('materials/', include('smartprep.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls'))

]
