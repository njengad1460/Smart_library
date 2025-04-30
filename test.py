from book import book
from Library import Library

lib = Library("Telst Library") #this creat a new libraly with a name

lib.add_book(book("Atomic Habit", "James kim",2018))
lib.add_book(book("Deep Work", "Cal Dev", 2016))

print("Library Catalogue")

for book in lib.list_books():
    print("\n", book)

num = book2 = input("Enter the book title to borrow: ") #this takes the book title from the user
found = lib.find_book(book2) #this search for the book
print(found.borrow()) if found else print("Book not Found")#this borrow the book