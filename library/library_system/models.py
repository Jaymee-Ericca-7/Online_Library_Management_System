from django.db import models
from django.urls import reverse
from account.models import Account
from datetime import datetime, timedelta

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g Science Fiction)')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', kwargs={'pk': self.pk})

class Review(models.Model):
    review_text = models.CharField(max_length=1000)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    review_writer = models.ForeignKey(Account,on_delete=models.SET_NULL, null=True, blank=True, default="Anonymouos")

    def _str_(self):
        return self.review_text

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN number')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    publisher = models.CharField(max_length=200)
    year_of_pub = models.CharField(max_length=4)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

import uuid

def get_deadline():
    return datetime.today() + timedelta(days=7)

class BookInstance(models.Model):
    """Model representing a specific copy of a book"""
    LOAN_STATUS = (
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID', editable=False)
    status = models.CharField(max_length=20, choices=LOAN_STATUS, blank=True, default='Available', help_text='Book Availability')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    version = models.CharField(max_length=200, help_text='description or version of book copy (eq. "5th edition" )', null=True)
    due_back = models.DateField(null=True, default=get_deadline)
    borrower = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'

    def get_absolute_url(self):
        return reverse('bookinstance-detail', kwargs={'pk': self.id})


class Author(models.Model):
    """Model representing an author. """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null = True, blank=True,  help_text='Format: yyyy-mm-dd')
    date_of_death = models.DateField(null=True, blank=True, help_text='Format: yyyy-mm-dd')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

class Language(models.Model):
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
