import csv
import os

DATA_PATH = "data/books.csv"

class Book:
    def __init__(self, book_id, title, author="Unknown", publisher="", publish_date="", available=True, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.available = available == "True" if isinstance(available, str) else available
        self.copies = int(copies)

    def borrow(self):
        if self.available:
            self.copies -= 1
            if self.copies == 0:
                self.available = False
            return True
        return False

    def return_book(self):
        self.copies += 1
        self.available = True

    def __str__(self):
        return (
            f"Book ID: {self.book_id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Publisher: {self.publisher}\n"
            f"Publish Date: {self.publish_date}\n"
            f"Copies: {self.copies}\n"
            f"Available: {'Yes' if self.available else 'No'}"
        )

# ===== Helper functions =====

def load_books():
    books = []
    if not os.path.exists(DATA_PATH):
        return books
    with open(DATA_PATH, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            book = Book(*row)
            books.append(book)
    return books

def save_books(books):
    with open(DATA_PATH, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for book in books:
            writer.writerow([
                book.book_id,
                book.title,
                book.author,
                book.publisher,
                book.publish_date,
                str(book.available),
                book.copies
            ])

def get_book_by_id(book_id):
    books = load_books()
    for book in books:
        if book.book_id == book_id:
            return book
    return None
