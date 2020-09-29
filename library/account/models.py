from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, id_num, role, password=None):
        if not email:
            return ValueError("Users must have an email address")
        if not username:
            return ValueError("Users must have a username")
        if not first_name:
            return ValueError("Users must have a first name")
        if not last_name:
            return ValueError("Users must have a last name")
        if not id_num:
            return ValueError("Users must have an ID number")
        if not role:
            return ValueError("Users must have a role ")
        user = self.model(
                email=self.normalize_email(email),
                username = username,
                first_name = first_name,
                last_name = last_name,
                id_num = id_num,
                role = role,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, id_num, role , password):
        user = self.create_user(
                email               =self.normalize_email(email),
                username            = username,
                first_name          = first_name,
                last_name           = last_name,
                id_num              = id_num,
                role                = role,
                password            = password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):

    ROLES = [
        ('regular', 'Student/Teacher'),
        ('manager', 'Book Manager'),
        ('head', 'Administrator'),
    ]

    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name          = models.CharField(max_length=100, default=None)
    last_name           = models.CharField(max_length=100)
    username            = models.CharField(max_length=30, unique=True)
    id_num              = models.IntegerField(unique=True)
    date_joined         = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="date joined", auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    role                = models.CharField(max_length=200, choices=ROLES, default='regular')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name','id_num', 'role']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



# Create your models here.
