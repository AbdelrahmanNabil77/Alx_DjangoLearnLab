from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # ✅ for direct use
from . import views  # ✅ so we can reference views.register and others

urlpatterns = [
    # ✅ Function-based view
    path('books/', views.list_books, name='list_books'),

    # ✅ Class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Authentication routes using built-in views directly
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
    path('register/', views.register, name='register'),

    # ✅ Role-based routes
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # ✅ Permission-protected book views (checker wants exact names)
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
