from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile', blank=True, null=True)
    user_type = models.CharField(
        max_length=7,
        choices=[('DOCTOR', 'DOCTOR'), ('PATIENT', 'PATIENT')], null=True
    )