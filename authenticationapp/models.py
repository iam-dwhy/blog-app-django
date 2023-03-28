from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    is_editor = models.BooleanField(default=False)
    profile_img = models.ImageField()





