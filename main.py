from user import Student, create_id, save_student, stud_auth
from librarian import Librarian, create_lib_id, save_librarian, auth_librarian
from library import Library
from book import Book
from pwinput import pwinput

library = Library()

def main_menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Student Login")
        print("2. Student Register")
        print("3. Librarian Login")
        print("4. Librarian Register")
        print("Press Enter to Exit")

        choice = input("Select an option: ").strip()

        if choice == "":
            break
        elif choice == '1':
            student_login()
        elif choice == '2':
            student_register()
        elif choice == '3':
            librarian_login()
        elif choice == '4':
            librarian_register()
        else:
            print("Invalid option.")

def student_login():
    sid = input("Student ID: ").strip()
    pwd = pwinput("Password: ").strip()
    student = stud_auth(sid, pwd)
    if student:
        print(f"\nWelcome, {student.name}!")
        student_menu(student)
    else:
        print("Invalid student ID or password.")

def student_register():
    name = input("Name: ").strip()
    pwd = pwinput("Password: ").strip()
    confirm = pwinput("Confirm Password: ").strip()

    if pwd != confirm:
        print("Passwords do not match.")
        return

    batch = input("Batch: ").strip()
    student_id = create_id()
    student = Student(student_id, name, pwd, batch)
    save_student(student)
    print(f"Student registered successfully. Your ID is {student_id}")

def student_menu(student):
    while True:
        print("\n--- Student Menu ---")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View My Borrowed Books")
        print("Press Enter to Logout")

        choice = input("Select an option: ").strip()

        if choice == "":
            break
        elif choice == '1':
            library.list_all_books()
        elif choice == '2':
            book_id = input("Enter Book ID to borrow: ").strip()
            book = library.get_book_by_id(book_id)
            if book:
                student.borrow_book(book)
                library.save_books()
            else:
                print("Book not found.")
        elif choice == '3':
            book_id = input("Enter Book ID to return: ").strip()
            book = library.get_book_by_id(book_id)
            if book:
                student.return_book(book)
                library.save_books()
            else:
                print("Book not found.")
        elif choice == '4':
            student.list_borrowed_books()
        else:
            print("Invalid option.")

def librarian_login():
    lid = input("Librarian ID: ").strip()
    pwd = pwinput("Password: ").strip()
    librarian = auth_librarian(lid, pwd)
    if librarian:
        print(f"\nWelcome, {librarian.name}!")
        librarian_menu(librarian)
    else:
        print("Invalid librarian ID or password.")

def librarian_register():
    name = input("Name: ").strip()
    pwd = pwinput("Password: ").strip()
    confirm = pwinput("Confirm Password: ").strip()

    if pwd != confirm:
        print("Passwords do not match.")
        return

    librarian_id = create_lib_id()
    librarian = Librarian(librarian_id, name, pwd)
    save_librarian(librarian)
    print(f"Librarian registered successfully. Your ID is {librarian_id}")

def librarian_menu(librarian):
    while True:
        print("\n--- Librarian Menu ---")
        print("1. View All Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("Press Enter to Logout")

        choice = input("Select an option: ").strip()

        if choice == "":
            break
        elif choice == '1':
            library.list_all_books()
        elif choice == '2':
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            copies = int(input("Enter Number of Copies: ").strip())
            book = Book(book_id, title, author, copies)
            library.add_book(book)
            library.save_books()
        elif choice == '3':
            book_id = input("Enter Book ID to remove: ").strip()
            if library.remove_book(book_id):
                print("Book removed successfully.")
                library.save_books()
            else:
                print("Book not found.")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
