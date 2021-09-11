from drbooks.models import Book, Review
from drbooks.serializers import BookSerializer, ReviewSerializer
from rest_framework import viewsets, permissions

class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    permission_classes= [
        permissions.AllowAny
        ]
    serializer_class= BookSerializer
class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    permission_classes= [
        permissions.AllowAny
        ]
    serializer_class= ReviewSerializer