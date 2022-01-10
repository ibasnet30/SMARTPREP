from django.db import models
from django.core import validators
from django.contrib.auth.models import User


class Contact(models.Model):
    firstname= models.CharField(max_length=50,null=True,validators=[validators.MinLengthValidator(2)])
    lastname=models.CharField(max_length=50, null=True, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message=models.TextField()
    def __str__(self):
        return self.firstname
