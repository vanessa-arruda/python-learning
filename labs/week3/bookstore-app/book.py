class Book:
    def __init__(self):
        self.book_title = str(input("Type the book title: "))
        self.book_volume = int(input("If part of series book, type the book number (0 if not): "))
        self.book_author_name = str(input("Type the author's name: "))
        self.book_author_surname = str(input("Type the author's surname: "))
        self.book_pages = int(input("Type the number of pages: "))
        self.book_price = int(input("Type the book price: "))
        self.book_stock = int(input("Type the stock amount of this current book: "))
