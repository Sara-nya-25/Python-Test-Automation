class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_on_loan = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_author(self, author):
        return [b for b in self.books if author.lower() in b.author.lower()]

    def find_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None