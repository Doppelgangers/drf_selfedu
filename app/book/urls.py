from django.urls import path

from book.views import BookAPIView

urlpatterns = [
    path('api/v1/bock/list', BookAPIView.as_view())
]
