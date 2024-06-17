from django.urls import path
from .views import BookListCreate, BookDetail, home, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('books/api/', BookListCreate.as_view(), name='book_list_create'),
    path('books/api/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]
