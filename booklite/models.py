from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    # genre = models.CharField(max_length=50)
    # description = models.TextField(max_length=None)
    published = models.DateField()
    publisher = models.CharField(max_length=50)
    # pagecount = models.IntegerField
    img_url = models.URLField

    def __str__(self):
        return self.title



