import csv

def save_all_books(all_books):
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "isbn", "year", "price", "quantity"])
        writer.writeheader()
        for book in all_books:
            writer.writerow(book)
