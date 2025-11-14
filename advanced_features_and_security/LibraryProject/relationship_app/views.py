from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book



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

# ✅ Login View (uses Django’s built-in LoginView)
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# ✅ Logout View (uses Django’s built-in LogoutView)
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# ✅ Registration View (custom)
def register(request):
    """
    Allow new users to register using Django’s UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect user to login page after successful registration
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})

@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Admin')
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
@login_required
def add_book(request):
    """
    View to add a new book. Only users with 'can_add_book' permission can access.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title:
            book = Book.objects.create(title=title)
            return render(request, 'relationship_app/add_book_success.html', {'book': book})
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
@login_required
def edit_book(request, book_id):
    """
    View to edit a book. Only users with 'can_change_book' permission can access.
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            book.title = new_title
            book.save()
            return render(request, 'relationship_app/edit_book_success.html', {'book': book})

    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
@login_required
def delete_book(request, book_id):
    """
    View to delete a book. Only users with 'can_delete_book' permission can access.
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return render(request, 'relationship_app/delete_book_success.html')

    return render(request, 'relationship_app/delete_book.html', {'book': book})

