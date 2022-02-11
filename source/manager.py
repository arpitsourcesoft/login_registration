from django.contrib.auth.base_user import BaseUserManager
from .models import models

class UserManager(BaseUserManager):

    def create_user(self,email,password=None):
        
        if not email:
            raise ValueError("Email is required")
        # if not username:
        #     raise ValueError("Username is required")
        user = self.model(
            email= self.normalize_email(email),
            # username= username,
            password = password
            
            )   
        
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,password=None):
        user = self.create_user(
            email= self.normalize_email(email),
            # username= username,
            password= password,            
            )  
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)
        return user
     




