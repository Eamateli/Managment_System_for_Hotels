from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField

GENDER = (
    ("None","None")
    ("Woman","Woman"),
    ("Man","Man"),
    ("Other","Other"),
    ("Prefer not to answer","Prefer not to answer"),
)

class User(AbstractUser):
    username = models.CharField(max_length=500, unique=True)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default="None")
    
    otp = models.CharField(max_length=100, null=True, blank=True)
    

