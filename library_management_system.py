from add_books import add_books
from view_all_books import view_all_books

def main():
    all_books = []

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_books(all_books)
        elif choice == '2':
            view_all_books()
        elif choice == '3':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")