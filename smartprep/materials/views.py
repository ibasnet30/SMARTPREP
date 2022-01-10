from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from accounts.auth import learner_only
from materials.filters import CourseFilter, CatFilter
from materials.models import Categories, Courses

@learner_only
def home(request):
    category=Categories.objects.all().order_by('-id')
    context={
        'category_material':category,
        'activate_home':'active'

    }

    return render(request, 'materials/content.html', context )

# for courses in course page
@learner_only
def course(request):
    courses=Courses.objects.all().order_by('course_Name')
    courses_filter = CourseFilter(request.GET, queryset=courses)
    courses_final = courses_filter.qs
    context={
        'course_material':courses_final,
        'user_course_filter':courses_filter,
        'activate_courses':'active'
    }

    return render(request, 'materials/courses.html', context )

#retrieving course according to category
@learner_only
def get_course_category(request,categories_id):
    category=Categories.objects.get(id=categories_id)
    context={
        'category':category
    }
    return render(request,'materials/get_course_category.html',context)

# recently added courses