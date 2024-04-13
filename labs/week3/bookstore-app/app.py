from bookstore import Bookstore
def main():

    print("--------------------------------------------------------")
    print("---Hello and welcome to the awesome Lexicon bookstore---")
    print("--------------------------------------------------------\n")

    #innitiate variable to call the main class
    bookstore = Bookstore()
    user_choice = ""
    
    while user_choice != 8:
        print("Menu options:\n")
        print("1.Add a book\n2.View all books\n3.Search a book by title\n4.Update a book price\n5.Delete a book\n6.View books by author\n7.View books in Stock\n8.Exit\n")
        user_choice = input("Type the number of your next action: ")

        if user_choice == "1":
            print("--------------------------")
            print("Selected: Add a book")
            print("--------------------------")
            bookstore.add_new_book()
            print("--------------------------")
            print("book successfuly added to bookstore.")
            print("--------------------------")
        #todos below:
        # Placeholder for view all books
        elif user_choice == "2":
            print("--------------------------")
            print("Selected: View all books")
            print("--------------------------")
            bookstore.view_book()
            print("--------------------------")
            print("All Book view ended.")
            print("--------------------------")
        # Placeholder for search book by title
        elif user_choice == "3":
            pass
        # Placeholder for update book price
        elif user_choice == "4":
            pass
        # Placeholder for delete book
        elif user_choice == "5":
            pass
        # Placeholder for view books by author
        elif user_choice == "6":
            pass
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

