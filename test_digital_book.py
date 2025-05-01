from digitalbook import DigitalBook

ebook= DigitalBook("Python for All", "Johs wamalwa", 2018, 2.5) #this creat a new digital book with a name

print (ebook.get_details())

print(ebook.stream()) #unique to digital book
print(ebook.borrow()) #overrides the original method 

# dig = DigitalBook("Adding libraly for digital book")
# dig.add_book