from rest_framework import viewsets
from library.models import Book
from library.serialisers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer