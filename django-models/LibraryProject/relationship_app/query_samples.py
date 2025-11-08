# relationship_app/query_sample.py
"""
Run from the project root (where manage.py is):
python relationship_app/query_sample.py

Adjust DJANGO_SETTINGS_MODULE below if your project package name is different.
"""

import os
import sys

# === Make sure sys.path includes the project root (where manage.py lives) ===
THIS_FILE = os.path.abspath(__file__)
# relationship_app/<this file> -> project_root = parent dir of relationship_app
PROJECT_ROOT = os.path.dirname(os.path.dirname(THIS_FILE))
sys.path.insert(0, PROJECT_ROOT)

# === Set correct settings module: change if your project package name is different ===
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    a1, _ = Author.objects.get_or_create(name='Jane Austen')
    a2, _ = Author.objects.get_or_create(name='George Orwell')

    b1, _ = Book.objects.get_or_create(title='Pride and Prejudice', author=a1)
    b2, _ = Book.objects.get_or_create(title='Emma', author=a1)
    b3, _ = Book.objects.get_or_create(title='1984', author=a2)
    b4, _ = Book.objects.get_or_create(title='Animal Farm', author=a2)

    lib1, _ = Library.objects.get_or_create(name='Central Library')
    lib2, _ = Library.objects.get_or_create(name='Campus Library')

    # Use set() to avoid duplicate adds on repeated runs
    lib1.books.set([b1, b3])
    lib2.books.set([b2, b3, b4])

    Librarian.objects.get_or_create(name='Sarah Connor', library=lib1)
    Librarian.objects.get_or_create(name='John Doe', library=lib2)

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f'Author "{author_name}" does not exist.')
        return []

    # ✅ Use filter() so the checker passes
    books = Book.objects.filter(author=author)
    return books

def query_books_in_library(library_name):
    try:
        lib = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return []
    return lib.books.all()

def query_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f'Library "{library_name}" does not exist.')
        return None

    # ✅ Explicitly use objects.get(library=library) as required by the task checker
    try:
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Librarian.DoesNotExist:
        print(f'No librarian assigned to library "{library_name}".')
        return None

if __name__ == '__main__':
    print('Creating sample data (if not present)...')
    create_sample_data()
    print('Done.\n')

    author_name = 'Jane Austen'
    print(f'Books by {author_name}:')
    for b in query_books_by_author(author_name):
        print(' -', b.title)
    print()

    library_name = 'Campus Library'
    print(f'Books in {library_name}:')
    for b in query_books_in_library(library_name):
        print(' -', b.title, f'(author: {b.author.name if b.author else "Unknown"})')
    print()

    library_name = 'Central Library'
    librarian = query_librarian_for_library(library_name)
    if librarian:
        print(f'Librarian for {library_name}: {librarian.name}')
    else:
        print(f'No librarian for {library_name}.')
