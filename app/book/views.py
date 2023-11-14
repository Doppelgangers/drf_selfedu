from rest_framework import generics
from .models import Book, Category
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Book.objects.all()

        return Book.objects.filter(pk=pk)

    @action(methods=["get"], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({"cats": cats.name})
