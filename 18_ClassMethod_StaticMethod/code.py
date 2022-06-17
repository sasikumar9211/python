class Book:

    TYPE = ("hardcover","paperback")

    def __init__(self,name, book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type},weighting {self.weight} g>"
    
    @classmethod
    def hardcover(cls,name,page_Weight):
        return cls(name,cls.TYPE[0],page_Weight+100)

    
    @classmethod
    def paperback(cls,name,page_Weight):
        return cls(name,cls.TYPE[1],page_Weight)

    @staticmethod
    def staticMethods():
        print ("In StaticMethods")
    


book = Book.hardcover("Harry Potter",1500)

book2 = Book.paperback("python 101",600)

print(book)
print(book2)

Book.staticMethods()