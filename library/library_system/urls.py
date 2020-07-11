from django.urls import path
from . import views
from .views import (
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView,
    AuthorListView, AuthorDetailView,
    AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    GenreListView, GenreDetailView,
    GenreCreateView, GenreUpdateView, GenreDeleteView )

urlpatterns = [
    path('', BookListView.as_view(), name="libsys-home"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('book/new/', BookCreateView.as_view(), name="book-create"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name="book-delete"),

    path('author/new/', AuthorCreateView.as_view(), name="author-create"),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name="author-detail"),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name="author-update"),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name="author-delete"),
    path('authors/',AuthorListView.as_view(), name="author-list" ),

    path('genre/new/', GenreCreateView.as_view(), name="genre-create"),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name="genre-detail"),
    path('genre/<int:pk>/update/', GenreUpdateView.as_view(), name="genre-update"),
    path('genre/<int:pk>/delete/', GenreDeleteView.as_view(), name="genre-delete"),
    path('genres/',GenreListView.as_view(), name="genre-list" )
]
