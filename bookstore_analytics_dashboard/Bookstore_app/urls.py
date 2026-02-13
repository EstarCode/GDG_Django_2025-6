from django.urls import path
from . import views

urlpatterns = [
    path("after2010/", views.after_2010, name="books_after_2010"),
    path("python/", views.python_books, name="python_books"),
    path("usa_authors/", views.usa_authors, name="usa_authors"),
    path("books_authors/", views.books_with_authors, name="books_with_authors"),
    path("expensive_authors/", views.expensive_authors, name="expensive_authors"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
