import pymongo
from book import Book
class Bookstore:
    
    def __init__(self):
        #MongoDB URI format - connect on the default host and port
        #create inside Bookstore so the connection and request happens only when Bookstore is selected (memory)
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.maindb = self.client["bookstore"]
        self.bookcol = self.maindb["book"]
        # self.actions = ["1.Add a book", "2.View all books", "3.Search a book by title", "4.Update a book price", "5.Delete a book", "6.View books by author", "7.View books in Stock", "8.Exit"]
    #CRUD
    def add_new_book(self):
        # Create a new Book instance
        new_book = Book()
        # Insert the book details into MongoDB
        result = self.bookcol.insert_one({
            "title": new_book.book_title,
            "volume": new_book.book_volume,
            "author_name": new_book.book_author_name,
            "author_surname": new_book.book_author_surname,
            "pages": new_book.book_pages,
            "price": new_book.book_price,
            "stock": new_book.book_stock
        })
        print(result)
        # print("Inserted document ID", result.inserted_id)

    def view_book(self):
        #prints all documents in the collection in the terminal directly
        print("All current books in the bookstore: \n")
        for book in self.bookcol.find():
            # Print each book's details
            print("--------------------------")
            print("Book Id: ", book["_id"])
            print("Title: ", book["title"])
            print("Volume: ", book["volume"])
            print("Author: ", book["author_name"], book["author_surname"])
            print("Pages: ", book["pages"])
            print("Price: ", book["price"])
            print("Stock: ", book["stock"])
            print("--------------------------\n")

    def update_book_price():
        pass
    def delete_book():
        pass
    def search_book():
        pass