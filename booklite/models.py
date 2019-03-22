from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)    
    description = models.TextField(max_length=None)
    published = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    pagecount = models.IntegerField(null=True, blank=True, default=0)
    img_url = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='books')
    isbn = models.CharField(max_length=13)
    genres = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title

    def get_genrestring(self):
        genrestr = ''
        for genre in self.genres.all():
            genrestr += str(genre)
        return genrestr
            

