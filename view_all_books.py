import csv

def view_all_books():
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.DictReader(file)
            all_books = list(reader)
            if not all_books:
                print("No books available in the system.")
            else:
                for book in all_books:
                    print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}")
    except FileNotFoundError:
        print("No books file found. Please add a book first.")
