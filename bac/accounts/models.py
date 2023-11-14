from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to='images/user/',
        null=True,
        blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['last_name', 'first_name']
    