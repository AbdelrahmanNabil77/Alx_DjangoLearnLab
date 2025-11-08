from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    # Each book belongs to one author. If author is deleted, set books' author to NULL (nullable).
    author = models.ForeignKey(
        Author,
        related_name='books',   # author.books.all() will return all their books
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} (by {self.author})'


class Library(models.Model):
    name = models.CharField(max_length=200)
    # A library contains many books; books can belong to many libraries
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    # One-to-one: each library has at most one librarian and vice versa
    library = models.OneToOneField(
        Library,
        related_name='librarian',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name} — {self.library.name}'
