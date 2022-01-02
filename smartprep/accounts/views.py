from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib import messages


from .forms import CreateUserForm, LoginForm
from accounts.auth import unauthenticated_user


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

# def loginpage(request):
#     return render(request,'accounts/login.html')

#
# def Registerpage(request):
#     return render(request,'accounts/register.html')

# function for logout
@login_required
def logout_user(request):
    logout(request)
    return redirect('/login_page')


@unauthenticated_user
def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.add_message(request, messages.SUCCESS, "User registered successfully")
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong")
            return render(request, 'accounts/register.html', {'form_user':form})

    context = {
        'form_user': CreateUserForm,
        'activate_register': 'active'
    }
    return render(request, 'accounts/register.html', context)



@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                if user.is_staff == 1 & user.is_superuser == 1:
                    login(request, user)
                    return redirect('/admins/dashboard')

                elif user.is_staff == 0 & user.is_superuser == 0:
                    login(request, user)
                    return redirect('/materials/home')

                elif not user.is_superuser == 0 & user.is_staff == 1:
                    login(request, user)
                    return redirect('/lecturer/lib_dashboard')

            else:
                messages.add_message(request, messages.ERROR, "Invalid data")
                return render(request, 'accounts/login.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')
