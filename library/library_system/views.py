from django.shortcuts import render
from django.http import HttpResponse
from library_system.models import Book, Author, Genre
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    books = Book.objects.all()
    args = {'books': books}
    return render(request, 'library_system/home.html', args)

class BookListView(ListView):
    model = Book
    template_name = 'library_system/home.html'
    context_object_name = 'books'
    ordering = ['-date_created']

class BookDetailView(DetailView):
    model = Book

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'isbn','genre', 'publisher', 'year_of_pub']

    def test_func(self):
        #get the post we're updating
        if self.request.user.username == "jaymee_ericca":
            return True
        return False

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'isbn','genre', 'publisher', 'year_of_pub']

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.username == "jaymee_ericca":
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/library_system'
    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.username == "jaymee_ericca":
            return True
        return False

class AuthorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

    def test_func(self):
        #get the post we're updating
        if self.request.user.username == "jaymee_ericca":
            return True
        return False

class AuthorListView(ListView):
    authors = Author.objects.all()
    model = Author
    template_name = 'library_system/home.html'
    context_object_name = 'authors'
    ordering = ['-date_created']

class AuthorDetailView(DetailView):
    model = Author

class AuthorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.username == "jaymee_ericca":
            return True
        return False

class AuthorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Author
    success_url = '/library_system/authors'
    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.username == "jaymee_ericca":
            return True
        return False


class GenreCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Genre
    fields = ['name']

    def test_func(self):
        #get the post we're updating
        if self.request.user.username == "jaymee_ericca":
            return True
        return False

class GenreListView(ListView):
    authors = Genre.objects.all()
    model = Genre
    template_name = 'library_system/home.html'
    context_object_name = 'genres'
    ordering = ['-date_created']

class GenreDetailView(DetailView):
    model = Genre

class GenreUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Genre
    fields = ['name']

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.username == "jaymee_ericca":
            return True
        return False

class GenreDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Genre
    success_url = '/library_system/genres'
    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.username == "jaymee_ericca":
            return True
        return False
