from django.http import JsonResponse
from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from .models import Author, Book, Category
import json

def get_authors(request):
    authors = list(Author.objects.values())
    return JsonResponse(authors, safe=False, status=200)

def get_author(request, id):
    try:
        author = Author.objects.get(author_id=id)
        return JsonResponse({
            "author_id": author.author_id,
            "name": author.name,
            "bio": author.bio,
            "date_of_birth": author.date_of_birth,
            "created_at": author.created_at
        }, status=200)
    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)

@csrf_exempt
def create_author(request):
    if request.method == "POST":
        data = json.loads(request.body)
        author = Author.objects.create(
            name=data.get("name"),
            bio=data.get("bio"),
            date_of_birth=data.get("date_of_birth")
        )
        return JsonResponse({"message": "Author created", "author_id": author.author_id}, status=201)

@csrf_exempt
def update_author(request, id):
    if request.method == "PUT":
        try:
            author = Author.objects.get(author_id=id)
            data = json.loads(request.body)

            author.name = data.get("name", author.name)
            author.bio = data.get("bio", author.bio)
            author.date_of_birth = data.get("date_of_birth", author.date_of_birth)
            author.save()

            return JsonResponse({"message": "Updated"}, status=200)
        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)


@csrf_exempt
def delete_author(request, id):
    if request.method == "DELETE":
        try:
            author = Author.objects.get(author_id=id)
            author.delete()
            return JsonResponse({"message": "Deleted"}, status=200)
        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)
@csrf_exempt
def update_author(request, id):
    if request.method == "PUT":
        try:
            author = Author.objects.get(author_id=id)
            data = json.loads(request.body)

            author.name = data.get("name", author.name)
            author.bio = data.get("bio", author.bio)
            author.date_of_birth = data.get("date_of_birth", author.date_of_birth)
            author.save()

            return JsonResponse({"message": "Updated"}, status=200)
        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)

def author_books(request, id):
    try:
        books = Book.objects.filter(author_id=id).values()
        return JsonResponse(list(books), safe=False, status=200)
    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)

def author_book_count(request):
    authors = Author.objects.annotate(total_books=Count("books")).values("author_id", "name", "total_books")
    return JsonResponse(list(authors), safe=False, status=200)

def get_books(request):
    books = Book.objects.select_related("author").prefetch_related("categories")

    data = []
    for b in books:
        data.append({
            "book_id": b.book_id,
            "title": b.title,
            "author": b.author.name,
            "price": b.price,
            "available": b.available
        })

    return JsonResponse(data, safe=False, status=200)

def get_book(request, id):
    try:
        b = Book.objects.select_related("author").prefetch_related("categories").get(book_id=id)
        return JsonResponse({
            "book_id": b.book_id,
            "title": b.title,
            "author": b.author.name,
            "categories": [c.name for c in b.categories.all()],
            "price": b.price
        }, status=200)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)
    
@csrf_exempt
def create_book(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if Book.objects.filter(isbn=data.get("isbn")).exists():
            return JsonResponse({"error": "ISBN must be unique"}, status=400)

        try:
            author = Author.objects.get(author_id=data.get("author_id"))

            book = Book.objects.create(
                title=data.get("title"),
                author=author,
                published_date=data.get("published_date"),
                isbn=data.get("isbn"),
                price=data.get("price"),
                available=data.get("available", True)
            )

            if "categories" in data:
                book.categories.set(data["categories"])

            return JsonResponse({"message": "Book created"}, status=201)

        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)

@csrf_exempt
def update_book(request, id):
    if request.method == "PUT":
        try:
            book = Book.objects.get(book_id=id)
            data = json.loads(request.body)

            if "isbn" in data and Book.objects.exclude(book_id=id).filter(isbn=data["isbn"]).exists():
                return JsonResponse({"error": "ISBN must be unique"}, status=400)

            book.title = data.get("title", book.title)
            book.price = data.get("price", book.price)
            book.available = data.get("available", book.available)
            book.save()

            return JsonResponse({"message": "Updated"}, status=200)

        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

@csrf_exempt
def delete_book(request, id):
    if request.method == "DELETE":
        try:
            book = Book.objects.get(book_id=id)
            book.delete()
            return JsonResponse({"message": "Deleted"}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        
def get_categories(request):
    return JsonResponse(list(Category.objects.values()), safe=False)

def get_category(request, id):
    try:
        c = Category.objects.get(category_id=id)
        return JsonResponse({"category_id": c.category_id, "name": c.name})
    except Category.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    
@csrf_exempt
def create_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        c = Category.objects.create(name=data.get("name"))
        return JsonResponse({"message": "Created"}, status=201)

@csrf_exempt
def update_category(request, id):
    if request.method == "PUT":
        try:
            c = Category.objects.get(category_id=id)
            data = json.loads(request.body)
            c.name = data.get("name", c.name)
            c.save()
            return JsonResponse({"message": "Updated"})
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        
@csrf_exempt
def delete_category(request, id):
    if request.method == "DELETE":
        try:
            Category.objects.get(category_id=id).delete()
            return JsonResponse({"message": "Deleted"})
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

def category_books(request, id):
    books = Book.objects.filter(categories__category_id=id).values()
    return JsonResponse(list(books), safe=False)

def books_by_author(request, author_id):
    books = Book.objects.filter(author_id=author_id).values()
    return JsonResponse(list(books), safe=False)

def books_by_category(request, category_id):
    books = Book.objects.filter(categories__category_id=category_id).values()
    return JsonResponse(list(books), safe=False)

def search_books(request):
    q = request.GET.get("q")
    books = Book.objects.filter(title__icontains=q).values()
    return JsonResponse(list(books), safe=False)

def price_range(request):
    min_price = request.GET.get("min")
    max_price = request.GET.get("max")

    books = Book.objects.filter(price__gte=min_price, price__lte=max_price).values()
    return JsonResponse(list(books), safe=False)

def available_books(request):
    books = Book.objects.filter(available=True).values()
    return JsonResponse(list(books), safe=False)

def order_by_date(request):
    books = Book.objects.order_by("published_date").values()
    return JsonResponse(list(books), safe=False)

def top_5_books(request):
    books = Book.objects.all()[:5].values()
    return JsonResponse(list(books), safe=False)