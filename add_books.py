import csv
from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = input("Enter ISBN Number: ")
    year = int(input("Enter Publishing Year Number: "))
    price = float(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity Number: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }
    
    all_books.append(book)
    save_all_books(all_books)