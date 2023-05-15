from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render


    # Add a related_name argument to avoid the reverse accessor clash with auth.User.groups
    # groups = models.ManyToManyField(Group, related_name='myapp_users')
    #
    # # Add a related_name argument to avoid the reverse accessor clash with auth.User.user_permissions
    # user_permissions = models.ManyToManyField(Permission, related_name='myapp_users')
    #
    # def __str__(self):
    #     return self.user


class Profile_img(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='profile_imgs')

    def __str__(self):
        return f'{self.user} Profile_img'

class Address(models.Model):
    user = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.user

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=70, unique=True)
    file = models.FileField(upload_to='uploads')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
