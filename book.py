class book: #a book is an object, it can carry allot of things, ie title, author....
    def __init__(self, title, author, year): # This is a constructer method to initialize the book object
        self.title = title
        self.author = author
        self.year = year
        self.available = True #availabel by default
        
    def borrow(self):
        if self.available: #if the book is available make it unavailable
            self.available = False #marks the book as bollowed if available 
            return f"You have borrowed '{self.title}'"
        return f"'{self.title}' is currently unavailabe " #if the book is borrowed/unavailabel return this satatent
    
    def return_book(self): # marks the book as returned 
        self.available = True
        return f"'{self.available}'has been returned"
    
    def get_details(self): # this returns formatted book information
        return f"{self.title} by {self.author} {self.year}"
    
    
        
    
        