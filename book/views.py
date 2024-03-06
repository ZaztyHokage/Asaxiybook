from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializer import *
from .models import *


# @api_view(['GET'])
# def books_list(request):
#     books = Book.objects.all()
#     authors = request.GET.getlist('author_id')
#     genre = request.GET.getlist('genre')

#     if authors:
#         books = books.filter(author_id__in=authors)

#     if genre:
#         books = books.filter(genre__in=genre)

#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data, status=200)


class BooksList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def get_book(request, book_id):
    book = Book.objects.filter(id=book_id)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data, status=200)