import csv

def save_all_books(all_books):
    try:
        with open('books.csv', mode='w', newline='') as file:
            fieldnames = ['title', 'author', 'isbn', 'year', 'price', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_books)
    except Exception as e:
        print(f"Error saving books: {e}")