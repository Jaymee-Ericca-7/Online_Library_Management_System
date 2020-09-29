from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
#
# from users.forms import CustomUserCreationForm, CustomUserChangeForm
# from users.models import CustomUser
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'role']
#
# admin.site.register(CustomUser, CustomUserAdmin)
#

# Register your models here.

# from .models import Author, Genre, Book, BookInstance, Language
#
#
# #admin.site.register(Book)
# # admin.site.register(Author)
# admin.site.register(Genre)
# #admin.site.register(BookInstance)
# admin.site.register(Language)
#
# class BooksInline(admin.TabularInline):
#     model = Book
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#     inlines = [BooksInline]
#
# admin.site.register(Author, AuthorAdmin)
#
# class BookInstanceInline(admin.TabularInline):
#     model = BookInstance
#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author')
#     inlines = [BookInstanceInline]
# admin.site.register(Book, BookAdmin)
#
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#     fieldsets = (
#         (None, {
#             'fields': ('book','imprint','id')
#             }),
#         ('Availability',{
#             'fields':('status','due_back')
#             }),
#         )
#     list_display = ('book','status','due_back','id')
# admin.site.register(BookInstance, BookInstanceAdmin)
