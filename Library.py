from book import book # This is the abstraction part

class Library:
    def __init__(self, name): # create a new library with a name and an rmpty list book
        self.name = name   #this creat a library name
        self.books = []    #an empty list is created to store the books
    
    def add_book(self, book): #add a boot object to the library correction
        self.books.append(book)
        
        
    def list_books(self): # return a list of all books and their details
        
        return [book.get_details() for book in self.books]
    
    def find_book(self, title): #this search the book by title (case-insensitive)
        #if found return the book object & if not return none
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
         