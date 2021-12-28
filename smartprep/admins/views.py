from django.shortcuts import render

# Create your views here.
from accounts.auth import admin_only


@admin_only
def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')