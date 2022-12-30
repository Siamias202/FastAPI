from fastapi import APIRouter,HTTPException,Request
from models.book import Book
from typing import List

book_router = APIRouter()

@book_router.get('/')
async def getallbooks()->List[Book]:
    books = await Book.find_all().to_list()
    if len(books)==0:
        return {"message":"No books found"}
    return books    

@book_router.post('/')
async def addbook(book:Book):
    try:
        await book.create()
        return {"message":"Book added"}
    except:
        raise HTTPException(status_code=404,detail="Unable to add")
              

@book_router.get('/book')
async def retrievebook(info:Request)->Book:
    req_info=await info.json()
    id=req_info["book_id"]

    try:
       book_to_get = await Book.find_one(Book.book_id==id)
       return book_to_get
    except:
        raise HTTPException(status_code=404,detail="Unable to find")   
  

@book_router.put('/')
async def updatebook(info:Request):
    req_info =await info.json()
    id=req_info["book_id"]
    new_price=req_info["price"]
    try:
        book_to_get=await Book.find_one(Book.book_id==id)
        book_to_get.price=new_price
        await book_to_get.save()
        return {"message":"Book updated"}
    except:
        raise HTTPException(status_code=404,detail="Unable to update")   
    





@book_router.delete('/')
async def deletebook(info:Request):
    req_info = await info.json()
    id=req_info["book_id"]
    try:
        book_to_get= await Book.find_one(Book.book_id==id)
        if(len(book_to_get)==0):
            return {"message":"No Book Found"}

        book_to_get.delete()    
        return {"message":"Book Deleted"}    

        
    except:
         raise HTTPException(status_code=404,detail="Unable to delete")    

    

