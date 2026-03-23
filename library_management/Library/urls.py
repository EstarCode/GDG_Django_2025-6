from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/borrow/', views.CreateLoanView.as_view(), name='create_loan'),
]