#Section B
#Question two
#(i)
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return (f'{self.title},{self.author},{self.pages}')
information=Book('The animal Farm','Goerge Orwel',250)
print(information)


#(ii)
class EBook:
    def __init__(self,title,author,pages,format):
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format
        def __str__(self):
            return (f'{self.title},{self.author},{self.pages},{self.fgormat}')
#information=Book('The animal Farm','Goerge Orwel',250,'ebook')
#print(information)

   
   #(iii)
# A "Book" class that returns only the book title and the author
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return (f'{self.title} by {self.author}')
book1=Book('The Animal Farm','Geoge Orwel')
print(book1)

#(iv)
A class is a user-defined data type that provides a collecting yard of  objects.

An object refers to a subset(characteristics) of a class.
    