from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# ✅ Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books and their authors.
    """
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})



# ✅ Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'