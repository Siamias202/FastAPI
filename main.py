from fastapi import FastAPI

from Router.bookrouter import book_router
from Router.userrouter import user_router
from database.db_connect import init__db
app=FastAPI()


@app.on_event('startup')
async def connect():
    await init__db()
    

app.include_router(book_router,prefix='/books')
app.include_router(user_router,prefix="/users")

