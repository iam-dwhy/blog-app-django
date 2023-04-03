from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    content = models.TextField(null=True)
    


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # comment should be deleted once user is deleted
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE) # belong to blog
    day_made = models.DateTimeField()


