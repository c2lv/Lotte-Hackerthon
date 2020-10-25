from django.db import models

# Create your models here.
class Post(models.Model):
    chef = models.CharField(max_length=50, null=False)
    menu = models.CharField(max_length=50, null=False)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
