from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
# from .forms import *

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is not set")
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email not set")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    # user_id =  models.AutoField(primary_key= True, default=None)
    # username = None
    username = models.CharField(unique=True,max_length = 20, null = False)
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique=True, max_length = 200, null = True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Submission(models.Model):
    
    @staticmethod
    def get_status():
        STATUS = (
            ('Accepted', 'Accepted'),
            ('Failed', 'Failed'),
            )
        return STATUS
    user = models.ForeignKey(User, null=True, on_delete = models.SET_NULL)
    submission_id = models.IntegerField(null = True)
    date_submitted = models.DateTimeField(auto_now_add = True, null = True)
    submission_language = models.CharField(max_length = 20, null = True)
    status = models.CharField(max_length=30, null = True, choices=get_status())


class Snippet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
