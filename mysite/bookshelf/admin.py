from django.contrib import admin
from .models import Language, Author, Book


admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)
