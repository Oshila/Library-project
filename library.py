import csv
from book import Book

BOOKS_FILE = 'data/books.csv'

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            with open(BOOKS_FILE, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 7:
                        continue
                    book_id = row[0]
                    title = row[1]
                    author = row[2]
                    publisher = row[3]
                    publish_date = row[4]
                    available = row[5] == "True"
                    copies = int(row[6])
                    book = Book(book_id, title, author, copies)
                    book.available = available
                    books.append(book)
        except FileNotFoundError:
            print(f"{BOOKS_FILE} not found. Starting with empty library.")
        return books

    def save_books(self):
        with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([
                    book.book_id,
                    book.title,
                    book.author,
                    "Unknown",  # placeholder for publisher
                    "01-01-2000",  # placeholder for publish date
                    book.available,
                    book.copies
                ])

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added successfully.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def list_all_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in the Library:")
            for book in self.books:
                print(book)
                print('-' * 40)

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
