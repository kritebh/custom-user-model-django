from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,password,**other_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not username:
            raise ValueError(_("Users must have an unique username"))
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
    
    def create_superuser(self,email,username,first_name,password,**other_fields):
            other_fields.setdefault('is_staff',True)
            other_fields.setdefault('is_superuser',True)
            other_fields.setdefault('is_active',True)
            if other_fields.get('is_staff') is not True:
                raise ValueError('is_staff is set to False')
            if other_fields.get('is_superuser') is not True:
                raise ValueError('is_superuser is set to False')
            return self.create_user(email,username,first_name,password,**other_fields)

class Account(AbstractBaseUser,PermissionsMixin):
    email         = models.EmailField(_('email address'),max_length=60,unique=True)
    username      = models.CharField(max_length=30,unique=True)
    first_name    = models.CharField(max_length=30,blank=True)
    last_name     = models.CharField(max_length=30,blank=True)
    date_of_birth = models.DateField(verbose_name='date of birth',null=True,blank=True)
    city          = models.CharField(max_length=50,blank=True)
    date_joined   = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']

    def __str__(self):
        return self.email