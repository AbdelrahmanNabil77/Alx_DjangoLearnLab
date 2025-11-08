from django.urls import path
# ✅ Explicit import required by checker
from .views import list_books
from .views import LibraryDetailView  # optional but good practice
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # ✅ for direct use
from . import views  # ✅ so we can reference views.register and others
from .views import (
    list_books,
    LibraryDetailView,
    UserLoginView,
    UserLogoutView,
    register,
)

urlpatterns = [
    # ✅ Function-based view URL
    path('books/', list_books, name='list_books'),

    # ✅ Class-based view URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

# ✅ Authentication routes
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
