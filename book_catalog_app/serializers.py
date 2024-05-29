from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
       model = Profile
       fields = ['id', 'first_name', 'last_name', 'favorites', 'tbr']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ['genre']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'book_genre', 'isbn']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['star']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book', 'stars', 'review_body', 'reviewer_name']