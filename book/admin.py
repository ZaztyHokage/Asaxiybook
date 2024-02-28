from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookOrder)
admin.site.register(Feedback)
admin.site.register(FavoriteAuthor)
admin.site.register(Wishlist)
