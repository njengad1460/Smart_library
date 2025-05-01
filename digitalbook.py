from book import book

class DigitalBook(book): #this is the child class of book
    def __init__(self, title, author, year, file_size): #this is the constructor method
        super().__init__(title, author, year) #we use super to ingerit attributes from the book class
        self.file_size = file_size
        
    def stream(self): #this method is used to stream the book
        return f"Streaming {self.title} by {self.author} ({self.year}) with file size {self.file_size}MB"
    
    def borrow(self): #this overrides the borrow method of the book class
        return f"{self.title} is a digital book. You can steram it online."
        