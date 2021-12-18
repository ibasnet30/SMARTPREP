from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'accounts/homepage.html')

def loginpage(request):
    return render(request,'accounts/login.html')