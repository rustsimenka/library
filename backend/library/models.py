from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=256)
    count_of_pages = models.IntegerField(null=True)


