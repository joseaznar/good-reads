from django.db import models
from modules.Books.models import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):

        if not email:
            raise ValueError('El email debe ser obligatorio')
        email = self.normalize_email(email)

        user = self.model(email=email,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, True, True, **extra_fields)

GENDER = (
    ("M", "Masculino"),
    ("F", "Femenino"),
)


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    # unique, no se van a repetir
    id = models.AutoField(primary_key=True, unique=True)

    nombre = models.CharField(max_length=40)
    last_name = models.CharField(max_length=25)
    celphone = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=50)
    gender = models.CharField(max_length=16, choices=GENDER)
    library = models.ManyToManyField(Book)

    # intermediario entre trans de cada modelo, object managaer de cada modelo
    objects = UserManager()

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.nombre

    def __str__(self):
        return self.nombre
