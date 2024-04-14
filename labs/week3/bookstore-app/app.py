from bookstore import Bookstore
def main():

    print("--------------------------------------------------------")
    print("---Hello and welcome to the awesome Lexicon bookstore---")
    print("--------------------------------------------------------\n")

    #innitiate variable to call the main class
    bookstore = Bookstore()
    user_choice = ""
    
    while user_choice != 8:
        print("--------------------------")
        print("------Menu options:-------")
        print("--------------------------")
        print("1.Add a book\n2.View all books\n3.Search a book by title\n4.Update a book price\n5.Delete a book\n6.View books by author\n7.View books in Stock\n8.Exit\n")
        user_choice = input("Type the number of your next action: ")

        if user_choice == "1":
            print("--------------------------")
            print("---Selected: Add a book---")
            print("--------------------------")
            bookstore.add_new_book()
            print("book successfuly added to bookstore.\n")
        elif user_choice == "2":
            print("--------------------------")
            print("-Selected: View all books-")
            print("--------------------------")
            bookstore.view_book()
            print("---All Book view ended.---\n")
        # Search book by title
        elif user_choice == "3":
            print("------------------------------------")
            print("---Selected: View books by author---")
            print("------------------------------------")
            bookstore.search_by_title()
            print("--------List ended.------\n")
        elif user_choice == "4":
            print("--------------------------")
            print("--Selected: Update price--")
            print("--------------------------")
            bookstore.update_book_price()
            print("----Price update ended----\n")

        # Delete book
        elif user_choice == "5":
            print("---------------------------")
            print("---Selected: Delete book---")
            print("---------------------------")
            bookstore.delete_book()
            print("---Delete book action ended.---\n")
        # View books by author
        elif user_choice == "6":
            print("------------------------------------")
            print("---Selected: View books by author---")
            print("------------------------------------")
            bookstore.search_by_author()
            print("--------List ended.------\n")
        # Placeholder for view books in stock
        elif user_choice == "7":
            pass
        elif user_choice == "8":
            print("Exiting bookstore program.")
            return
        else:
            print("Invalid choice. Please select a valid action.")

main()

# def generate_id():
#     new_id = [0,0,0,0]
#     while new_id[0] == 0:
#         digits = list(range(10))
#         random.shuffle(digits)
#         new_id = digits[:4]
#         id_number = int(''.join(map(str, new_id)))
#     return id_number
# generate_id()

