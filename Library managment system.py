import json
import os

# ---------- Book Class ----------
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        """Convert book object to dictionary for JSON storage"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }


# ---------- Library Class ----------
class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Load books from JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book(**book) for book in data]
        else:
            self.books = []

    def save_books(self):
        """Save books to JSON file"""
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, title, author, isbn):
        """Add a new book"""
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        print(f"✅ Book '{title}' added successfully!")

    def list_books(self):
        """List all books"""
        if not self.books:
            print("No books available.")
        else:
            print("\n📚 Library Books:")
            for book in self.books:
                status = "✅ Available" if book.available else "❌ Borrowed"
                print(f"- {book.title} by {book.author} (ISBN: {book.isbn}) → {status}")

    def borrow_book(self, isbn):
        """Borrow a book if available"""
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    self.save_books()
                    print(f"📖 You borrowed '{book.title}' successfully!")
                    return
                else:
                    print("⚠ Book already borrowed.")
                    return
        print("❌ Book not found.")

    def return_book(self, isbn):
        """Return a borrowed book"""
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    self.save_books()
                    print(f"✅ You returned '{book.title}' successfully!")
                    return
                else:
                    print("⚠ This book was not borrowed.")
                    return
        print("❌ Book not found.")


# ---------- Menu ----------
def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "2":
            library.list_books()

        elif choice == "3":
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(isbn)

        elif choice == "4":
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)

        elif choice == "5":
            print("👋 Exiting Library System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()