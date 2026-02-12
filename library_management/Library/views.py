from django.shortcuts import render
from .models import Author, Book, Member, Category, Loan
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from .models import ...


def book_list(request):
    books = Book.objects.select_related("author").prefetch_related("categories")

    context = {
        "books": books
    }

    return render(request, "books.html", context)



class CreateLoanView(View):
    def post(self, request, book_id, *args, **kwargs):

        member_id = request.POST.get("member_id")

        if not member_id:
            return JsonResponse({"error": "member_id is required"}, status=400)

        # book comes from URL
        book = get_object_or_404(Book, id=book_id)
        member = get_object_or_404(Member, id=member_id)

        # check availability
        if book.available_copies <= 0:
            return JsonResponse({"error": "Book not available"}, status=400)

        # create loan
        Loan.objects.create(book=book, member=member)

        # update copies
        book.available_copies -= 1
        book.save()

        return JsonResponse({
            "message": f"{member} borrowed '{book.title}'"
        }, status=201)
   