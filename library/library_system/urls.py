from django.urls import path
from . import views
from .views import ( SearchListView,
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView,
    AuthorListView, AuthorDetailView,
    AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    GenreListView, GenreDetailView,
    GenreCreateView, GenreUpdateView, GenreDeleteView,
    BookInstanceDetailView, BookInstanceListView,
    BookInstanceCreateView,BookInstanceUpdateView, BookInstanceDeleteView,
    ReviewDetailView, ReviewListView,FilteredReview,
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
    profile, borrow_book, return_book)

urlpatterns = [
    path('profile/', profile, name="profile-page" ),

    path('', BookListView.as_view(), name="libsys-home"),
    path('search/', SearchListView.as_view(), name="libsys-search"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('book/new/', BookCreateView.as_view(), name="book-create"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name="book-delete"),

    path('book/borrow_book/', borrow_book, name="borrow_book"),
    path('book/return_book/', return_book, name="return_book"),

    path('author/new/', AuthorCreateView.as_view(), name="author-create"),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name="author-detail"),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name="author-update"),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name="author-delete"),
    path('authors/',AuthorListView.as_view(), name="author-list" ),

    path('genre/new/', GenreCreateView.as_view(), name="genre-create"),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name="genre-detail"),
    path('genre/<int:pk>/update/', GenreUpdateView.as_view(), name="genre-update"),
    path('genre/<int:pk>/delete/', GenreDeleteView.as_view(), name="genre-delete"),
    path('genres/',GenreListView.as_view(), name="genre-list" ),

    path('review/<int:pk>/', ReviewDetailView.as_view(), name="review-detail"),
    path('f_reviews/', FilteredReview, name="filtered-review-list"),
    path('reviews/', ReviewListView.as_view(), name="review-list"),
    path('review/new/', ReviewCreateView.as_view(), name="review-create"),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name="review-update"),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review-delete"),

    path('bookinstance/new/', BookInstanceCreateView.as_view(), name="bookinstance-create"),
    path('bookinstance/<pk>/', BookInstanceDetailView.as_view(), name="bookinstance-detail"),
    path('bookinstance/<pk>/update/', BookInstanceUpdateView.as_view(), name="bookinstance-update"),
    path('bookinstance/<pk>/delete/', BookInstanceDeleteView.as_view(), name="bookinstance-delete"),
    path('bookinstance/',BookInstanceListView, name="bookinstance-list"),

]
