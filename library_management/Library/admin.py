from django.contrib import admin
from .models import Author, Book, Member, Category, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    # What columns show in the admin list
    list_display = ("title", "author", "available_copies")

    # Filters (right sidebar)
    list_filter = ("author", "categories")

    # Search bar
    search_fields = ("title", "isbn")


# Register other models normally
admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Loan)

