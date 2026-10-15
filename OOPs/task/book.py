class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            for book in self.books:
                print("Title:", book.title)
                print("Author:", book.author)
                print()

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book Found!")
                print("Title:", book.title)
                print("Author:", book.author)
                return

        print("Book Not Found!")


library = Library()

while True:

    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(title, author)
        library.add_book(book)

    elif choice == "2":

        library.display_books()

    elif choice == "3":

        title = input("Enter book title to search: ")
        library.search_book(title)

    elif choice == "4":

        print("Program exited")
        break

    else:
        print("Invalid choice")