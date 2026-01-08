books = {
    "1984": {
        "author": "George Orwell",
        "year": 1949
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "year": 1960
    },
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    "Dracula": {
        "author": "Bram Stoker",
        "year": 1897
    },
    "Dune": {
        "author": "Frank Herbert",
        "year": 1965
    }
}
borrowed_books = []


def view_books():
    for title, info in books.items():
        print(f"Title: {title}")
        print(f"Author: {info['author']}")
        print(f"Year: {info['year']}")
        print()


def borrow_book(title):
    if title in books and title not in borrowed_books:
        borrowed_books.append(title)
        print(f"You have borrowed '{title}'.")
    else:
        print(f"Sorry, '{title}' is not available for borrowing.")


def return_book(title):
    if title in borrowed_books:
        borrowed_books.remove(title)
        print(f"You have returned '{title}'.")
    else:
        print(f"You did not borrow '{title}'.")
    print("Current borrowed books:")
    for book in borrowed_books:
        print(f"- {book}")


def add_book(title, author, year):
    if title not in books:
        books[title] = {
            "author": author,
            "year": year
        }
        print(f"Book '{title}' added successfully.")
    else:
        print(f"Book '{title}' already exists.")


def view_borrowed_books():
    if borrowed_books:
        print("Borrowed Books:")
        for book in borrowed_books:
            print(f"- {book}")
    else:
        print("No books are currently borrowed.")


while True:
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. View Borrowed Books")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_books()
    elif choice == "2":
        title = input("Enter the title of the book to borrow: ")
        borrow_book(title)
    elif choice == "3":
        title = input("Enter the title of the book to return: ")
        return_book(title)
    elif choice == "4":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = int(input("Enter the year of publication: "))
        add_book(title, author, year)
    elif choice == "5":
        view_borrowed_books()
    elif choice == "6":
        break

    else:
        print("Invalid choice. Please try again.")
