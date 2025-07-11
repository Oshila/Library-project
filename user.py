import csv
<<<<<<< HEAD
from book import Book

class Student:
    def __init__(self, student_id, name, password, batch):
        self.student_id = student_id
        self.name = name
        self.password = password
        self.batch = batch
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
=======
from book import Book # Import the Book class so students can borrow and return books

class Student:
#represents a student in the library system
    def __init__(self, student_id, name, password, batch):
        self.student_id = student_id        # Unique ID assigned to each student
        self.name = name                    # Student's name
        self.password = password            # Student's password (stored in plain text)
        self.batch = batch                  # The department the student belongs to 
        self.borrowed_books = []           # List to store books the student has borrowed
#Attempts to borrow a book and adds it to the borrowed list.
    def borrow_book(self, book):
        if book.borrow():  # Call Book's borrow method
>>>>>>> 7575790 (adding comments in code)
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' not available.")

<<<<<<< HEAD
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
=======
#Returns a book if it was previously borrowed.
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()   # Call Book's return method
>>>>>>> 7575790 (adding comments in code)
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print("You didn't borrow this book.")

<<<<<<< HEAD
    def check_fines(self):
        print("No fines for now.")

=======
#Deregisters the student from the system.
>>>>>>> 7575790 (adding comments in code)
    def deregister(self):
        print(f"{self.name} deregistered.")
        return True

<<<<<<< HEAD
=======
#Lists all the books currently borrowed by the student.
>>>>>>> 7575790 (adding comments in code)
    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for b in self.borrowed_books:
                print(f"- {b.title} (ID: {b.book_id})")
<<<<<<< HEAD

=======
#Generate a unique ID based on last entry in students.csv
>>>>>>> 7575790 (adding comments in code)
def create_id():
    try:
        with open("data/students.csv", "r") as f:
            lines = list(csv.reader(f))
<<<<<<< HEAD
            last = lines[-1][0]
            num = int(last[2:]) + 1
            return f"st{num:04d}"
    except:
        return "st0001"

=======
            last = lines[-1][0]    # Get last student ID like 'st0002'
            num = int(last[2:]) + 1
            return f"st{num:04d}"   # Returns ID like 'st0003'
    except:
        return "st0001"  # Start from 'st0001' if file is missing

#Saves a new student record to students.csv file.
>>>>>>> 7575790 (adding comments in code)
def save_student(student):
    with open("data/students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student.student_id, student.name, student.password, student.batch])
    print("Student saved.")

<<<<<<< HEAD
=======
# Authenticates a student using ID and password.
    Returns a Student object if found, else None
>>>>>>> 7575790 (adding comments in code)
def stud_auth(sid, pwd):
    try:
        with open("data/students.csv", "r") as f:
            for row in csv.reader(f):
                if row[0] == sid and row[2] == pwd:
                    return Student(row[0], row[1], row[2], row[3])
    except FileNotFoundError:
        print("students.csv not found.")
    return None
