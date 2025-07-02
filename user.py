import csv
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
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print("You didn't borrow this book.")

    def check_fines(self):
        print("No fines for now.")

    def deregister(self):
        print(f"{self.name} deregistered.")
        return True

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for b in self.borrowed_books:
                print(f"- {b.title} (ID: {b.book_id})")

def create_id():
    try:
        with open("data/students.csv", "r") as f:
            lines = list(csv.reader(f))
            last = lines[-1][0]
            num = int(last[2:]) + 1
            return f"st{num:04d}"
    except:
        return "st0001"

def save_student(student):
    with open("data/students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student.student_id, student.name, student.password, student.batch])
    print("Student saved.")

def stud_auth(sid, pwd):
    try:
        with open("data/students.csv", "r") as f:
            for row in csv.reader(f):
                if row[0] == sid and row[2] == pwd:
                    return Student(row[0], row[1], row[2], row[3])
    except FileNotFoundError:
        print("students.csv not found.")
    return None
