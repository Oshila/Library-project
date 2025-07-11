<<<<<<< HEAD
=======
# Import necessary classes and helper functions
>>>>>>> 7575790 (adding comments in code)
from user import Student, create_id, save_student, stud_auth
from librarian import Librarian, create_lib_id, save_librarian, auth_librarian
from library import Library
from book import Book
<<<<<<< HEAD
from pwinput import pwinput

library = Library()

=======
from pwinput import pwinput  # For secure password input (no display)

# Create a Library instance to manage all books
library = Library()

# --------- MAIN MENU -------
>>>>>>> 7575790 (adding comments in code)
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
<<<<<<< HEAD
            break
=======
            break  # Exit loop if input is empty
>>>>>>> 7575790 (adding comments in code)
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

<<<<<<< HEAD
def student_login():
    sid = input("Student ID: ").strip()
    pwd = pwinput("Password: ").strip()
    student = stud_auth(sid, pwd)
    if student:
        print(f"\nWelcome, {student.name}!")
        student_menu(student)
=======
# -------- STUDENT SECTION --------
def student_login():
    # Prompt user for student login credentials
    sid = input("Student ID: ").strip()
    pwd = pwinput("Password: ").strip()
    student = stud_auth(sid, pwd)  # Authenticate from CSV

    if student:
        print(f"\nWelcome, {student.name}!")
        student_menu(student)  # Open student menu
>>>>>>> 7575790 (adding comments in code)
    else:
        print("Invalid student ID or password.")

def student_register():
<<<<<<< HEAD
=======
    # Gather registration info from user
>>>>>>> 7575790 (adding comments in code)
    name = input("Name: ").strip()
    pwd = pwinput("Password: ").strip()
    confirm = pwinput("Confirm Password: ").strip()

    if pwd != confirm:
        print("Passwords do not match.")
        return

    batch = input("Batch: ").strip()
<<<<<<< HEAD
    student_id = create_id()
    student = Student(student_id, name, pwd, batch)
    save_student(student)
=======
    student_id = create_id()  # Automatically generate student ID
    student = Student(student_id, name, pwd, batch)
    save_student(student)  # Save to CSV
>>>>>>> 7575790 (adding comments in code)
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
<<<<<<< HEAD
            library.list_all_books()
=======
            library.list_all_books()  # Show all books
>>>>>>> 7575790 (adding comments in code)
        elif choice == '2':
            book_id = input("Enter Book ID to borrow: ").strip()
            book = library.get_book_by_id(book_id)
            if book:
<<<<<<< HEAD
                student.borrow_book(book)
                library.save_books()
=======
                student.borrow_book(book)  # Borrow process
                library.save_books()  # Update CSV
>>>>>>> 7575790 (adding comments in code)
            else:
                print("Book not found.")
        elif choice == '3':
            book_id = input("Enter Book ID to return: ").strip()
            book = library.get_book_by_id(book_id)
            if book:
<<<<<<< HEAD
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
=======
                student.return_book(book)  # Return process
                library.save_books()  # Update CSV
            else:
                print("Book not found.")
        elif choice == '4':
            student.list_borrowed_books()  # Show borrowed books
        else:
            print("Invalid option.")

# ------ LIBRARIAN SECTION -------
def librarian_login():
    lid = input("Librarian ID: ").strip()
    pwd = pwinput("Password: ").strip()
    librarian = auth_librarian(lid, pwd)  # Validate credentials

>>>>>>> 7575790 (adding comments in code)
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
<<<<<<< HEAD
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
=======
            library.list_all_books()  # View all books
        elif choice == '2':
            # Prompt librarian to enter full book info
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            publisher = input("Enter Publisher: ").strip()
            publish_date = input("Enter Publish Date (e.g., 2025-08-01): ").strip()
            copies = int(input("Enter Number of Copies: ").strip())

            # Create book with all details in the correct order
            book = Book(book_id, title, author, publisher, publish_date, True, copies)
            library.add_book(book)  # Add to library
            library.save_books()    # Save to CSV
            print(f"Book '{title}' added successfully.")
        elif choice == '3':
            book_id = input("Enter Book ID to remove: ").strip()
            if library.remove_book(book_id):
                library.save_books()
                print("Book removed successfully.")
>>>>>>> 7575790 (adding comments in code)
            else:
                print("Book not found.")
        else:
            print("Invalid option.")

<<<<<<< HEAD
if __name__ == "__main__":
    main_menu()
=======
# ------ Run Program -----
if __name__ == "__main__":
    main_menu()  # Start the app
>>>>>>> 7575790 (adding comments in code)
