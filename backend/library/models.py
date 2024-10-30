from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=256)

class Book(models.Model):
    name = models.CharField(max_length=256)
    count_of_pages = models.IntegerField()
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)



