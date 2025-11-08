from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


def list_books(request):
    """
    Function-based view that lists all books and their authors.
    """
    books = Book.objects.all()
    # ✅ points to templates/relationship_app/list_books.html
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ matches new location
    context_object_name = 'library'
