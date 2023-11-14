from django.urls import path, include

from book.views import BookViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"book", BookViewSet, basename="book")


urlpatterns = [
    path('api/v1/', include(router.urls)),


]
