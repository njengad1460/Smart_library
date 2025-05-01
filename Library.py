from book import Book # This is the abstraction part

class Library:
    def __init__(self, name): # create a new library with a name and an rmpty list book
        self.name = name   #this creat a library name
        self.books = []    #an empty list is created to store the books
    
    def add_book(self, Book): #add a boot object to the library correction
        self.books.append(Book) #this adds the book to the list of books in the library
        # return f"'{Book.title}' has been added to the library."
    def return_book(self, title): #this method is used to return a book
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return f"'{book.title}' has been returned."
        return f"'{title}' not found in the library."
        
    def list_books(self): # return a list of all books and their details
        
        return [book.get_details() for book in self.books]
    
    def find_book(self, title): #this search the book by title (case-insensitive)
        #if found return the book object & if not return none
        for Book in self.books:
            if Book.title.lower() == title.lower():
                return Book
        return None
         