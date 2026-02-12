from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books" )
    categories = models.ManyToManyField(Category, related_name="books")

    def __str__(self):
        return self.title



class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="loans")
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member} borrowed '{self.book}'"
