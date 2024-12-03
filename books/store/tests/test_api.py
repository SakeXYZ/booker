from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BooksSerializer


class BooksAPITestCase(APITestCase):
    def test_get(self):
        book1 = Book.objects.create(name='Test Books 1', price=25)
        book2 = Book.objects.create(name='Test Books 2', price=30)
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([book1, book2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
