from rest_framework.viewsets import ModelViewSet
from library.models import Book
from library.serialisers import BookSerializer
from rest_framework import mixins


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()

    serializer_class = BookSerializer