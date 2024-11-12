from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('artist', 'Artist'),
        ('manager', 'Manager'),
        ('consumer', 'Consumer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
