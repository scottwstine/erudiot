from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    # genre = models.CharField(max_length=50)
    # description = models.TextField(max_length=None)
    published = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    # pagecount = models.IntegerField
    img_url = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='books')

    def __str__(self):
        return self.title



