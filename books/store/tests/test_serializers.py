from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_serializer(self):
        book1 = Book.objects.create(name='Test Books 1', price=25)
        book2 = Book.objects.create(name='Test Books 2', price=30)
        data = BooksSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'name': 'Test Books 1',
                'price': '25.00'
            },

            {
                'id': book2.id,
                'name': 'Test Books 2',
                'price': '30.00'
            }

        ]

        self.assertEqual(expected_data, data)
