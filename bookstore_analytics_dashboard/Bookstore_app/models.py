from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title