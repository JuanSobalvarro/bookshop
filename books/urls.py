from django.urls import path
from .views import BookListCreate, BookDetail, home, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('api/books/', BookListCreate.as_view(), name='book_list_create'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]
