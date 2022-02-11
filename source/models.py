from multiprocessing.sharedctypes import Value
from operator import truediv
from pyexpat import model
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from . import manager
from django.contrib.auth.models import PermissionsMixin
from source.manager import UserManager


# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    
    first_name  = models.CharField(max_length=110)
    last_name   = models.CharField(max_length=100)
    username    = models.CharField(max_length=255)
    email       = models.EmailField(verbose_name='email',max_length=60,unique=True)
    mobile      = models.CharField(max_length=14)
    password    = models.CharField(max_length=40)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    is_staff    = models.BooleanField(default= False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []


    def __str__(self):
        return self.email

    def has_perm(self, perm,obj=None):
        return self.is_admin
    
    def has_module_perm(self, app_label):
        return True





