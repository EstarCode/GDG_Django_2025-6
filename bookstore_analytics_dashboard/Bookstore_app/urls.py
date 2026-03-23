from django.urls import path
from . import views

urlpatterns = [
    path('books/after-2010/', views.after_2010, name='after_2010'),
    path('books/python/', views.python_books, name='python_books'),
    path('authors/usa/', views.usa_authors, name='usa_authors'),
    path('books/with-authors/', views.books_with_authors, name='books_with_authors'),
    path('authors/expensive/', views.expensive_authors, name='expensive_authors'),
    path('dashboard/', views.dashboard, name='dashboard'),
]