from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

"""
API VIEWS
"""


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


"""
WEBSITE VIEWS
"""


def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})