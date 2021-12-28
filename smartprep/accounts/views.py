from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'accounts/homepage.html')

def contact(request):
    context = {
        'activate_contact': 'active',

    }
    return render(request, 'accounts/contact.html',context)

def about(request):
    context = {
        'activate_about': 'active',

    }
    return render(request, 'accounts/aboutus.html',context)

def loginpage(request):
    return render(request,'accounts/login.html')

def Registerpage(request):
    return render(request,'accounts/register.html')