from typing import List


class Searchable:

    def search_book(self, value: str):
        pass


class Borrowable:

    def borrow_book(self, book: Book):
        pass


class Book(Searchable, Borrowable):

    def __init__(self, title: str, autor: str, isbn: str):
        self.title = title
        self.autor = autor
        self.isbn = isbn


class SearchBook:

    def search_book(self, value: str):
        pass


class SearchStrategy:

    def search_book(self, value: str):
        pass


class TitleSearchStrategy(SearchStrategy):

    def __init__(self, books: List[Book]):
        self.books = books

    def search_book(self, value: str):
        lst_books = []
        for book in self.books:
            if book.autor == value:
                lst_books.append(book)
        return lst_books


class AuthorSearchStrategy(SearchStrategy):

    def __init__(self, books: List[Book]):
        self.books = books

    def search_book(self, value: str):
        lst_books = []
        for book in self.books:
            if book.autor == value:
                lst_books.append(book)
        return lst_books


class IsbnSearchStrategy(SearchStrategy):

    def __init__(self, books: List[Book]):
        self.books = books

    def search_book(self, value: str):
        lst_books = []
        for book in self.books:
            if book.isbn == value:
                lst_books.append(book)
        return lst_books


class LibraryCatalog:

    def __init__(self, search_strategy: SearchStrategy):
        self.search_strategy = search_strategy
        self.books = []

    def search_book_by_title(self, value: str):
        return self.search_strategy.search(value)


    def add_book(self, title: str, author: str, isbn: str):
        self.books.append(Book(title, author, isbn))


class User:

    def __init__(self, name):
        self.name = name


class Member(User):

    def __init__(self, name: str):
        super().__init__(name)


class Borrowable:
    def borrow_book(self, book: Book):
        pass


class BorrowingMember(Member, Borrowable):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)
        