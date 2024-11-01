from django.core.validators import MinLengthValidator
from django.db import models


class ExplicitModel(models.Model):
    class Meta:
        abstract = True
    objects: models.Manager


class Author(ExplicitModel):
    name = models.CharField(max_length=256)


class Book(ExplicitModel):
    name = models.CharField(max_length=256, validators=[MinLengthValidator(4)])
    pages = models.IntegerField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
