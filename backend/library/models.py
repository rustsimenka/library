from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=256)


class Book(models.Model):
    name = models.CharField(max_length=256)

