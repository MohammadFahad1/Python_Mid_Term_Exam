class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability = True) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"The book {self.title} has been borrowed")
            return True
        else:
            print(f"The book {self.title} is already borrowed")
            return False

    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"The book {self.title} has been returned")
            return True
        else:
            print(f"The book {self.title} is not borrowed")
            return False

    def view_book_info(self):
        print(f"Book Id: {self.book_id} Title: {self.title} Author: {self.author} Availability: {"Available" if self.availability else "Not Available"}")


Book(101, "1984", "George Orwell")
Book(102, "To Kill a Mockingbird", "Harper Lee")
Book(103, "The Great Gatsby", "F. Scott Fitzgerald")

while True:
    print("\nLibrary Menu")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            for book in Library.book_list:
                book.view_book_info()
        elif choice == 2:
            book_id = int(input("Enter the Book ID to borrow: "))
            book = next((b for b in Library.book_list if b.book_id == book_id), None)
            if book:
                book.borrow_book()
            else:
                print("Book not found.")
        elif choice == 3:
            book_id = int(input("Enter the Book ID to return: "))
            book = next((b for b in Library.book_list if b.book_id == book_id), None)
            if book:
                book.return_book()
            else:
                print("Book not found.")
        elif choice == 4:
            print("Exiting the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")