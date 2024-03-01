from django.urls import path
from .views import *


urlpatterns = [
    path('books', books_list, name='books'),
    path('book/<int:book_id>/', get_book, name='get_book')
]