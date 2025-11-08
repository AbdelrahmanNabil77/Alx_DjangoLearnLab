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
]
