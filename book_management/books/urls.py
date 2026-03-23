from django.urls import path
from . import views

urlpatterns = [

    
    # AUTHOR ENDPOINTS
    # =========================
    path('authors/', views.get_authors, name='get_authors'),
    path('authors/<int:id>/', views.get_author, name='get_author'),
    path('authors/create/', views.create_author, name='create_author'),
    path('authors/<int:id>/update/', views.update_author, name='update_author'),
    path('authors/<int:id>/delete/', views.delete_author, name='delete_author'),
    path('authors/<int:id>/books/', views.author_books, name='author_books'),
    path('authors/book-count/', views.author_book_count, name='author_book_count'),


    # BOOK ENDPOINTS
    # =========================
    path('books/', views.get_books, name='get_books'),
    path('books/<int:id>/', views.get_book, name='get_book'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:id>/update/', views.update_book, name='update_book'),
    path('books/<int:id>/delete/', views.delete_book, name='delete_book'),

    
    # CATEGORY ENDPOINTS
    # =========================
    path('categories/', views.get_categories, name='get_categories'),
    path('categories/<int:id>/', views.get_category, name='get_category'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:id>/update/', views.update_category, name='update_category'),
    path('categories/<int:id>/delete/', views.delete_category, name='delete_category'),
    path('categories/<int:id>/books/', views.category_books, name='category_books'),

    
    # FILTERING ENDPOINTS
    # =========================
    path('books/author/<int:author_id>/', views.books_by_author, name='books_by_author'),
    path('books/category/<int:category_id>/', views.books_by_category, name='books_by_category'),
    path('books/search/', views.search_books, name='search_books'),
    path('books/price-range/', views.price_range, name='price_range'),
    path('books/available/', views.available_books, name='available_books'),
    path('books/order-by-date/', views.order_by_date, name='order_by_date'),
    path('books/top-5/', views.top_5_books, name='top_5_books'),
]