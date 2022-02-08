import os

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from accounts.auth import admin_only
from accounts.models import Contact

from materials.forms import CategoriesForm, CoursesForm, LecturesForm
from materials.models import Categories, Courses, Lectures


def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

def form(request):
    return render(request, 'admins/form.html')

def show_course(request):
    return render(request, 'admins/show_course.html')




# retrieving category form
def categories_form(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/admins/get_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add the category')
            return render(request, 'admins/category_form.html', {'form_category':form})
    context ={
        'form_category': CategoriesForm,

    }
    return render(request, 'admins/category_form.html', context)

#
# retrieving category
def get_category(request):
    category=Categories.objects.all().order_by('-id')

    context={
        'category':category,
        'activate_category_admin':'active'
    }
    return render(request, 'admins/get_category.html', context)



#deleting category
def delete_category(request, categories_id):
    category=Categories.objects.get(id=categories_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category Deleted!')
    return redirect('/admins/get_category/')

# update category
def category_update_form(request, categories_id):
    category = Categories.objects.get(id=categories_id)
    if request.method == "POST":
        if request.FILES.get('categories_Image'):
            os.remove(category.categories_Image.path)
        form = CategoriesForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated successfully')
            return redirect("/admins/get_category/")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update')
            return render(request, 'admins/category_update_form.html', {'form_category_update':category})
    context ={
        'form_category_update': CategoriesForm(instance=category),
        'activate_category':'active'
    }
    return render(request, 'admins/category_update_form.html', context)



# retrieving contact
def show_contact(request):
    contact=Contact.objects.filter(status='Mark as read').order_by('-created_date')

    context={
        'contact_admin':contact,
        'activate_contact':'active_admin'
    }
    return render(request, 'admins/show_contact.html', context)



def mark_as_read(request, contact_id):
    message=Contact.objects.get(id=contact_id)
    message.status="Seen"
    message.save()

    return redirect('/admins/show_contact')
