from Library import Library
from book import Book
from digitalbook import DigitalBook
from magazines import Magazines

def main():
    library = Library("Smart Library")
    
    # Add various books types to the library
    library.add_book(Book("Python for All", "John Wamalwa", 2018))
    library.add_book(DigitalBook("Python for All", "John Wamalwa", 2018, 2.5))
    library.add_book(Magazines("Python Magazine", "John Wangula", 2020))
    
    while True:
        print("\nWelcome to the Smart Library!")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Rate a book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            print("\nAvailable books:")
            for b in library.books:
                print(f"- {b.get_details()}")
                
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            selected_book = library.find_book(title)
            if selected_book:
                print(selected_book.borrow())
            else:
                print(f"'{title}' not found in the library.")
                
        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)
            
        elif choice == "4":
            title = input("Enter the title of the book you want to rate: ")
            selected_book = library.find_book(title)
            if selected_book:
                try:
                    rating = float(input("Enter your rating (0-5): "))
                    selected_book.rate_book(rating)
                    print(f"Thank you for rating '{title}' with a score of {rating}.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 5.")
            else:
                print(f"'{title}' not found in the library.")
                
        elif choice == "5":
            print("Thank you for using the Smart Library!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# from Library import Library
# from book import book
# from digitalbook import DigitalBook
# from magazines import magazines


# def main():
    
#     library = Library("Smart Library")
    
#     #add variaus books types to the library
#     library.add_book(book("Python for All", "John Wamalwa", 2018))
#     library.add_book(DigitalBook("Python for Jones", "John Wamalwa", 2018, 2.5))
#     library.add_book(magazines("Python Magazine", "John Wangula", 2020))
    
#     while True:
#         print("\nWelcome to the Smart Library!")
#         print("1. View all books")
#         print("2. Borrow a book")
#         print("3. return to main menu")
#         print("4. rate a book")
#         print("5. Exit")
        
#         choice = input("Enter your choice: (1-5) ")
        
#         if choice == "1":
#             print("\n Available books:")
#             for book in library.books:
#                 print(f"- {book.get_details()}")
                
#         elif choice == "2":
#             title = input("Enter the title of the book you want to borrow: ")
#             book = library.find_book(title)
#             if book:
#                 print(book.borrow())
#             else:
#                 print(f"'{title}' not found in the library.")
#         elif choice == "3":
#             title = input("Enter the title of the book you want to return: ")
#             library.return_book(title)
#         elif choice == "4":
#             title = input("Enter the title of the book you want to rate: ")
#             book = library.find_book(title)
#             if book:
#                 try:
#                     rating = float(input("Enter your rating (0-5): "))
#                     book.rate_book(rating)
#                     print(f"Thank you for rating {title} with a score of {rating}.")
#                 except ValueError:
#                     print("Invalid input. Please enter a number between 0 and 5.")
#             else:
#                 print(f"'{title}' not found in the library.")
#                 continue
#         elif choice == "5":
#             print("Thank you for using the Smart Library!")
#             break
        
#         else:
#             print("Invalid choice. Please try again.")
# if __name__ == "__main__":
#     main()