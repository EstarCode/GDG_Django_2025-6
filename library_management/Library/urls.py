from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book-list'),
    path("books/<int:book_id>/loan/", views.CreateLoanView.as_view(), name='create-loan'),
]