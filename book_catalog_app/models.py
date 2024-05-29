from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
       return self.name

class BookGenre(models.Model):
    genre = models.CharField(max_length=75, null=True)

    def __str__(self):
       return self.genre

class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    book_genre = models.ManyToManyField(BookGenre)
    isbn = models.PositiveIntegerField(null=True)

    def __str__(self):
       return f'{self.title} by {self.author}, Genre: {self.book_genre}, ISBN: {self.isbn}'

class Rating(models.Model):
    star = models.PositiveIntegerField(null=True)

    def __str__(self):
       return self.star

class Profile (models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
   first_name = models.TextField()
   last_name = models.TextField()

   def __str__(self):
       return self.user.username
   
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    stars = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True)
    review_body = models.CharField(max_length=800, null=True)
    reviewer_name = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
       return f'Book: {self.book}, {self.stars} Star Rating, by {self.reviewer_name}, {self.review_body}'
   
