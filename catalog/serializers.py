from rest_framework import serializers
from .models import Book, Genre, Language, Author, BookInstance


class BookSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'summary', 'isbn', 'language', 'genre']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Genre
    fields = ['id', 'name']


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Language
    fields = ['id', 'name']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Author
    fields = ('first_name','last_name','date_of_birth','date_of_death')


# BookInstance
class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = BookInstance
    fields = ('id', 'book', 'imprint', 'due_back', 'borrower', )
