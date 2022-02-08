from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from django.contrib import messages

from .models import Profile

from .forms import CreateUserForm, LoginForm, ContactForm, ProfileForm
from accounts.auth import unauthenticated_user, learner_only
from .models import Contact


def form(request):
    return render(request, 'accounts/form.html')

def homepage(request):
    return render(request, 'accounts/homepage.html')

def setting(request):
    return render(request, 'accounts/setting1.html')


def about(request):
    context = {
        'activate_about': 'active',

    }
    return render(request, 'accounts/aboutus.html',context)



# function for logout
@login_required
def logout_user(request):
    logout(request)
    return redirect('/login_page')


@unauthenticated_user
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email=user.email)
            messages.add_message(request, messages.SUCCESS, "User registered successfully")
            return redirect('/login')
        else:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR,'username already exists')
                return redirect('/RegisterForm/')
            messages.add_message(request, messages.ERROR, "Something went wrong")
            return render(request, 'accounts/register.html', {'form_user':form})

    context = {
        'form_user': CreateUserForm,
        'activate_register': 'active'
    }
    return render(request, 'accounts/register.html', context)



@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')


#
# @unauthenticated_user
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
                    return redirect('/lecturer/lecturerDashboard')

            else:
                messages.add_message(request, messages.ERROR, "Invalid credentials")
                return render(request, 'accounts/login.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html', context)




def contact(request):
    if request.method == "POST":
        if request.method == "POST":
            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                phone = request.POST.get('phone')
                message = request.POST.get('message')
                message_send = Contact.objects.create(firstname=firstname,
                                                      lastname=lastname,
                                                      phone=phone,
                                                      message=message,
                                                      status="Mark as read")
                if message_send:
                    messages.add_message(request, messages.SUCCESS, 'Your message has been sent')

                    return redirect("/contact")
            else:
                messages.add_message(request, messages.ERROR, 'Please try again')
                return render(request, 'accounts/contact.html', {'form_contact': form})
    context = {
        'activate_contact': 'active',
        'form_contact': ContactForm,

    }
    return render(request, 'accounts/contact.html', context)



@login_required
def profilee(request):
    # profile gives data from backend
    profile=request.user.profile

    if request.method=="POST":
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Profile Updated')
            return redirect('/profilee')
    context={
        'form':ProfileForm(instance=profile),
        'activate_profile':'activate'
    }
    return render(request,'accounts/profile.html',context)



# for password change
# function for changing password
@login_required
def password_change(request):
    if request.method=='POST':
        # new_password1 = request.POST.get('new_password1')
        # new_password2 = request.POST.get('new_password2')
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.add_message(request,messages.SUCCESS,"Password changed successfully!")
            return redirect('/password_change')
        else:
            # if User.objects.filter(new_password1=new_password1).exists():
            #     messages.add_message(request, messages.ERROR,'username already exists')
            #     return redirect('/RegisterForm/')
            messages.add_message(request,messages.ERROR, "Something went wrong!")
            return render(request,'accounts/password_change.html', {'password_change_form':form})
    context={
        'password_change_form':PasswordChangeForm(request.user),
    }
    return render(request,'accounts/password_change.html',context)