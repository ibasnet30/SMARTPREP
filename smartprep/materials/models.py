from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# categories table
class Categories(models.Model):
    category_Name=models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(1000)],
                                  null=True, max_length=1000)

    category_Description=models.TextField(validators=[MinLengthValidator(9), MaxLengthValidator(3000)],
                                  null=True, max_length=3000)
    category_Image=models.FileField(upload_to='static/uploaded_Files')
    def __str__(self):
        return self.category_Name


# course_Level table
class Levels(models.Model):
    course_Level=models.CharField(max_length=50)

# courses table
class Courses(models.Model):
    course_Name=models.CharField(max_length=1000)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    course_Description = models.TextField(validators=[MinLengthValidator(9), MaxLengthValidator(3000)],

                                            null=True, max_length=3000)
    course_Image = models.FileField(upload_to='static/uploaded_Files')
    course_Time=models.CharField(max_length=40, null=True)

    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.course_Name


# lecturers table
class Lectures(models.Model):
    lecture_Number=models.IntegerField(max_length=3, null=True)
    lecture_Name=models.CharField(max_length=3000)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lecture_content= models.TextField(validators=[MinLengthValidator(9), MaxLengthValidator(3000)],
                                            null=True, max_length=3000)
    def __str__(self):
        return self.lecture_Name




class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    content=models.TextField(max_length=250)
    created_Date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.content)
