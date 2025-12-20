class Library:
    def __init__(self):
        self.book = None

    def add_book(self, book):
        self.book = book

    def show_book(self):
        return f"{self.book}"


library1 = Library()
library1.add_book("Atomic Habit")
print(library1.show_book())
