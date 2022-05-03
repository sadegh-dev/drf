from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager

class User(AbstractBaseUser):
    email =        models.EmailField(max_length=254, unique=True)
    full_name =    models.CharField(max_length=200)
    is_admin =     models.BooleanField(default=False)
    is_active =    models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]
    objects = MyUserManager()

    def __str__(self):
        return f'{self.email} - {self.full_name}'
    
    def has_perm(self, perm, obj=None):
        pass

    def has_module_perms(self, app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin




