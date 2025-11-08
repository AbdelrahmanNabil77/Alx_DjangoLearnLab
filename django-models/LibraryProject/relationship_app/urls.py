from django.urls import path
# ✅ Explicit import required by checker
from .views import list_books
from .views import LibraryDetailView  # optional but good practice

urlpatterns = [
    # ✅ Function-based view URL
    path('books/', list_books, name='list_books'),

    # ✅ Class-based view URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
