from django.urls import path

from book.views import BookAPIList, BookAPIUpdate, BookDetailAPI

urlpatterns = [
    path('api/v1/bock', BookAPIList.as_view()),
    path('api/v1/bock/<int:pk>', BookAPIUpdate.as_view()),
    path('api/v1/bock/detail/<int:pk>', BookDetailAPI.as_view()),

]
