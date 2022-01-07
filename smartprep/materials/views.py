from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from accounts.auth import learner_only
from materials.filters import CourseFilter, CatFilter
from materials.models import Categories, Courses



def content(request):
    category=Categories.objects.all().order_by('-id')
    context={
        'category_material':category,

    }

    return render(request, 'materials/content.html', context )



def courses(request):
    course=Courses.objects.all().order_by('-id')
    context={
        'course_material':course
    }

    return render(request, 'materials/courses.html', context )


def categories(request):
    category=Categories.objects.all().order_by('-id')
    context={
        'category_material':category,

    }

    return render(request, 'materials/categories.html', context )
