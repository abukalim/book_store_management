import json
import os

# File to store book data
FILE_NAME = "books.json"

# Load existing books from file
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book():
    books = load_books()
    isbn = input("Enter ISBN: ")
    if any(book['ISBN'] == isbn for book in books):
        print("Book with this ISBN already exists!")
        return
    
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    try:
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        print("Invalid input! Price must be positive and quantity must be a non-negative integer.")
        return
    
    books.append({"ISBN": isbn, "Title": title, "Author": author, "Genre": genre, "Price": price, "Quantity": quantity})
    save_books(books)
    print("Book added successfully!")

# View all books
def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    print("\nBook List:")
    for book in books:
        print(f"ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Price: ${book['Price']}, Stock: {book['Quantity']}")

# Search books
def search_books():
    books = load_books()
    if not books:
        print("No books available to search.")
        return
    
    query = input("Enter title, author, or ISBN to search: ").lower()
    found_books = [book for book in books if query in book['Title'].lower() or query in book['Author'].lower() or query == book['ISBN']]
    
    if found_books:
        for book in found_books:
            print(f"ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']}, Price: ${book['Price']}, Stock: {book['Quantity']}")
    else:
        print("No books found.")

# Remove a book
def remove_book():
    books = load_books()
    if not books:
        print("No books available to remove.")
        return
    
    isbn = input("Enter ISBN of the book to remove: ")
    new_books = [book for book in books if book['ISBN'] != isbn]
    
    if len(new_books) == len(books):
        print("Book not found!")
    else:
        save_books(new_books)
        print("Book removed successfully!")

# Menu system
def menu():
    while True:
        print("\n--- Book Store Management ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
