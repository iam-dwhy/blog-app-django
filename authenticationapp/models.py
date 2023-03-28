from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser): 
    is_editor = models.BooleanField(default=False)
    profile_img = models.ImageField()
    about = models.TextField(null=True)



