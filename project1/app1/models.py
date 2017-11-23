from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserModel(models.Model):
    user=models.OneToOneField(User)
class UserProfileModel(models.Model):
    profile_pic=models.ImageField(blank=True)
    website=models.URLField(blank=True)
