from django.shortcuts import render
from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer


# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookAPIView(APIView):

    def get(self, request):
        lst = Book.objects.all()
        return Response({"books": BookSerializer(lst, many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_post = Book.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            category_id=request.data["category_id"]
        )
        return Response({"created": BookSerializer(new_post).data})

