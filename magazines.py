from book import book

class magazines(book):
    def __init__(self, title, editor, year): #we still call parent constroctor, but use editor instead of author
        super().__init__(title, editor, year)
    
    def borrow(self): #magazines can't be borrowed override the borrow method
        return f"{self.title} this is a magazine and is not supporse to be borrowed"
        