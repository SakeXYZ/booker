from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BooksSerializer


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']


def oauth(request):
    return render(request, 'oauth.html')
