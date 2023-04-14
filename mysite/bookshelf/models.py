from django.db import models
from datetime import date

from django.db.models import F


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_year = models.DateField()
    death_year = models.DateField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} ({self.surname}) {self.age} {self.number_of_book}'

    @property
    def age(self):
        if self.death_year:
            return f'{self.death_year.year - self.birth_year.year}'
        else:
            return f'{date.today().year - self.birth_year.year}'

    @property
    def number_of_book(self):
        # books = Book.objects.filter(author=self.id)
        # return len(books)
        # books = Book.objects.filter(author=self.id).annotate(models.Count('author'))
        bookss = Author.objects.filter(pk=self.id).annotate(books=models.Count('book'))
        # print(books.values())
        print(bookss.values())
        return bookss[0].books


class Language(models.Model):
    title = models.CharField(max_length=50)
    spoken = models.CharField(max_length=50)
    countries = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} ({self.spoken})'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=50)
    language = models.ManyToManyField(Language, related_name='book_language')

    def __str__(self):
        return f'{self.title}'

    # @property
    # def last_year_book(self):
    #     return Book.objects.all().filter(publication_date__gt=self.name)