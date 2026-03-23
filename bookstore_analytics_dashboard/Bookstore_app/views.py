from django.shortcuts import render
from .models import Book, Author
from django.db.models import Sum


def after_2010(request):
    books = Book.objects.filter(published_year__gt=2010)
    return render(request, "Bookstore_app/after_2010.html", {
        "title": "Books After 2010",
        "books": books
    })


def python_books(request):
    books = Book.objects.filter(title__icontains="python")
    return render(request, "Bookstore_app/python_books.html", {
        "title": "Python Books",
        "books": books
    })


def usa_authors(request):
    authors = Author.objects.filter(country="USA").order_by("name")
    return render(request, "Bookstore_app/usa_authors.html", {
        "title": "USA Authors",
        "authors": authors
    })


def books_with_authors(request):
    books = Book.objects.select_related("author")
    return render(request, "Bookstore_app/books_with_authors.html", {
        "title": "Books With Authors",
        "books": books
    })


def expensive_authors(request):
    authors = Author.objects.filter(
        books__price__gt=50
    ).distinct().prefetch_related("books")

    return render(request, "Bookstore_app/expensive_authors.html", {
        "title": "Authors With Expensive Books",
        "authors": authors
    })


def dashboard(request):
    authors = Author.objects.annotate(
        total_revenue=Sum("books__price")
    ).order_by("-total_revenue")[:5].prefetch_related("books")

    return render(request, "Bookstore_app/dashboard.html", {
        "title": "Top 5 Authors by Revenue",
        "authors": authors
    })