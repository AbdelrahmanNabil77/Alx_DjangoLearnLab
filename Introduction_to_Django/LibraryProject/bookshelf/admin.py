from django.contrib import admin

# Register your models here.
from .models import Book

# Customize how the Book model appears in the Django admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for quick navigation
    list_filter = ('publication_year', 'author')
    
    # Enable search by title or author
    search_fields = ('title', 'author')