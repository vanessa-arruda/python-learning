import pymongo
from bson.objectid import ObjectId
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

    def view_book(self):
        #prints all documents in the collection in the terminal directly
        print("All current books in the bookstore: \n")
        print(f"Total books count: {self.bookcol.count_documents({})}\n")
        print("All current books details: ")
        list_counter = 0
        for book in self.bookcol.find():
            # Print each book's details
            list_counter += 1
            print("--------------------------")
            print(list_counter,".""Book Id: ", book["_id"],"| " "title: ", book["title"], "| ""volume: ", book["volume"], "| ""pages: ", book["pages"])
            print("Author: ", book["author_name"], book["author_surname"])
            print("Price in SEK: {:.2f}".format(book["price"]))
            print("Stock: ", book["stock"])
            print("--------------------------\n")

    def update_book_price(self):
        user_input_id = str(input("Type book ID: "))
        query = ({"_id": ObjectId(user_input_id)})
        # choose which key to update - implement later
        # print("1.Title\n2.Volume\n3.Author name\n4.Author surname\n5.Pages\n6.Price\n7.Stock\n")
        # updated_key = str(input("Select attribute you want to update: "))
        updated_value = float(input("Set new price (SEK): "))
        new_value = {"$set":{"price": updated_value}}
        self.bookcol.update_one(query, new_value)
        print("Book price updated")

    def delete_book(self):
        user_input = str(input("Type corresponding ID to delete the book: "))
        delete_query = ({"_id": ObjectId(user_input)})
        print(delete_query)
        result = self.bookcol.delete_one(delete_query)
        print(f"Book removed from bookstore.")
        print(result)
        print(f"Total current books count: {self.bookcol.count_documents({})}\n")

    def search_by_author(self):
        print("List of books by AUTHOR in the bookstore: \n")
        # Print each book's details
        list_counter = 0
        book_list = self.bookcol.find().sort("author_name")
        for book in book_list:
            list_counter += 1
            print(list_counter,". ""Author: ", book["author_name"], book["author_surname"], "|", "Book Id: ", book["_id"],"|","Title: ", book["title"],"|","Volume: ", book["volume"],"|","Pages: ", book["pages"],"|","Price in SEK: {:.2f}".format(book["price"]),"|","Stock: ", book["stock"])
    
    def search_by_title(self):
        print("List of books by TITLE in the bookstore: \n")
        # Print each book's details
        list_counter = 0
        book_list = self.bookcol.find().sort("title")
        for book in book_list:
            list_counter += 1
            print(list_counter,".","Title: ", book["title"],"|", "Volume: ", book["volume"],"|" "Book Id: ", book["_id"],"|", "Author: ", book["author_name"], book["author_surname"], "|","Pages: ", book["pages"],"|","Price in SEK: {:.2f}".format(book["price"]),"|","Stock: ", book["stock"])