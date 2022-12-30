from beanie import Document

class Book(Document):
    book_id:int
    name:str
    author:str
    category:str
    publisher:str
    year:int
    price:int
    tc:bool

    class settings:
        name="book_shop"
