import csv

def view_all_books(all_books):
    try:
        if not all_books:
            print("No books available in the system.")
        else:
            for book in all_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}")
    except Exception as e:
        print(f"Error reading books: {e}")