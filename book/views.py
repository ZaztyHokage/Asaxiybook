from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *

@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_book(request, book_id):
    book = Book.objects.filter(id=book_id)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data, status=200)