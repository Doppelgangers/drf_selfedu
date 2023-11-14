from rest_framework import generics
from .models import Book, Category
from .permisions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

# class BookViewSet(viewsets.ModelViewSet):
#     # queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Book.objects.all()
#
#         return Book.objects.filter(pk=pk)
#
#     @action(methods=["get"], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({"cats": cats.name})


class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class BookDestroyAPI(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)
