class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")
    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print(book)
    def search_book(self, name):
        if name in self.books:
            print("Book found:", name)
        else:
            print("Book not found.")
library = Library()
while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        name = input("Enter book name to search: ")
        library.search_book(name)
    elif choice == "4":
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice!")
