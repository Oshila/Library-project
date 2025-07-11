import csv
import os

<<<<<<< HEAD
DATA_PATH = "data/librarian.csv"

class Librarian:
    def __init__(self, librarian_id, name, password=None):
        self.librarian_id = librarian_id
        self.name = name
        self.password = password  # Only used internally

    def add_book(self, library, book):
=======
# File path to store librarian data
DATA_PATH = "data/librarian.csv"

class Librarian:

    #For a librarian user who can manage books.
    def __init__(self, librarian_id, name, password=None):
        self.librarian_id = librarian_id  # Unique ID for each librarian
        self.name = name    # Librarian's name
        self.password = password  # Used only for authentication

    def add_book(self, library, book):

        #Adds a new book to the library.
>>>>>>> 7575790 (adding comments in code)
        library.add_book(book)
        print(f"Librarian {self.name} added '{book.title}'.")

    def remove_book(self, library, book_id):
<<<<<<< HEAD
=======

        #Removes a book by its ID if it exists
>>>>>>> 7575790 (adding comments in code)
        if library.remove_book(book_id):
            print(f"Librarian {self.name} removed book with ID {book_id}.")
        else:
            print(f"Book with ID {book_id} not found.")

    def __str__(self):
<<<<<<< HEAD
        return f"Librarian ID: {self.librarian_id}, Name: {self.name}"

# ===== Helper Functions =====

def create_lib_id():
=======
        # Shows the librarian’s ID and name when printed
        return f"Librarian ID: {self.librarian_id}, Name: {self.name}"

# ---- Helper Functions ----

def create_lib_id():

    #Creates a new unique librarian ID based on the last one in the file.
    #Start from lb0001 if no data
>>>>>>> 7575790 (adding comments in code)
    if not os.path.exists(DATA_PATH):
        return "lb0001"
    with open(DATA_PATH, newline='') as f:
        rows = list(csv.reader(f))
        if not rows:
            return "lb0001"
<<<<<<< HEAD
        last_id = rows[-1][0]
        num = int(last_id[2:]) + 1
        return f"lb{num:04d}"

def save_librarian(lib):
=======

        last_id = rows[-1][0]    # Get last librarian ID
        num = int(last_id[2:]) + 1  # Increase the number part
        return f"lb{num:04d}"    # Format as lb0002, lb0003, etc

def save_librarian(lib):

    #Saves a new librarian's details to the CSV file
>>>>>>> 7575790 (adding comments in code)
    with open(DATA_PATH, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([lib.librarian_id, lib.name, lib.password])
    print(f"Librarian {lib.name} saved successfully.")

def auth_librarian(lib_id, password):
<<<<<<< HEAD
=======

    #Checks if a librarian ID and password match what's saved in the file
>>>>>>> 7575790 (adding comments in code)
    if not os.path.exists(DATA_PATH):
        return None
    with open(DATA_PATH, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == lib_id and row[2] == password:
<<<<<<< HEAD
                return Librarian(row[0], row[1], row[2])
    return None
=======
                return Librarian(row[0], row[1], row[2]) # Finds and returns the librarian if the ID and password match

    return None #No match found
>>>>>>> 7575790 (adding comments in code)
