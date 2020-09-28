from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from library_system.models import Book, Author, Genre, BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


class SearchListView(ListView):
    model = Book
    template_name = 'library_system/home.html'
    context_object_name = 'books'
    ordering = ['-date_created']
    paginate_by = 3

    def get_queryset(self):
      result = super(SearchListView, self).get_queryset()
      query = self.request.GET.get('search')
      if query:
          postresult = Book.objects.filter(title__contains=query)
          result = postresult
      else:
          result = None
      return result


def home(request):

    books = Book.objects.all()
    args = {'books': books}
    return render(request, 'library_system/home.html', args)

class BookListView(ListView):
    model = Book
    template_name = 'library_system/home.html'
    context_object_name = 'books'
    ordering = ['-date_created']
    paginate_by = 3

class BookDetailView(DetailView):
    model = Book

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'isbn','genre', 'publisher', 'year_of_pub']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'isbn','genre', 'publisher', 'year_of_pub']

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/library_system'
    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False

class AuthorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class AuthorListView(ListView):
    authors = Author.objects.all()
    model = Author
    template_name = 'library_system/home.html'
    context_object_name = 'authors'
    ordering = ['-date_created']
    paginate_by = 3

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class AuthorDetailView(DetailView):
    model = Author

class AuthorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class AuthorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Author
    success_url = '/library_system/authors'
    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False


class GenreCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Genre
    fields = ['name']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class GenreListView(ListView):
    genres = Genre.objects.all()
    model = Genre
    template_name = 'library_system/home.html'
    context_object_name = 'genres'
    ordering = ['-date_created']
    paginate_by = 3


class GenreDetailView(DetailView):
    model = Genre

class GenreUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Genre
    fields = ['name']

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False

class GenreDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Genre
    success_url = '/library_system/genres'
    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False


class BookInstanceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BookInstance
    fields = ['id', 'book', 'imprint', 'due_back', 'status']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class BookInstanceListView(ListView):
    bookinstances = BookInstance.objects.all()
    model = BookInstance
    template_name = 'library_system/home.html'
    context_object_name = 'bookinstances'
    ordering = ['-date_created']
    paginate_by = 3


class BookInstanceDetailView(DetailView):
    model = BookInstance

class BookInstanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BookInstance
    fields = ['imprint', 'due_back', 'status']

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False

class BookInstanceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BookInstance
    success_url = '/bookinstance'
    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False
