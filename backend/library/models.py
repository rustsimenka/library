from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=256)
    pages = models.IntegerField(null=False)

class Author(models.Model):
    name = models.CharField(max_length=256)