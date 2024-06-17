from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from decimal import Decimal
from .models import Book
from datetime import date

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description",
            price=9.99,
            published_date="2020-01-01",
            isbn="1234567890123")

    def test_book_fields(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.description, "Test Description")
        self.assertEqual(book.price, Decimal('9.99'))
        self.assertEqual(book.published_date, date(2020, 1, 1))
        self.assertEqual(book.isbn, "1234567890123")

    def test_unique_title(self):
        # Attempt to create another book with the same title
        with self.assertRaises(IntegrityError):
            # Use assertRaises with a context manager to catch IntegrityError
            with transaction.atomic():
                Book.objects.create(
                    title="Test Book",
                    author="Another Author",
                    description="Another Description",
                    price=9.99,
                    published_date="2020-01-01",
                    isbn="9876543210987"
                )

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Test Author")

    def test_invalid_price(self):
        # Attempt to create a book with an invalid price (non-numeric)
        with self.assertRaises(ValidationError):
            Book.objects.create(
                title="Invalid Price Book",
                author="Test Author",
                description="Test Description",
                price="Invalid Price",  # This should trigger a ValidationError
                published_date="2020-01-01",
                isbn="1234567890123"
            )

