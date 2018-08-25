from django.contrib import admin
from .models import Book, Author, Genre, BookInstance

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

#admin.site.register(Book)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]