from django.db import models
from django.core import validators
from django.contrib.auth.models import User


class Contact(models.Model):
    STATUS = (
        ('Mark as read', 'Seen'),

    )
    firstname = models.CharField(max_length=50, null=True, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=50, null=True, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, default='Mark as read')

    def __str__(self):
        return self.firstname




class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50,)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50, null=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    location=models.CharField(max_length=50, null=True)
    country=models.CharField(max_length=50, null=True)
    profile_pic=models.FileField(upload_to='static/profiles', default='static/images/user.png')
    created_date=models.DateTimeField(auto_now_add=True)
