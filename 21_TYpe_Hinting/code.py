class Book:

    TYPE = ("hardcover","paperback")

    def __init__(self,name:  str, book_type: str,weight:  int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type},weighting {self.weight} g>"
    
    @classmethod
    def hardcover(cls,name: str,page_Weight: int) -> "Book":
        return cls(name,cls.TYPE[0],page_Weight+100)

    
    @classmethod
    def paperback(cls,name:  str,page_Weight: int) -> "Book":
        return cls(name,cls.TYPE[1],page_Weight)

    @staticmethod
    def staticMethods():
        print ("In StaticMethods")
    


book = Book.hardcover("Harry Potter",1500)

book2 = Book.paperback("python 101",600)

print(book)
print(book2)

Book.staticMethods()