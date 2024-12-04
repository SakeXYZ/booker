from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BooksSerializer


class BooksAPITestCase(APITestCase):

    def setUp(self):
        self.book1 = Book.objects.create(name='B Test Books 1', price=25,
                                         author_name='Test Author 1')

        self.book2 = Book.objects.create(name='C Test Books 2', price=30,
                                         author_name='Test Author 2')

        self.book3 = Book.objects.create(name='A Test Books Test Author 1', price=50,
                                         author_name='Test Author 3')

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': "Test Author 1"})
        serializer_data = BooksSerializer([self.book1, self.book2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'filter':'name'})
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        print(response.data, serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)