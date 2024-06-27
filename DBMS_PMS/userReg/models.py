
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    cnic = models.CharField(max_length=13, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    home_address = models.TextField()
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = [ 'first_name', 'last_name']