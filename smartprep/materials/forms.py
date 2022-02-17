from django import forms
from  django.forms import ModelForm
from .models import Categories, Courses, Lectures, Comments


class CategoriesForm(ModelForm):
    class Meta:
        model=Categories
        fields='__all__'

class CoursesForm(ModelForm):
    class Meta:
        model=Courses
        fields="__all__"
        exclude = ['user']


class LecturesForm(ModelForm):
    class Meta:
        model=Lectures
        fields = "__all__"


class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['content']





