import csv
import os

DATA_PATH = "data/librarian.csv"

class Librarian:
    def __init__(self, librarian_id, name, password=None):
        self.librarian_id = librarian_id
        self.name = name
        self.password = password  # Only used internally

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Librarian {self.name} added '{book.title}'.")

    def remove_book(self, library, book_id):
        if library.remove_book(book_id):
            print(f"Librarian {self.name} removed book with ID {book_id}.")
        else:
            print(f"Book with ID {book_id} not found.")

    def __str__(self):
        return f"Librarian ID: {self.librarian_id}, Name: {self.name}"

# ===== Helper Functions =====

def create_lib_id():
    if not os.path.exists(DATA_PATH):
        return "lb0001"
    with open(DATA_PATH, newline='') as f:
        rows = list(csv.reader(f))
        if not rows:
            return "lb0001"
        last_id = rows[-1][0]
        num = int(last_id[2:]) + 1
        return f"lb{num:04d}"

def save_librarian(lib):
    with open(DATA_PATH, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([lib.librarian_id, lib.name, lib.password])
    print(f"Librarian {lib.name} saved successfully.")

def auth_librarian(lib_id, password):
    if not os.path.exists(DATA_PATH):
        return None
    with open(DATA_PATH, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == lib_id and row[2] == password:
                return Librarian(row[0], row[1], row[2])
    return None
