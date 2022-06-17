class TooManyPageReadError (Exception):
    pass

class Book:

    def __init__(self,name: str, page_count: int):
        self.name= name
        self.page_count= page_count
        self.page_read= 0
    

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.page_read} pages out of {self.page_count}"
        )
    
    def read(self, pages: int):

        if self.page_read + pages > self.page_count:
            raise TooManyPageReadError(
                f" you tried to read {self.page_read+pages},but the book has only {self.page_count} pages."
            )

        self.page_read += pages
        print(f" you have now read {self.page_read} pages out of {self.page_count}")


book = Book("Harry potter", 100)

try:
    book.read(50)
    book.read(50)
    book.read(50)
except TooManyPageReadError as e:
    print(f" Reading more than the available pages...")
finally:
    print("Thanks for Reading")

