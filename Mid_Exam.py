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