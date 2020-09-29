from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from library_system.models import Book, Author, Genre, BookInstance, Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
    paginate_by = 3

    args = {'books': books,
            'paginate_by': paginate_by}
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


# ----------------------------------------------------------------------------------------


class AuthorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class AuthorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
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

class AuthorDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Author
    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

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

# ----------------------------------------------------------------------------------------


class GenreCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Genre
    fields = ['name']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class GenreListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    genres = Genre.objects.all()
    model = Genre
    template_name = 'library_system/home.html'
    context_object_name = 'genres'
    ordering = ['-date_created']
    paginate_by = 3

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class GenreDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Genre
    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

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


# ----------------------------------------------------------------------------------------

class ReviewCreateView(CreateView):
    model = Review
    fields = ['book', 'review_text', 'review_writer']
    success_url = '/library_system/reviews'

def FilteredReview(request):
    template = 'library_system/home.html'
    query = request.GET.get('q')
    print(query)
    if query:
        print("query exists")
        reviews = Review.objects.filter(book__id__iexact=query)
        print(reviews)
    else:
        reviews = Review.objects.all()
    context = {
        "object_list": reviews
    }
    return render(request, template, context)


class ReviewListView(ListView):
    reviews = Review.objects.all()
    model = Review
    template_name = 'library_system/home.html'
    context_object_name = 'reviews'
    ordering = ['-date_created']
    paginate_by = 3


class ReviewDetailView(DetailView):
    model = Review

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['review_text']

    def test_func(self):
        #get the post we're updating
        review = self.get_object()
        if self.request.user.role=="regular":
            return True
        return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/library_system/reviews'
    def test_func(self):
        #get the post we're updating
        review = self.get_object()
        if self.request.user.role=="regular":
            return True
        return False


# ---------------------------------------------------------------------------------

class BookInstanceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BookInstance
    fields = ['book', 'borrower', 'version', 'due_back', 'status']

    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

def BookInstanceListView(request):
    template = 'library_system/home.html'
    query = request.GET.get('q')
    query2 = request.GET.get('u')
    print(query)
    print(query2)
    paginate_by = 3
    if query:
        print("query exists")
        book_copies = BookInstance.objects.filter(book__title__iexact=query)
        print(book_copies)
        context = {
            "bookinstances": book_copies,
            "paginate_by": paginate_by
        }
    elif query2:
        print("query exists 2 ")
        books_borrowed = BookInstance.objects.filter(borrower__email=query2)
        print(books_borrowed)
        template = 'library_system/profile.html'
        context = {
            "booksborrowed": books_borrowed,
            "paginate_by": paginate_by
        }
    else:
        book_copies = BookInstance.objects.all()
        books_borrowed = []
        context = {
            "booksborrowed": books_borrowed,
            "bookinstances": book_copies,
            "paginate_by": paginate_by
        }
    paginate_by = 3
    return render(request, template, context)
    # bookinstances = BookInstance.objects.all()
    # model = BookInstance


class BookInstanceDetailView(DetailView):
    model = BookInstance
    def test_func(self):
        #get the post we're updating
        if self.request.user.role=="manager":
            return True
        return False

class BookInstanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BookInstance
    fields = ['version', 'due_back', 'status', 'borrower']

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False

class BookInstanceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BookInstance
    success_url = '/library_system/bookinstance'

    def test_func(self):
        #get the post we're updating
        book = self.get_object()
        if self.request.user.role=="manager":
            return True
        return False

def profile(request):
    template = 'library_system/profile.html'
    query = request.GET.get('q')
    print(query)
    paginate_by = 3
    if query:
        print("query exists")
        reviews = Review.objects.filter(review_writer__email__iexact=query)
        books_borrowed = BookInstance.objects.filter(borrower__email=query)
        print(reviews)
    else:
        reviews = []
        books_borrowed = []
    context = {
        "object_list": reviews,
        "booksborrowed": books_borrowed,
        "paginate_by": paginate_by
    }
    return render(request, template, context)
