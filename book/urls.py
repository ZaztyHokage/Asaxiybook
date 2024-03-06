from django.urls import path
from .views import *


urlpatterns = [
    path('books', BooksList.as_view(), name='books'),
    path('book/<int:book_id>/', get_book, name='get_book')
]