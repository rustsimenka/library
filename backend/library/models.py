from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=256)

class Book(models.Model):
    name = models.CharField(max_length=256)
    pages = models.IntegerField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


