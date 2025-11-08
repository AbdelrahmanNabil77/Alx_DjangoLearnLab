# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ✅ Function-based view route
    path('books/', views.list_books, name='list_books'),

    # ✅ Class-based view route
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
