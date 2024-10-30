from rest_framework.viewsets import GenericViewSet
from library.models import Book
from library.serialisers import BookSerializer
from rest_framework import mixins


class BookViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer