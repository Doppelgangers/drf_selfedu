from django.urls import path, include

# from book.views import BookViewSet
# from rest_framework import routers
#
# router = routers.SimpleRouter()
# router.register(r"book", BookViewSet, basename="book")

from book.views import BookListAPI, BookUpdateAPI, BookDestroyAPI
urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('api/v1/book/', BookListAPI.as_view()),
    path('api/v1/book/<int:pk>/', BookUpdateAPI.as_view()),
    path('api/v1/book/delate/<int:pk>/', BookDestroyAPI.as_view()),

]
