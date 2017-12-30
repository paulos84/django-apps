from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


# admin.ModelAdmin allow us to define model-specific admin behaviour
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)


# Register the Admin classes for Book using the decorator - it does the same as admin.site.register()
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
