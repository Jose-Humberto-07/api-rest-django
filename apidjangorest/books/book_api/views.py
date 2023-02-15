from django.shortcuts import render
from django.http import JsonResponse
from book_api.models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    books_python = list(books.values())
    return JsonResponse({
        'books': books_python
    })
